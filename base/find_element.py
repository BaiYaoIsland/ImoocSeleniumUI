'''
第五层 获取元素方法
封装基本webdriver get元素的方法，被page层调用
通过配置文件常量参数定位
'''
from util.read_ini import ReadIni
from selenium import webdriver

class FindElement():
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None

if __name__ == '__main__':
    find_element = FindElement()
    driver = webdriver.Safari()
    fe = find_element.get_element('')
    print(fe)