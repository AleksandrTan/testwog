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
        r = requests.post(self.get_request_url(), data, headers={'Content-Type': 'application/json'})
        print(r.text)

    def get_request_url(self):
        return f"{self.base_url}{self.request_url}"
