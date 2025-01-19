import json

import requests


def get_server_ip():
    # Call Amazon's checkip service to get the current IP address
    response = requests.get("https://checkip.amazonaws.com")
    return response.text.strip()


def lambda_handler(event, context):
    client_ip = event["requestContext"]["identity"]["sourceIp"]
    server_ip = get_server_ip()

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "ipaddress": client_ip,
                "serverip": server_ip,
            }
        ),
    }
