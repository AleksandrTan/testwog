from testwogs.testsdir.logintest import LoginTest
from testwogs.testsdir.logouttest import LogoutTest

"""
    Base URL API
"""
BASE_URL_API = 'https://ng-dating-test.webmonstr.com/'

"""
    User Defaults Settings
"""
USER_NAME = 'admin'
USER_PASSWORD = 'admin'
USER_EMAIL = 'admin@do.com'

"""
    Tests dict
"""
TESTS_DICT = {
    'logintest': {'class_name': LoginTest(), 'request_url': 'api-token-auth/', 'method': 'post'},
    'logouttest': {'class_name': LogoutTest(), 'request_url': 'logout/', 'method': 'get'}
}
