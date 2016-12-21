import pytest
import json
import os.path
import sys
from fixture.Application import Application
from fixture.Application import ApplicationAuth
from fixture.Application import ApplicationAdvert

@pytest.fixture
def app(request):
    global fixture
    with open(request.config.getoption("--target"), 'r') as config_file:
        target = json.load(config_file)
    fixture = Application(base_url=target['baseUrl'])

    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture
def app_auth(request):
    global fixture
    with open(request.config.getoption("--target"), 'r') as config_file:
        target = json.load(config_file)
    fixture = ApplicationAuth(base_url=target['baseUrl'], mail=target['email'], password=target['password'])
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture
def app_advert(request):
    global fixture
    with open(request.config.getoption("--target"), 'r') as config_file:
        target = json.load(config_file)
    fixture = ApplicationAdvert(base_url=target['baseUrl'], mail=target['email'], password=target['password'])
    # fixture.ensure_login("email"=)
    request.addfinalizer(fixture.destroy)
    return fixture



def pytest_addoption(parser):
    parser.addoption("--target", action="store", default='target.json')




