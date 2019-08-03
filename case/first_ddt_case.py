#邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
import ddt
import unittest
from selenium import webdriver
from Imooc_selenium.business.register_business import RegisterBusiness
import time
import HTMLTestRunner
import os

class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Safari()
        self.driver.get('http://www.5itest.cn/register')
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name)
                self.driver.save_screenshot(file_path)
        self.driver.close()
    '''
    @ddt.data(
        ['email','username','password','code','user_email_error','请输入有效的电子邮件地址']
    )
    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_case(self,email,username,password,code,assertCode,assertText):
        email_error = self.login.register_function('1314@qq.com','user1111@qq.com','111111',self.file_name)
        return self.assertFalse(email_error,"测试失败")

if __name__ == '__main__':
    unittest.main()
    file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first report")
    runner.run(suite)