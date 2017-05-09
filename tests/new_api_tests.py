import requests
import pytest
import json

def test_gn_mobile_api(app):
    g = requests.get(app.url + 'advertisements/guided_navigation', data ={'category' :'cars/passenger/'})
    data = g.json()
    print(data)
    assert g.status_code == 200
    assert data['error'] == None, data



def test_suggests_mobile_api(app):
    g = requests.get(app.url + 'advertisements/suggest', data ={'keywords' :'Audi'})
    data = g.json()
    print(data)
    assert g.status_code == 200
    assert data['error'] == None, data
    suggests_array = data['suggest']
    print(suggests_array)