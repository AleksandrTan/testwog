""""
LoginTest - Login class
"""

from testwogs.testsdir.intertests import BaseTests


class LoginTest(BaseTests):
    def __init__(self):
        super().__init__()
        self.request_url = 'api-token-auth/'