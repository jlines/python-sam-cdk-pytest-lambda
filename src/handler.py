import json

import src.routes.device as device

# import items as device


# import requests


def lambda_handler(event, context):

    if event["path"] == "/device":
        return device.lambda_handler(event, context)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "default"}),
    }
