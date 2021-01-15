import datetime
import numpy
from tests.conftest import DATE_FORMAT, MAX_ID, post_request,\
    valid_user_post, invalid_user_firstname, invalid_user_lastname,\
    invalid_user_email, invalid_user_roles


def test_post_valid_user():
    p_response = post_request('/user', valid_user_post)
    response_json = p_response.json()
    assert p_response.status_code == 200
    assert response_json['first_name'] == 'Testi'
    assert response_json['last_name'] == 'Testinen'
    assert response_json['email'] == 'testi.testinen@example.com'
    assert response_json['roles'] == [0]
    assert response_json['group_id'] == 1
    assert datetime.datetime.strptime(response_json['created'], DATE_FORMAT)


def test_post_invalid_user_firstname():
    p_response = post_request('/user', invalid_user_firstname)
    assert p_response.status_code == 400


def test_post_invalid_user_lastname():
    p_response = post_request('/user', invalid_user_lastname)
    assert p_response.status_code == 400


def test_post_invalid_user_email():
    p_response = post_request('/user', invalid_user_email)
    assert p_response.status_code == 400


def test_post_invalid_user_roles():
    p_response = post_request('/user', invalid_user_roles)
    assert p_response.status_code == 400


def test_post_invalid_user_groupid(group_json):
    existing_groups_ids = [int(g) for g in group_json]
    while True:
        invalid_group_id = numpy.random.randint(MAX_ID)
        if invalid_group_id not in existing_groups_ids:
            break
    valid_user_post['group_id'] = invalid_group_id
    p_response = post_request('/user', valid_user_post)
    assert p_response.status_code == 400

