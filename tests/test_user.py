# API testing with python
import numpy
import string
import random
import datetime
import requests
from tests.conftest import DATE_FORMAT, HEADER, URL, MAX_ID


def test_usersnames_are_strings(users_json):
    for user in users_json:
        assert type(users_json[user]['first_name']) is str
        assert type(users_json[user]['last_name']) is str


def test_usersemail_is_string(users_json):
    for user in users_json:
        assert type(users_json[user]['email']) is str


def test_usersroles_is_int_list(users_json):
    for user in users_json:
        for role in users_json[user]['roles']:
            assert type(role) is int


def test_userscreated_format(users_json):
    for user in users_json:
        assert datetime.datetime.strptime(users_json[user]['created'], DATE_FORMAT)


def test_usersgroupid_is_int_in_groups(users_json, group_json):
    existing_groups = [int(g) for g in group_json]
    for user in users_json:
        assert users_json[user]['group_id'] in existing_groups


def test_userscreatedby_is_int_in_existing_users(users_json):
    existing_users = [int(u) for u in users_json]
    for user in users_json:
        assert users_json[user]['created_by'] in existing_users


def test_userid_not_exist(users_json):
    existing_ids = [int(id) for id in users_json]
    # Generate valid id not present in API
    while True:
        invalid_id = numpy.random.randint(MAX_ID)
        if invalid_id not in existing_ids:
            break
    response = requests.get(URL + '/user/' + str(invalid_id), headers=HEADER)
    assert response.status_code == 404


def test_userid_invalid():
    # Generate a invalid id character
    invalid_id = random.choice(list(set(string.printable).difference(set(string.digits))))
    response = requests.get(URL + '/user/' + str(invalid_id), headers=HEADER)
    assert response.status_code == 400

    # TODO: Refactor following test into several fixtures that can be reused by other tests


def test_user_fields(users_json, group_json):
    existing_ids = [int(id) for id in users_json]
    # Choose random id from the existing ones
    testing_id = random.choice(existing_ids)
    json_response = requests.get(URL + '/user/' + str(testing_id), headers=HEADER).json()
    assert type(json_response['first_name']) is str
    assert type(json_response['last_name']) is str
    assert type(json_response['email']) is str
    for role in json_response['roles']:
        assert type(role) is int
    assert json_response['created'], DATE_FORMAT
    existing_groups = [int(g) for g in group_json]
    assert json_response['group_id'] in existing_groups
    assert json_response['created_by'] in existing_ids


