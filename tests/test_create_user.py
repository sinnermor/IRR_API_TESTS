import requests
#
#
#
def test_auth_and_create_new_user(app):
    app.user.create_user()
    app.user.get_authorized()


def test_auth_old_user(app_auth):
    app_auth.user.get_authorized()


def test_get_profile(app_auth):
    g = requests.get(app_auth.url +'account', data={'auth_token': app_auth.user.get_auth_token()})
    data = g.json()
    assert g.status_code == 200
    assert data['error'] == None


def test_edit_user_info(app):
    app.user.create_user()
    app.user.get_authorized()
    app.user.edit_user_info()


def test_logout(app):
    app.user.create_user()
    app.user.get_authorized()
    app.user.get_user_logout()


def test_change_user(app):
    app.user.create_user()
    app.user.get_authorized()
    app.user.change_user_password()
#
# def test_restore_password(app):
#     app.user.create_user()
#     app.user.get_authorized()
#     app.user.get_restore_password
#

