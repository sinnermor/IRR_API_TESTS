import requests
import pytest
import json
import jsonschema
from jsonschema import validate
# import validictory


#
# mandatory_fields_real_estate = {'rooms', 'meters-total', 'etage', 'price'}
#
# mandatory_fields_cars = {'make', 'model', 'car-year', 'bodytype', 'mileage', 'transmittion', 'price'}
#
# mandatory_fields_cars_new = {'make', 'model', 'car-year', 'bodytype', 'transmittion', 'price'}
#
# mandatory_fields_test_data = [
#     ('realty_sell', 'real-estate/apartments-sale/secondary/', 'russia/moskva-gorod/',mandatory_fields_real_estate),
#     ('auto_sprobegom', 'cars/passenger/used/', 'russia/moskva-gorod/', mandatory_fields_cars),
#     ('auto_new', 'cars/passenger/new/', 'russia/moskva-gorod/', mandatory_fields_cars_new),
#     ('realty_new', 'real-estate/apartments-sale/new/', 'russia/moskva-gorod/',mandatory_fields_real_estate)
# ]
#
#
# @pytest.mark.parametrize("advert_type,  category, region, mandatory_fields", mandatory_fields_test_data)
# def test_get_category_rel_estate(app, advert_type,  category, region, mandatory_fields):
#     r = requests.get(app.url + 'categories/fields/post', data={'advert_type' : advert_type, 'category': category, 'region': region })
#     data = r.json()
#     print(data)
#     assert r.status_code == 200
#     assert data['error'] == None
#     main_characteristics = data['group_custom_fields']
#     print (main_characteristics)
#     mandatory_list = []
#     for el in main_characteristics:
#         custom_1 = el['custom_fields']
#         for custom in custom_1:
#             if custom['mandatory'] == True:
#                 mandatory_list.append(custom['name'])
#                 print (mandatory_list)
#
#     result = set(mandatory_fields)^set(mandatory_list)
#     assert (result == set()), "Something went wrong"
#
#
# category_schema = {
#     "$schema": "http://json-schema.org/draft-04/schema#",
#     "type": "object",
#     "required" : ["group_custom_fields"],
#     "properties": {
#         "group_custom_fields" : {
#             "type": "array",
#             "items" :  {
#                 "allOf": [
#                     {
#                         "type": "object",
#                         "properties": {
#                             "title": {"type" : "string"},
#                             "custom_fields" : {
#                                 "type" : "array",
#                                 "items" : {
#                                     "oneOf" : [
#                                         {
#                                             "type" : "object",
#                                             "properties":{
#                                                 "title": {"type": "string"},
#                                                 "field_values": {"type": "array"},
#                                                 "mandatory": {"type": "boolean"}
#
#                                             },
#                                             "required": ["title", "field_values", "mandatory"]
#                                         }
#                                     ]
#
#                                 }
#                             },
#                         } ,
#                         "required" : ["title", "custom_fields"]
#                     }
#                 ]
#             }
#         }
#     }
# }
#
# category_test_data = [
#     ('realty_sell', 'real-estate/apartments-sale/secondary/', 'russia/moskva-gorod/'),
#     ('auto_sprobegom', 'cars/passenger/used/', 'russia/moskva-gorod/'),
#     ('auto_new', 'cars/passenger/new/', 'russia/moskva-gorod/'),
#     ('realty_new', 'real-estate/apartments-sale/new/', 'russia/moskva-gorod/')
# ]
#
#
# @pytest.mark.parametrize("advert_type,  category, region", category_test_data)
# def test_get_category_url_schema_validation(app, advert_type, category, region):
#     r = requests.get(app.url + 'categories/fields/post',
#                      data={'advert_type': advert_type, 'category': category, 'region': region})
#     data = r.text
#     jsonData = json.loads(data)
#     assert r.status_code == 200
#     assert (validate(jsonData, category_schema) == None), "Schema is incorrect"
#
#
#
#
# advertisement_data_1 = {'category': 'real-estate/apartments-sale/secondary/', 'region': 'russia/moskva-region/moskva-gorod/', 'advert_type' : 'realty_sell',
#                       'advertisement[price]':'200333','advertisement[text]': 'Объявление из фикстуры', 'advertisement[custom_fields][etage][0]':'7', 'advertisement[custom_fields][etage-all][0]': '11',
#                       'advertisement[custom_fields][meters-total][0]': '220', 'advertisement[custom_fields][rooms][0]': '3'}
#
# def test_create_advermission(app_auth):
#     # app_auth.user.create_user()
#     app_auth.user.get_authorized()
#     advertisement_data_1['auth_token'] = app_auth.user.get_auth_token()
#     # test_data_advermission_real_estate[advertisement] = advertisement_data
#     p = requests.post(app_auth.url + 'advertisements/advert', data= advertisement_data_1)
#     data = p.json()
#     print(data)
#     assert p.status_code == 200
#     assert data['advertisement']['email'] == app_auth.mail, data
#


