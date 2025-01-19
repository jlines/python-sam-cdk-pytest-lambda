#!/usr/bin/env python3
if __name__ == "__main__":
    from os import getenv

    import aws_cdk as cdk

    from cdk_stacks.deploy_api_stack import ApiLambdaStack

    account = getenv("AWS_DEFAULT_ACCOUNT")
    region = getenv("AWS_DEFAULT_REGION")

    print(f"Region: {region}")

    app = cdk.App()
    ApiLambdaStack(
        app,
        "MyApiLambdaStack",
        env=cdk.Environment(account=account, region=region),
    )

    app.synth()
