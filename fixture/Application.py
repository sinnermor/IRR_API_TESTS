import requests
import datetime
from source.Assertions import Base
from source.NewUser import User

class Application(object):

    def create_uniq_mail(self):
        now = datetime.datetime.now()
        now_date = str(now.day) + str(now.month)
        now_time = str(now.hour) + str(now.minute)
        suff = now_date + '' + now_time
        mail = 'test' + suff + '@pronto.ru'
        return mail

    def __init__(self, base_url):
        self.url = base_url
        self.mail = self.create_uniq_mail()
        self.password = '111111'
        self.user = User(self)

    def destroy(self):
        pass



# Fixture for actions with user
class ApplicationAuth(object):

    def __init__(self, base_url, mail, password):
        self.url = base_url
        self.mail = mail
        self.password = password
        self.user = User(self)


    def destroy(self):
        pass



advertisement_data = {'category': 'real-estate/apartments-sale/secondary/', 'region': 'russia/moskva-gorod/', 'advert_type' : 'realty_sell',
                      'advertisement[price]':'20000000','advertisement[text]': 'Объявление из фикстуры', 'advertisement[custom_fields][etage][0]':'7', 'advertisement[custom_fields][etage-all][0]': '11',
                      'advertisement[custom_fields][meters-total][0]': '220', 'advertisement[custom_fields][rooms][0]': '3'}


# Fixture for actions with advermissions
class ApplicationAdvert(ApplicationAuth):

    def __init__(self,base_url, mail, password):
        super(ApplicationAdvert, self).__init__(base_url, mail, password)
        self.auth_advert= self.get_advert()



    def get_advert(self):
        advertisement_data['auth_token'] = self.user.get_auth_token()
        p = requests.post(self.url + 'advertisements/advert', data= advertisement_data)
        data = p.json()
        adv_info = {'id': data['advertisement']['id'], 'auth_token': data['advertisement']['auth_token']}
        return adv_info

    def destroy(self):
        requests.delete(self.url + 'advertisements/advert/' + self.auth_advert['id'],
                        data={'auth_token': self.auth_advert['auth_token']})