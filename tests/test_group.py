import numpy
import string
import random
import datetime
import requests
from tests.conftest import DATE_FORMAT, HEADER, URL, MAX_ID


def test_groupname_is_strings(group_json):
    for group in group_json:
        assert type(group_json[group]['name']) is str


def test_groupcreated_format(group_json):
    for group in group_json:
        assert datetime.datetime.strptime(group_json[group]['created'], DATE_FORMAT)


def test_groupcreatedby_is_int_in_existing_groups(group_json):
    existing_groups_ids = [int(g) for g in group_json]
    for group in group_json:
        assert group_json[group]['created_by'] in existing_groups_ids


def test_groupparenid_is_valid(group_json):
    existing_groups_ids = [int(g) for g in group_json]
    for group in group_json:
        if group_json[group]['parent_id'] is not None:
            assert group_json[group]['parent_id'] in existing_groups_ids
        else:
            assert group_json[group]['name'] == 'Root Group'


def test_groupid_not_exist(group_json):
    existing_groups_ids = [int(g) for g in group_json]
    # Generate a valid id group not present in API
    while True:
        invalid_group_id = numpy.random.randint(MAX_ID)
        if invalid_group_id not in existing_groups_ids:
            break
    response = requests.get(URL + '/group/' + str(invalid_group_id), headers=HEADER)
    assert response.status_code == 404


def test_groupid_is_invalid(group_json):
    # Generate a invalid id character
    invalid_id = random.choice(list(set(string.printable).difference(set(string.digits))))
    response = requests.get(URL + '/group/' + str(invalid_id), headers=HEADER)
    assert response.status_code == 400


def test_group_fields(group_json):
    existing_group_ids = [int(g_id) for g_id in group_json]
    # Choose random id from the existing ones
    testing_id = random.choice(existing_group_ids)
    json_response = requests.get(URL + '/group/' + str(testing_id), headers=HEADER).json()
    assert type(json_response['name']) is str
    assert datetime.datetime.strptime(json_response['created'], DATE_FORMAT)
    assert json_response['created_by'] in existing_group_ids
    if json_response['parent_id'] is not None:
        assert json_response['parent_id'] in existing_group_ids
    else:
        assert json_response['name'] == 'Root Group'