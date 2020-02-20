""""
BaseTests - base class (interface) for all application tests
"""

from abc import ABCMeta, abstractmethod


class BaseTests(metaclass=ABCMeta):

    @abstractmethod
    def run_test(self):
        pass

    @abstractmethod
    def get_request_url(self) -> str:
        pass
    """
        Save data in DB
    """
    @abstractmethod
    def save_data_test(self, server_status, url_request, test_status='successfully',
                       message='No Message', api_status=0):
        pass