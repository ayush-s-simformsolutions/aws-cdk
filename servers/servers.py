from constructs import Construct
import os
from networking.networking import Networking
from aws_cdk import (
    Stack,
    NestedStack,
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling
)

class Servers(NestedStack):
    def __init__(self, scope: Construct, construct_id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        securityGroup = ec2.SecurityGroup(self, 'SecurityGroup',
            vpc = vpc,
            allow_all_outbound = True,
            security_group_name = os.getenv('PROJECT_NAME'),
        )

        securityGroup.add_ingress_rule(
            peer = ec2.Peer.any_ipv4(),
            connection = ec2.Port.tcp(443),
            description = "HTTPS From Anywhere"
        )

        securityGroup.add_ingress_rule(
            peer = ec2.Peer.any_ipv4(),
            connection = ec2.Port.tcp(80),
            description = "HTTP From Anywhere"
        )

        securityGroup.add_ingress_rule(
            peer = ec2.Peer.any_ipv4(),
            connection = ec2.Port.tcp(22),
            description = "SSH From Anywhere"
        )

        launch_template = ec2.LaunchTemplate(self, 'LaunchTemplate', 
            launch_template_name = os.getenv('PROJECT_NAME'),
            instance_type = ec2.InstanceType(instance_type_identifier = os.getenv('INSTANCE_TYPE')),
            machine_image = ec2.AmazonLinuxImage(
                generation = ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            ),
            security_group = securityGroup,
        )
        
        asg = autoscaling.AutoScalingGroup(self, 'ASG', 
            vpc = vpc,
            vpc_subnets = ec2.SubnetSelection(
                subnet_type = ec2.SubnetType.PRIVATE_WITH_NAT
            ),
            launch_template = launch_template,
            auto_scaling_group_name = os.getenv('PROJECT_NAME'),
            min_capacity = 1,
            max_capacity = 6,
        )

