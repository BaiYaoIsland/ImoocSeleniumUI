import unittest
import os
import HTMLtestrunner
class RunCase(unittest.TestCase):
    def test_case01(self):
        '''
        os.path.join(os.getcwd(),'case'
        os.getcwd()获取当前工程目录
        逗号后面是文件路径
        '''
        case_path = os.path.join(os.getcwd())
        suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()
