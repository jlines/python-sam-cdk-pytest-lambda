import boto3
import pytest
import requests


class TestApiGateway:

    @pytest.fixture()
    def api_gateway_url(self):
        """Get the API Gateway URL from Cloudformation Stack outputs"""
        stack_name = "MyApiLambdaStack"

        if stack_name is None:
            raise ValueError("Configure stack_name in the test")

        client = boto3.client("cloudformation")

        try:
            response = client.describe_stacks(StackName=stack_name)
            # response = client.describe_stacks()
        except Exception as e:
            raise Exception(f"Cannot find stack {stack_name} \n") from e

        stacks = response["Stacks"]
        stack_outputs = stacks[0]["Outputs"]
        api_outputs = [output for output in stack_outputs if output["OutputKey"].startswith("MyAPI")]

        if not api_outputs:
            raise KeyError(f"MyAPI not found in stack {stack_name}")

        return api_outputs[0]["OutputValue"]  # Extract url from stack outputs

    def test_api_gateway(self, api_gateway_url):
        """Call the API Gateway endpoint and check the response"""
        response = requests.get(api_gateway_url)

        assert response.status_code == 200
        assert response.json() == {"message": "default"}
