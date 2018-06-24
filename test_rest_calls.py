import pytest
import json
import unittest
import requests
from rest.keysandurls import *


class TestRestCalls(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("***Test for calls started <SUITE LEVEL>***")

    @classmethod
    def tearDownClass(cls):
        print("***Test for calls ended <SUITE LEVEL>***")

    def setUp(self):
        print("This is case level set-up")

    def tearDown(self):
        print("This is case level tear-down")

    @pytest.mark.run(order=1)
    @pytest.mark.dependency()
    def test_get(self):

        global base_url
        get_user_list_ep = "/api/users"
        param = {'page': 2}

        get_user_list_rsp = requests.get(base_url + get_user_list_ep, params=param)

        with open('get_user_list_rsp.json') as infile:
            get_user_list_json = json.load(infile)

        self.assertEqual(get_user_list_rsp.status_code, 200)
        self.assertEqual(get_user_list_rsp.json(), get_user_list_json)

        print("This is test to get the user list.")

    @pytest.mark.second
    @pytest.mark.dependency()
    def test_post(self):
        global base_url, post_endpoint

        post_payload = {"name": "morpheus", "job": "leader"}

        post_resp_verify = {"name": "morpheus", "job": "leader", "id": "752", "createdAt": "2018-05-08T07:24:42.502Z"}

        get_post_resp = requests.post(base_url + post_endpoint, data=post_payload)

        # print
        # (get_post_resp.json()['name'], get_post_resp.json()['job'])

        self.assertEqual(get_post_resp.status_code, 201)
        self.assertEqual(get_post_resp.json()['name'], post_resp_verify['name'])
        self.assertEqual(get_post_resp.json()['job'], post_resp_verify['job'])

        print("This is the test to add new user.")

    @pytest.mark.dependency(depends=['TestRestCalls::test_get','TestRestCalls::test_post'])
    def test_put(self):
        global base_url, put_endpoint

        put_payload = {"name": "morpheus", "job": "zion resident"}
        put_resp_verify = {"name": "morpheus","job": "zion resident","updatedAt": "2018-05-08T07:32:26.482Z"}

        get_put_resp = requests.put(base_url + put_endpoint, data=put_payload)

        self.assertEqual(get_put_resp.status_code, 200)
        self.assertEqual(get_put_resp.json()['name'], put_resp_verify['name'])
        self.assertEqual(get_put_resp.json()['job'], put_resp_verify['job'])

        print("This is the test to update user.")

    @pytest.mark.last
    @pytest.mark.dependency()
    def test_del(self):

        global base_url, put_endpoint
        get_del_resp = requests.delete(base_url + put_endpoint)
        self.assertEqual(get_del_resp.status_code, 204)
        print("This is the test to delete any user.")