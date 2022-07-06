#!/usr/bin/env python3
import aws_cdk as cdk
from networking.networking import Networking
from servers.servers import Servers

app = cdk.App()
Networking(app, "Networking")
Servers(app, "Servers")
app.synth()