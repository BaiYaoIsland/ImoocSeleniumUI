from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
import HTMLTestRunner
import unittest
import os
import time
from log.user_log import UserLog
'''
第一层 测试用例
'''
log = UserLog().get_log()
class FirstCase(unittest.TestCase):
    def test_login_email_error(self):
        login('5zhishi20xb@sina.com','JHzhang','111111','zxfc3')
        # 通过assert判断是否为error

    def test_login_username_error(self):
        login('23','111')
        log.debug("this is Safer")


    def test_login_code_error(self):
        login('23','111')

    def test_login_success(self):
        login('23','111')