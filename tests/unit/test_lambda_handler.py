import json

import pytest

import handler


@pytest.fixture()
def apigw_event():
    """Generates API GW Event"""

    with open("./events/default_get.json", "r") as file:
        data = json.load(file)

    return data


def test_lambda_handler(apigw_event):

    ret = handler.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "default"


def test_example_handler(apigw_event):

    apigw_event["path"] = "/example"
    ret = handler.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "ipaddress" in ret["body"]
    assert data["ipaddress"] == "127.0.0.1"
