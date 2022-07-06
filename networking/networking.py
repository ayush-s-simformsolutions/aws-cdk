from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    CfnOutput,
)

class Networking(Stack):
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        vpc = ec2.Vpc(self, 'VPC', 
            cidr = '10.0.0.0/16',
            max_azs = 3,
            subnet_configuration = [
                ec2.SubnetConfiguration(
                    cidr_mask = 24,
                    name = 'ingress',
                    subnet_type = ec2.SubnetType.PUBLIC,
                ),
                ec2.SubnetConfiguration(
                    cidr_mask = 24,
                    name = 'application',
                    subnet_type = ec2.SubnetType.PRIVATE_WITH_NAT,
                ),
                ec2.SubnetConfiguration(
                    cidr_mask = 24,
                    name = 'rds',
                    subnet_type = ec2.SubnetType.PRIVATE_ISOLATED,
                ),
            ]
        )
        CfnOutput(self, 'VpcID', 
            value = vpc.vpc_id,
            description = 'The id of the VPC',
            export_name = 'VpcID'
        )