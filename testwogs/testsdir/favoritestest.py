""""
FavoritesTest class
"""
import requests
import json
from testwogs.testsdir.intertests import BaseTests
from testwogs.testsdir.logintest import LoginTest
from testwogs import settings


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
                print(f'FavoritesTest completion status - {rec.status_code}')
            else:
                print(f'Something is wrong!!!\nFavoritesTest completion status - {rec.status_code}')
        else:
            print("Text message - Authentication credentials were not provided.")

    def get_request_url(self):
        return f"{self.base_url}{self.request_url}"

    def get_token_user(self):
        login_object = LoginTest()
        return login_object.run_test()
