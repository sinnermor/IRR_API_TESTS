import requests
from source.Assertions import Base

class User(Base):

    def __init__(self, app):
        super(User, self).__init__(app)
        self.email = app.mail
        self.password = app.password

    def create_user(self):
        p =requests.post(self.url + 'account', data={'email': self.email, 'password': self.password})
        data = p.json()
        assert p.status_code == 200
        if data['error'] != None:
            assert (data['error']['code'] == 30), "There is some shit here"
        else : self.assert_token_is_not_null(data)

    def check_user_create(self):
        pass

    def get_authorized(self):
        r = requests.post(self.url + 'account/login',
                          data={'username': self.email, 'password': self.password})
        data = r.json()
        assert r.status_code == 200, 'Code is not 200, something went wrong'
        self.assert_error_is_None(data)
        assert ( data['user_info']['email'] == self.email), 'Email is incorrect! Waited - ' + self.email + 'had - ' + \
                                                       data['user_info'['email']]

    def get_auth_token(self):
        r = requests.post(self.url + 'account/login', data={'username': self.email, 'password': self.password})
        data = r.json()
        return data['auth_token']

    def edit_user_info(self):
        skype = 'sinner'
        phone = '89102315655'
        icq =  '666666'
        mobile = '89120005560'
        user_name = "Василиca"
        user_last_name = 'Ивановa'
        test_data_json = {'auth_token': self.get_auth_token(), 'user_info[phone]': phone, 'user_info[skype]':skype, 'user_info[icq]': icq, 'user_info[mobile]':mobile, 'user_info[first_name]': user_name,
                          'user_info[last_name]': user_last_name}
        p = requests.put(self.url +'account', data=test_data_json)
        data = p.json()
        assert p.status_code==200
        assert (data['error'] != 0) & (data['user_info']['skype']== skype)

    def get_user_logout(self):
        p = requests.post(self.url + 'account/logout', data={'auth_token': self.get_auth_token()})
        data = p.json()
        print(data)
        assert p.status_code == 200
        assert data['error'] == None


    def change_user_password(self):
        new_pass = '111111'
        r = requests.post(self.url + 'account/changepassword',
                          data={'auth_token': self.get_auth_token(), 'old_password': self.password, 'new_password': new_pass})
        data = r.json()
        assert r.status_code == 200
        assert data['error'] == None




