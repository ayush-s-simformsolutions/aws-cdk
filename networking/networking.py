from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    CfnOutput,
    Tags,
    NestedStack,
)
import os

class Networking(NestedStack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.vpc = ec2.Vpc(self, 'VPC',
            vpc_name = os.getenv('PROJECT_NAME'),
            cidr = '10.0.0.0/16',
            max_azs = 3,
            subnet_configuration = [
                ec2.SubnetConfiguration(
                    cidr_mask = 24,
                    name = 'Public',
                    subnet_type = ec2.SubnetType.PUBLIC,
                ),
                ec2.SubnetConfiguration(
                    cidr_mask = 24,
                    name = 'Application',
                    subnet_type = ec2.SubnetType.PRIVATE_WITH_NAT,
                ),
                ec2.SubnetConfiguration(
                    cidr_mask = 24,
                    name = 'RDS',
                    subnet_type = ec2.SubnetType.PRIVATE_ISOLATED,
                ),
            ]
        )