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
    """
        Runs the test, returns the token on success
    """
    def run_test(self):
        data_request = {'username': self.username, 'password': self.userpassword}
        data = json.dumps(data_request)
        rec = requests.post(self.get_request_url(), data, headers={'Content-Type': 'application/json'})
        if rec.status_code == 200:
            print(f'Test completion status - {rec.status_code}')
            return rec.json()['token']
        else:
            print(f'Something is wrong.\nTest completion status - {rec.status_code}')
            return False

    def get_request_url(self) -> str:
        return f"{self.base_url}{self.request_url}"