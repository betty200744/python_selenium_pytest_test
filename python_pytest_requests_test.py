
import pytest
import unittest
import requests


def setup_module(module):
    print 'setup module=====>%s' %(module.__name__)

def teardown_module(module):
    print 'teardown module=====>%s' %(module.__name__)

def setup_function(function):
    print 'setup function =======>%s' %(function.__name__)

def teardown_function(function):
    print 'teardown function =====>%s' %(function.__name__)


def test_multiply_3_4():
    assert ((3 * 4), 12)

def test_add_3_4():
    assert ((3+4), 6)

class TestMultiply(unittest.TestCase):
    def test_multiply_3_4(self):
        self.assertEqual((3 * 4), 12)

class TestRequest():
    def setup_class(cls):
        print 'setup class=====>%s' %(cls.__name__)

    def teardown_class(cls):
        print 'teardown class=====>%s' %(cls.__name__)

    def setup_method(self,method):
        print 'setup method=====>%s' %(method.__name__)

    def teardown_method(self,method):
        print 'teardown method=====>%s' %(method.__name__)

    @pytest.mark.parametrize('url', (
        'http://www.baidu.com',
        'http://www.yhd.com',
        'http://www.taobao.com'
    ))
    def test_post_valid_url(self,url):
        r = requests.get(url)
        assert r.status_code ==  200

    @pytest.mark.xfail()  # py.test --runxfail  -s python_pytest_requests_test.py::TestRequest ,run even xfail
    def test_post_invalid_url(self):
        pass


@pytest.mark.v2extest
class TestV2EX():
    def test_v2ex_open_url(self):
        assert 1+1 ==2

    def test_v2ex_login(self):
        assert 1+1 ==2

    def test_action_favorite_it(self):
        assert 1+1 == 2













