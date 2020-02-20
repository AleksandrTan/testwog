""""
LoginTest - Login class
"""
import requests
import json
from testwogs.testsdir.intertests import BaseTests
from testwogs import settings
from testwogs.models import Logserver


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
        data_request = {'username': 1, 'password': self.userpassword}
        data = json.dumps(data_request)
        rec = requests.post(self.get_request_url(), data, headers={'Content-Type': 'application/json'})
        if rec.status_code == 200:
            # save data in DB
            self.save_data_test(rec.status_code, self.request_url)

            #information output to the console
            print('=' * 50)
            print(f'URL_REQUEST - {self.request_url}\nLogintest completion status - {rec.status_code} - Ok')
            print('=' * 50)
            return rec.json()['token']
        else:
            # save data in DB
            self.save_data_test(rec.status_code, self.request_url, test_status='no successfully', api_status=1)

            # information output to the console
            print('=' * 50)
            print(f'Something is wrong.\nURL_REQUEST - {self.request_url}\nTest completion status - {rec.status_code}')
            print('=' * 50)
            return False

    def get_request_url(self) -> str:
        return f"{self.base_url}{self.request_url}"

    def save_data_test(self, server_status, url_request, test_status='successfully', message='', api_status=0):
        data_record = Logserver.objects.save_new_record(server_status, url_request, test_status, message, api_status)
        return data_record