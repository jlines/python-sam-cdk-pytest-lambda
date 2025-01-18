#!/usr/bin/env python3
import aws_cdk as cdk

from cdk_stacks.deploy_api_stack import ApiLambdaStack

app = cdk.App()
ApiLambdaStack(
    app,
    "ApiLambdaStack",
    env=cdk.Environment(account="{AWS_ACCOUNT_NUMBER}", region="us-east-1"),
)

app.synth()
