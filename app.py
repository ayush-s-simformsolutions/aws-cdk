#!/usr/bin/env python3


from aws_cdk import (
    Environment,
    Stack,
)
import aws_cdk as cdk
import os
from networking.networking import Networking
from servers.servers import AutoScalingGroup
from dotenv import load_dotenv

load_dotenv()

env = Environment(
    account = os.getenv('CDK_DEFAULT_ACCOUNT'), 
    region = os.getenv('CDK_DEFAULT_REGION'),
)
app = cdk.App()
main_stack = Stack(
    app,
    os.getenv('Project_name'),
)
networking = Networking(
    main_stack, 
    "Networking",
)
AutoScalingGroup(main_stack, "Servers", 
    vpc = networking.vpc
)
app.synth()