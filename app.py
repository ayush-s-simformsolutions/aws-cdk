#!/usr/bin/env python3
from aws_cdk import (
    Environment,
    Stack,
)
import aws_cdk as cdk
import os
from networking.networking import Networking
from servers.servers import AutoScalingGroup

env = Environment(
    account = os.environ["CDK_DEFAULT_ACCOUNT"], 
    region = os.environ["CDK_DEFAULT_REGION"],
)
app = cdk.App()
main_stack = Stack(
    app, 
    "Project_name",
)
networking = Networking(
    main_stack, 
    "Networking",
)
AutoScalingGroup(main_stack, "Servers", 
    vpc = networking.vpc
)
app.synth()