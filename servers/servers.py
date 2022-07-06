from constructs import Construct
from networking.networking import Networking
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    Fn,
    CfnOutput,
)

class Servers(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
 
        ec2_instance = ec2.Instance(self, 'Instance', 
            vpc =  Fn.import_value('VpcID'),
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
        