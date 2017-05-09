import pytest
import json
import os.path
import sys
from fixture.Application import Application
from fixture.Application import ApplicationAuth
from fixture.Application import ApplicationAdvert


PREFICS_URL = 'mobile_api/1.2/'



@pytest.fixture(scope='function')
def app(request):
    global fixture
    global fixtureAuth
    url_param = request.config.getoption("--url")
    if url_param != '':
        with open(request.config.getoption("--target"), 'r') as config_file:
            target = json.load(config_file)
        if url_param == target['baseUrl']:
            fixture = Application(base_url=target['baseUrl'])
            fixtureAuth = ApplicationAuth(base_url = url_param + PREFICS_URL, mail=target['email'], password=target['password'])
        else:  fixture = Application(base_url=url_param + "mobile_api/1.2/")
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture(scope='function')
def app_auth(request):
    global fixture
    url_param = request.config.getoption("--url")
    with open(request.config.getoption("--target"), 'r') as config_file:
        target = json.load(config_file)
    if url_param == target['baseUrl']:
            fixture = ApplicationAuth(base_url=target['baseUrl'], mail=target['email'], password=target['password'])
    else: fixture = ApplicationAuth(base_url = url_param + PREFICS_URL, mail=target['email'], password=target['password'])
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture
def app_advert(request):
    global fixture
    url_param = request.config.getoption("--url")
    with open(request.config.getoption("--target"), 'r') as config_file:
        target = json.load(config_file)
    if url_param == target['baseUrl']:
            fixture = ApplicationAdvert(base_url=target['baseUrl'], mail=target['email'], password=target['password'])
    else: fixture = ApplicationAdvert(base_url = url_param + PREFICS_URL, mail=target['email'], password=target['password'])
    # fixture.ensure_login("email"=)
    request.addfinalizer(fixture.destroy)
    return fixture



def pytest_addoption(parser):
    parser.addoption("--target", action="store", default='target.json')
    parser.addoption("--url", action="store", default='http://akordyukova.irr.ru.dev/')




