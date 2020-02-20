""""
LogoutTest - Logout class
"""
import requests
from testwogs.testsdir.intertests import BaseTests
from testwogs import settings
from testwogs.models import Logserver


class LogoutTest(BaseTests):
    def __init__(self):
        self.base_url = settings.BASE_URL_API
        self.request_url = 'logout/'

    def run_test(self):
        rec = requests.get(self.get_request_url(), headers={'Content-Type': 'application/json'})
        if rec.status_code == 200:
            # save data in DB
            data_json = rec.json()
            self.save_data_test(rec.status_code, self.request_url, message=data_json['message'],
                                api_status=data_json['status'])

            # information output to the console
            print('=' * 50)
            print(f'URL_REQUEST - {self.request_url}\nLogoutTest completion status - {rec.status_code} - Ok')
            print('=' * 50)
        else:
            # save data in DB
            self.save_data_test(rec.status_code, self.request_url, test_status='no successfully', api_status=1)

            # information output to the console
            print('=' * 50)
            print(f'Something is wrong.\nURL_REQUEST - {self.request_url}\n'
                  f'LogoutTest completion status - {rec.status_code}')
            print('=' * 50)

    def get_request_url(self):
        return f"{self.base_url}{self.request_url}"

    def save_data_test(self, server_status, url_request, test_status='successfully', message='', api_status=0):
        data_record = Logserver.objects.save_new_record(server_status, url_request, test_status, message, api_status)
        return data_record