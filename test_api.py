# API testing with python
import requests
import os


HEADER = {'x-api-key': os.getenv('API_KEY')}
URL = 'https://l9njuzrhf3.execute-api.eu-west-1.amazonaws.com/prod/user'


def test_code_response():
    response = requests.get(url=URL, headers=HEADER)
    assert response.status_code == 200
