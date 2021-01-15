import requests
import datetime
from tests.conftest import DATE_FORMAT, HEADER, URL, MAX_ID


def test_groupname_is_strings(group_json):
    for group in group_json:
        assert type(group_json[group]['name']) is str


def test_groupcreated_format(group_json):
    for group in group_json:
        assert datetime.datetime.strptime(group_json[group]['created'], DATE_FORMAT)


def test_groupcreatedby_is_int_in_existing_groups(group_json):
    existing_groups = [int(g) for g in group_json]
    for group in group_json:
        assert group_json[group]['created_by'] in existing_groups