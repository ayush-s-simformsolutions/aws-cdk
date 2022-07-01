from constructs import Construct
import os
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_ec2 as ec2,
    Tags
)


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        vpc = ec2.Vpc(self, 'project_name', 
            cidr = os.getenv('cidr') 
        )
        Tags.of(vpc).add('Name', 'project_name')