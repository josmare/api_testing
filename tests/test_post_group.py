import datetime
import random
import numpy

from tests.conftest import post_request, valid_group_post, invalid_group_name, MAX_ID, \
    DATE_FORMAT


def test_post_valid_group():
    p_response = post_request('/group', valid_group_post)
    response_json = p_response.json()
    assert p_response.status_code == 200
    assert response_json['name'] == 'Test Co.'
    assert type(response_json['parent_id']) is int
    assert datetime.datetime.strptime(response_json['created'], DATE_FORMAT)



def test_post_invalid_group_name():
    p_response = post_request('/group', invalid_group_name)
    assert p_response.status_code == 400


def test_post_invalid_group_parendid(group_json):
    existing_groups_ids = [int(g) for g in group_json]
    while True:
        invalid_group_id = numpy.random.randint(MAX_ID)
        if invalid_group_id not in existing_groups_ids:
            break
    valid_group_post['parent_id'] = invalid_group_id
    p_response = post_request('/user', valid_group_post)
    assert p_response.status_code == 400

