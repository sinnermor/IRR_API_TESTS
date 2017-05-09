import requests
import json
from jsonschema import validate
import pytest

category_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "required" : ["group_custom_fields"],
    "properties": {
        "group_custom_fields" : {
            "type": "array",
            "items" :  {
                "allOf": [
                    {
                        "type": "object",
                        "properties": {
                            "title": {"type" : "string"},
                            "custom_fields" : {
                                "type" : "array",
                                "items" : {
                                    "oneOf" : [
                                        {
                                            "type" : "object",
                                            "properties":{
                                                "title": {"type": "string"},
                                                "field_values": {"type": "array"},
                                                "mandatory": {"type": "boolean"}

                                            },
                                            "required": ["title", "field_values", "mandatory"]
                                        }
                                    ]

                                }
                            },
                        } ,
                        "required" : ["title", "custom_fields"]
                    }
                ]
            }
        }
    }
}

category_test_data = [
    ('realty_sell', 'real-estate/apartments-sale/secondary/', 'russia/moskva-gorod/'),
    ('auto_sprobegom', 'cars/passenger/used/', 'russia/moskva-gorod/'),
    ('auto_new', 'cars/passenger/new/', 'russia/moskva-gorod/'),
    ('realty_new', 'real-estate/apartments-sale/new/', 'russia/moskva-gorod/')
]

@pytest.mark.parametrize("advert_type,  category, region", category_test_data)
def test_get_category_url_schema_validation(advert_type, category, region):
    r = requests.get('http://irr.ru/mobile_api/1.2/' + 'categories/fields/post', data={'advert_type': advert_type, 'category': category, 'region': region})
    data = r.text
    jsonData = json.loads(data)
    print(data)
    assert (validate(jsonData, category_schema) == None), "Schema is incorrect"



@pytest.mark.parametrize("advert_type,  category, region", category_test_data)
def test_get_category_url_schema_validation(app, advert_type, category, region):
    r = requests.get(app.url + 'categories/fields/post', data={'advert_type': advert_type, 'category': category, 'region': region})
    data = r.text
    jsonData = json.loads(data)
    print(jsonData)


def test_get_listing(app):
    r = requests.get(app.url + 'advertisements/category', data={'category' : 'real-estate/apartments-sale/'})
    data = r.json()
    print(data)
    assert data['error'] == None, "Something went wront"

def test_list_filter_search(app):
    r = requests.get(app.url + 'categories/fields/search', data={'category': 'real-estate/apartments-sale/'})
    data = r.json()
    print(data)