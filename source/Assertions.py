import pytest

class Base(object):

    def __init__(self, app):
        self.app = app
        self.url = app.url

    def assert_error_is_None(self, json):
        assert (json['error'] == None), "Error is not null! Something had happened - " + json['error']['description']

    def assert_token_is_not_null(self, json):
        assert (json['auth_token'] != '')
