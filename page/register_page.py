'''
第四层 定位页面元素
获取各页面元素
被handle操作层调用
'''
from Imooc_selenium.base.find_element import FindElement

class RegisterPage():
    def __init__(self):
        self.fd = FindElement(driver)
    def get_email_element(self):
        return self.fd.get_element("user_email")