def test_advermission_actions(app_advert):
    g = requests.get(app_advert.url + 'advertisements/advert/' + app_advert.auth_advert['id'] + '/actions', data={'auth_token': app_advert.auth_advert['auth_token']})
    data = g.json()
    assert g.status_code == 200
    assert data['error'] == None, data


# def test_advermission_edit(app_auth):
#     pass


def test_advermission_get_by_id(app_advert):
    g = requests.get(app_advert.url + 'advertisements/advert/'+app_advert.auth_advert['id'], data={'auth_token': app_advert.auth_advert['auth_token']})
    data = g.json()
    print(data)
    assert g.status_code == 200
    assert data['error'] == None, data


# def test_advermission_add_to_favorites(app_advert):
    p = requests.post(app_advert.url + 'advertisements/advert/' + app_advert.auth_advert['id'] + '/favorite',
                     data={'auth_token': app_advert.auth_advert['auth_token']})
    data = p.json()
    print(data)
    assert p.status_code == 200
    assert data['error'] == None
#
def test_advermission_remove_from_favorites(app_advert):
    p = requests.delete(app_advert.url + 'advertisements/advert/' + app_advert.auth_advert['id'] + '/favorite', data={'auth_token': app_advert.auth_advert['auth_token']})
    data = p.json()
    print(data)
    assert p.status_code == 200
    assert data['error'] == None

def test_advermission_send_complaint(app_advert):
    p = requests.post(app_advert.url + 'advertisements/advert/' + app_advert.auth_advert['id'] + '/complain',
                        data={'author_email': 'test@pronto.ru', 'comment':'Тестирование мобильного API', 'reason':'Неверный регион, рубрика'})
    data = p.json()
    print(data)
    assert p.status_code == 200
    assert data['error'] == None, data

def test_advermission_view_history(app_advert):
    g = requests.get(app_advert.url + 'advertisements/advert/' + app_advert.auth_advert['id'] + '/view_history')
    data = g.json()
    print(data)
    assert g.status_code == 200
    assert data['error'] == None, data

def test_advermission_similar(app_advert):
    g = requests.get(app_advert.url + 'advertisements/advert/' + app_advert.auth_advert['id'] + '/similar')
    data = g.json()
    print(data)
    assert g.status_code == 200
    assert data['error'] == None, data


def test_advermission_deactivate(app_advert):
    p = requests.post(app_advert.url + 'advertisements/advert/' + app_advert.auth_advert['id'] + '/deactivate', data={'auth_token': app_advert.auth_advert['auth_token']})
    data = p.json()
    assert p.status_code == 200
    assert data['error'] == None, data


def test_advermission_delete(app_advert):
    d = requests.delete(app_advert.url + 'advertisements/advert/' + app_advert.auth_advert['id'], data={'auth_token': app_advert.auth_advert['auth_token']})
    data = d.json()
    assert d.status_code == 200
    assert data['error'] == None, data




