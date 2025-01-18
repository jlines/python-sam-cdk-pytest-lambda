import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_stacks.deploy_api_stack import ApiLambdaStack


# example tests. To run these tests, uncomment this file along with the example
# resource in deploy_cdk/deploy_cdk_stack.py
def test_handler_name():
    app = core.App()
    stack = ApiLambdaStack(app, "deploy-cdk")
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "Handler": "handler.lambda_handler",
        },
    )
