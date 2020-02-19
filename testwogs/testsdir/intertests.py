""""
BaseTests - base class (interface) for all application tests
"""

from abc import ABCMeta, abstractmethod
import request

from testwogs import settings


class BaseTests(metaclass=ABCMeta):
    def __init__(self):
        self.base_url = settings.base_url_api

    def get_baseurl(self):
        return self.base_url

    @abstractmethod
    def make_request(self):
        pass
