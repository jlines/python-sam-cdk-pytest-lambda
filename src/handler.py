import json

import routes.example as example

# import items as device


# import requests


def lambda_handler(event, context):

    if event["path"] == "/example":
        return example.lambda_handler(event, context)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "default"}),
    }
