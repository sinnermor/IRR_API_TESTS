import requests
import pytest


def setup_module(module):
    # init_something()
    pass


def teardown_module(module):
    # teardown_something()
    pass

def get_data_json(uri, data):
    r = requests.post(uri, data)
    answer = r.json()
    return answer

#
# def test_creat_user():
#
#     p =requests.post('http://akordyukova.irr.ru.dev/mobile_api/1.2/account', data = {'email':'akordyukova021110@pronto.ru', 'password':'111111'})
#     data = p.json()
#     assert p.status_code == 200
#     assert (data['error'] == None)&(data['auth_token'] != '')



def test_authorization():
    login = 'akordyukova021107@pronto.ru'
    password = '111111'
    r = requests.post('http://irr.ru/mobile_api/1.2/account/login', data={'username': login, 'password':password})
    data = r.json()
    assert r.status_code == 200, 'Code is not 200, something went wrong'
    assert data['error']==None, "Error is not null! Something had happened - " + data['error']['description']
    # assert (data['user_info']['email']==login), 'Email is incorrect! Waited - ' + login + 'had - ' + data['user_info'['email']]


def get_auth_token(login, passwd):
    r = requests.post('http://irr.ru/mobile_api/1.2/account/login', data={'username': login, 'password':passwd})
    data = r.json()
    return data['auth_token']



def test_get_profile():
    token = get_auth_token('akordyukova021107@pronto.ru', '111111')
    print(token)
    g = requests.get('http://irr.ru/mobile_api/1.2/account', data={'auth_token':token})
    data = g.json()
    assert g.status_code == 200
    assert data['error'] == None
    print (data)


def test_edit_user_info():
    token = get_auth_token('akordyukova021107@pronto.ru', '111111')

    skype = 'sinner'
    phone = '89102315655'
    icq =  '666666'
    mobile = '89120005560'
    user_name = "Василиca"
    user_last_name = 'Ивановa'
    test_data_json = {'auth_token': token, 'user_info[phone]': phone, 'user_info[skype]':skype, 'user_info[icq]': icq, 'user_info[mobile]':mobile, 'user_info[first_name]': user_name,
                      'user_info[last_name]': user_last_name}
    p = requests.put('http://irr.ru/mobile_api/1.2/account', data=test_data_json)
    data = p.json()
    print(data)
    assert p.status_code==200
    assert (data['error'] != 0) & (data['user_info']['skype']== skype)


# def test_change_user():
#     token = get_auth_token('akordyukova021107@pronto.ru', '222222')
#     r = requests.post('http://irr.ru/mobile_api/1.2/account/changepassword', data={'auth_token':token, 'old_password':'222222', 'new_password':'111111'})
#     data = r.json()
#     print(data)
#     assert r.status_code == 200
#     assert data['error'] == None
# #
def test_logout():
    token = get_auth_token('akordyukova021107@pronto.ru', '111111')
    p = requests.post('http://irr.ru/mobile_api/1.2/account/logout', data={'auth_token':token})
    data = p.json()
    print(data)
    assert p.status_code == 200
    assert data['error'] == None