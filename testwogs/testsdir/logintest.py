""""
LoginTest - Login class
"""

from testwogs.testsdir.intertests import BaseTests
from testwogs import settings


class LoginTest(BaseTests):

    def get_request_url(self):
        return f"{self.base_url}{settings.tests_dict[self.__class__.__name__.lower()]['request_url']}"
