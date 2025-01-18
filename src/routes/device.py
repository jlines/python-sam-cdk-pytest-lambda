import json

# import requests


def lambda_handler(event, context):
    client_ip = event["requestContext"]["identity"]["sourceIp"]

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "ipaddress": client_ip,
                "location": "locaton",
                "weather": {
                    "windspeed": "windspeed",
                    "cloudcover": "cloudcover",
                },
                "airquality": "airquality",
                "timezone_offset": "offset",
                "time": "time",
            }
        ),
    }
