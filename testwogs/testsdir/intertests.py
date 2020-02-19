""""
BaseTests - base class (interface) for all application tests
"""

from abc import ABCMeta, abstractmethod
import requests
import json

from testwogs import settings


class BaseTests(metaclass=ABCMeta):
    def __init__(self):
        self.base_url = settings.base_url_api

    def run_test(self):
        payload = {'username': "admin", 'password': "admin"}
        data = json.dumps(payload)
        r = requests.post(self.get_request_url(), data, headers={'Content-Type': 'application/json'})
        print(r.text)

    def get_base_url(self):
        return self.base_url

    def get_request_url(self):
        return f"{self.base_url}{settings.tests_dict[self.__class__.__name__.lower()]['request_url']}"