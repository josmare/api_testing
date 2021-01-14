# API testing with python
import requests
import os
import pytest

HEADER = {'x-api-key': os.getenv('API_KEY')}
URL = 'https://l9njuzrhf3.execute-api.eu-west-1.amazonaws.com/prod'


@pytest.fixture
def user_json():
    return requests.get(url=URL + '/user', headers=HEADER).json()


def test_usernames_are_strings(user_json):
    for i in user_json:
        assert type(user_json[i]['first_name']) is str
        assert type(user_json[i]['last_name']) is str
        assert type(user_json[i]['last_name']) is str
