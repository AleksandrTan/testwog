""""
FavoritesTest class
"""
import requests
import json
from testwogs.testsdir.intertests import BaseTests
from testwogs.testsdir.logintest import LoginTest
from testwogs import settings
from testwogs.models import Logserver


class FavoritesTest(BaseTests):
    def __init__(self):
        self.base_url = settings.BASE_URL_API
        self.request_url = 'account/favorites'
        self.limit = 5
        self.offset = 2

    def run_test(self):
        data_request = {'limit': self.limit, 'offset': self.offset}
        data = json.dumps(data_request)
        token = self.get_token_user()
        if token:
            rec = requests.get(self.get_request_url(), data, headers={'Content-Type': 'application/json',
                                                                      'Authorization': 'Token ' + token})
            if rec.status_code == 200:
                # save data in DB
                self.save_data_test(rec.status_code, self.request_url)

                # information output to the console
                print('=' * 50)
                print(f'URL_REQUEST - {self.request_url}\nFavoritesTest completion status - {rec.status_code} - Ok')
                print('=' * 50)
            else:
                # save data in DB
                self.save_data_test(rec.status_code, self.request_url, test_status='no successfully', api_status=1)

                # information output to the console
                print('=' * 50)
                print(f'URL_REQUEST - {self.request_url}\n'
                      f'Something is wrong!!!\nFavoritesTest completion status - {rec.status_code}')
                print('=' * 50)
        else:
            print("Text message - Authentication credentials were not provided.")

    def get_request_url(self):
        return f"{self.base_url}{self.request_url}"

    def get_token_user(self):
        login_object = LoginTest()
        return login_object.run_test()

    def save_data_test(self, server_status, url_request, test_status='successfully', message='', api_status=0):
        data_record = Logserver.objects.save_new_record(server_status, url_request, test_status, message, api_status)
        return data_record
