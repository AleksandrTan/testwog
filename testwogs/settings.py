from testwogs.testsdir.logintest import LoginTest
from testwogs.testsdir.logouttest import LogoutTest
from testwogs.testsdir.favoritestest import FavoritesTest

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
    'logouttest': {'class_name': LogoutTest(), 'request_url': 'logout/', 'method': 'get'},
    'favoritestest': {'class_name': FavoritesTest(), 'request_url': 'account/favorites', 'method': 'get'}
}

token = "0807261049ea7033a702e13ae47ff262da91addc",
