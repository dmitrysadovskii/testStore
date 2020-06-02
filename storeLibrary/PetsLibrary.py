import requests
import json
from helpers.ApiHelper import ApiHelper
from helpers.JsonHelper import JsonHelper
# from config2.enviroment import pets_data, endpoints


class PetsLibrary:

    def __init__(self, url, data):
        self.url = url
        self.data = data

    def add_pets_to_store(self, name):
        upd_json = JsonHelper().update_json(json_data=self.data, name=name)
        resp = ApiHelper().send_request('post', self.url, upd_json)
        return resp['id']

    def add_pets_to_store_with_invalid_id(self):
        upd_json = JsonHelper().update_json(json_data=self.data, id='id')
        ApiHelper().send_request('post', self.url, upd_json, status_code=500)

    def update_pets_name_by_id(self, pets_id, name, status):
        upd_json = JsonHelper().update_json(json_data=self.data, id=pets_id, name=name, status=status)
        resp = ApiHelper().send_request('put', self.url, data=upd_json)
        assert resp['name'] == name, f'Name should be {name}'
        assert resp['id'] == pets_id, f"{resp['id']} != {pets_id}"

    def update_pets_name_with_invalid_data(self, pets_id, name, status_code):
        upd_json = JsonHelper().update_json(json_data=self.data, id=pets_id, name=name)
        ApiHelper().send_request('put', self.url, data=upd_json, status_code=status_code)

    def find_pets_by_status(self, id, name, status: str):
        new_url = self.url + f"/findByStatus?status={status}"
        resp = ApiHelper().send_request('get', new_url)
        assert resp[0]['id'] == int(id), f"{resp[0]['id']} != {int(id)}"
        assert resp[0]['name'] == name

    def find_pets_by_id(self, id, name):
        new_url = self.url + f"/{id}"
        resp = ApiHelper().send_request('get', new_url)
        assert resp['id'] == int(id), f"{resp['id']} != {int(id)}"
        assert resp['name'] == name

    def find_pets_by_invalid_id(self, id, status_code):
        new_url = self.url + f"/{id}"
        ApiHelper().send_request('get', new_url, status_code=status_code)

    def delete_pets_by_id(self, id):
        new_url = self.url + f"/{id}"
        ApiHelper().send_request('delete', new_url)
        self.find_pets_by_invalid_id(id=id, status_code=404)

    def delete_pets_by_invalid_id(self, id):
        new_url = self.url + f"/{id}"
        ApiHelper().send_request('delete', new_url, status_code=404)

