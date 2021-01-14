# API testing with python
import os
import pytest
import datetime
import requests

HEADER = {'x-api-key': os.getenv('API_KEY')}
URL = 'https://l9njuzrhf3.execute-api.eu-west-1.amazonaws.com/prod'


@pytest.fixture
def users_json():
    return requests.get(url=URL + '/user', headers=HEADER).json()


@pytest.fixture()
def group_json():
    return requests.get(url=URL + '/group', headers=HEADER).json()


def test_usernames_are_strings(users_json):
    for user in users_json:
        assert type(users_json[user]['first_name']) is str
        assert type(users_json[user]['last_name']) is str


def test_email_is_string(users_json):
    for user in users_json:
        assert type(users_json[user]['email']) is str


def test_roles_is_int_list(users_json):
    for user in users_json:
        for role in users_json[user]['roles']:
            assert type(role) is int


def test_created_format(users_json):
    correct_format = '%m-%d-%y %H:%M:%S %z'
    for user in users_json:
        assert datetime.datetime.strptime(users_json[user]['created'], correct_format)