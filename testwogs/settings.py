from testwogs.testsdir.logintest import LoginTest

"""
    Base URL API
"""
base_url_api = 'https://ng-dating-test.webmonstr.com/'

"""
    Tests dict
"""
tests_dict = {
    'logintest': {'class_name': LoginTest(), 'request_url': 'api-token-auth/'}
}