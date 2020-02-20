""""
LoginTest - Login class
"""
import requests
import json
from testwogs.testsdir.intertests import BaseTests
from testwogs import settings


class LoginTest(BaseTests):
    def __init__(self):
        self.base_url = settings.BASE_URL_API
        self.request_url = 'api-token-auth/'
        self.username = settings.USER_NAME
        self.userpassword = settings.USER_PASSWORD

    def run_test(self):
        data_request = {'username': self.username, 'password': self.userpassword}
        data = json.dumps(data_request)
        rec = requests.post(self.get_request_url(), data, headers={'Content-Type': 'application/json'})
        if rec.status_code == 200:
            print(rec.json()['token'], rec.status_code)
        else:
            print(rec.json(), rec.status_code)

    def get_request_url(self):
        return f"{self.base_url}{self.request_url}"

    def get_token_user(self):
        data_request = {'username': self.username, 'password': self.userpassword}
        data = json.dumps(data_request)
        rec = requests.post(self.get_request_url(), data, headers={'Content-Type': 'application/json'})
        if rec.status_code == 200:
            return rec.json()['token']
        else:
            return 0