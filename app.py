#!/usr/bin/env python3

import aws_cdk as cdk

from cdk.networking import Networking



app = cdk.App()
Networking(app, "Networking")



app.synth()
