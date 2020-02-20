""""
LogoutTest - Logout class
"""
import requests
from testwogs.testsdir.intertests import BaseTests
from testwogs import settings


class LogoutTest(BaseTests):
    def __init__(self):
        self.base_url = settings.BASE_URL_API
        self.request_url = 'logout/'

    def run_test(self):
        rec = requests.get(self.get_request_url(), headers={'Content-Type': 'application/json'})
        if rec.status_code == 200:
            print(f'LogoutTest completion status - {rec.status_code}')
        else:
            print(f'Something is wrong.\nLogoutTest completion status - {rec.status_code}')

    def get_request_url(self):
        return f"{self.base_url}{self.request_url}"
