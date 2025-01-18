from aws_cdk import Stack
from aws_cdk import aws_apigateway as apigateway
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class ApiLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function
        my_lambda = _lambda.Function(
            self,
            "MyLambda",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="handler.lambda_handler",
            code=_lambda.Code.from_asset("./src"),  # solve module problems with pythonpath
        )

        # We can setup 2 way tls for the devices
        # https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mutual-tls.html
        # Define the API Gateway
        api = apigateway.LambdaRestApi(self, "MyAPI", handler=my_lambda, proxy=False)

        # Define a resource and method for the API
        items = api.root.add_resource("path")
        items.add_method("GET")  # GET /items
