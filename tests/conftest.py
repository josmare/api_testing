import os
import pytest
import random
import string
import numpy
import requests

HEADER = {'x-api-key': os.getenv('API_KEY')}
URL = 'https://l9njuzrhf3.execute-api.eu-west-1.amazonaws.com/prod'
MAX_ID = 999
DATE_FORMAT = '%m-%d-%y %H:%M:%S %z'
MIN_LENGTH = 2
MAX_LENGTH = 50


# ######  Pytest fixtures  ######

@pytest.fixture
def users_json():
    return requests.get(url=URL + '/user', headers=HEADER).json()


@pytest.fixture()
def group_json():
    return requests.get(url=URL + '/group', headers=HEADER).json()


@pytest.fixture()
def random_names():
    name1_length = numpy.random.randint(MIN_LENGTH, MAX_LENGTH)
    name2_length = numpy.random.randint(MIN_LENGTH, MAX_LENGTH)
    letters = string.ascii_letters + string.digits
    rand_name1 = ''.join(random.choice(letters) for i in range(name1_length))
    rand_name2 = ''.join(random.choice(letters) for i in range(name2_length))
    return [rand_name1, rand_name2]


#  #####   Other resources  ######

def post_request(r_url, json):
    return requests.post(url=URL + r_url, headers=HEADER, json=json)


def random_invalid_name():
    """Generates a random string out of boundaries 2-50 characters"""
    name_length = numpy.random.randint(MAX_LENGTH, 599)
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(name_length))


def random_invalid_list():
    "Generates a random list of int of random size between 0-4"""
    randomlist = []
    random_size = numpy.random.randint(0, 99)
    for i in range(0, random_size):
        n = random.randint(5, 99)
    randomlist.append(n)
    return randomlist


valid_user_post = {
    'first_name': 'Testi',
    'last_name': 'Testinen',
    'email': 'testi.testinen@example.com',
    'roles': [0],
    'group_id': 1
}

invalid_user_firstname = {
    'first_name': random_invalid_name(),
    'last_name': 'Testinen',
    'email': 'testi.testinen@example.com',
    'roles': [0],
    'group_id': 1
}

invalid_user_lastname = {
    'first_name': 'Testi',
    'last_name': random_invalid_name(),
    'email': 'testi.testinen@example.com',
    'roles': [0],
    'group_id': 1
}

invalid_user_email = {
    'first_name': 'Testi',
    'last_name': 'Testinen',
    'email': random_invalid_name(),
    'roles': [0],
    'group_id': 1
}


invalid_user_roles = {
    'first_name': 'Testi',
    'last_name': 'Testinen',
    'email': 'testi.testinen@example.com',
    'roles': random_invalid_list(),
    'group_id': 1
}