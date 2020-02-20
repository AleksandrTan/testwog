""""
BaseTests - base class (interface) for all application tests
"""

from abc import ABCMeta, abstractmethod


class BaseTests(metaclass=ABCMeta):

    @abstractmethod
    def run_test(self):
        pass