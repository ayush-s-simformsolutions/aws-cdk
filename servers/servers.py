from constructs import Construct
from networking.networking import Networking
from aws_cdk import (
    Stack,
    NestedStack,
    aws_ec2 as ec2,
)

class AutoScalingGroup(NestedStack):
    def __init__(self, scope: Construct, construct_id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        ec2_instance = ec2.Instance(self, 'Instance', 
            vpc = vpc,
            vpc_subnets = ec2.SubnetSelection(
                subnet_type = ec2.SubnetType.PRIVATE_WITH_NAT
            ),
            instance_type = ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3,
                ec2.InstanceSize.MICRO,
            ),
            machine_image = ec2.AmazonLinuxImage(
                generation = ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            ),
        )
        