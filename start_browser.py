from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.common.by import By
import random
from PIL import Image

driver = webdriver.Safari()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
print(EC.title_contains("注册"))

# element = driver.find_element_by_class_name("controls")
locator = (By.CLASS_NAME,"controls")
element_located = EC.visibility_of_element_located(locator)
wd(driver,1).until(element_located)

# 获取验证码坐标将其截取、保存下来另作识别
driver.save_screenshot("./screenshot/imooc.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
im = Image.open("./screenshot/imooc.png")
img = im.crop((left,top,right,height))
img.save("./screenshot/imooc1.png")


email_element = driver.find_element_by_id("register_email")
# user_email = random.sample('1234567890',5)
# 随机生成用户名，random.sample（组成元素，位数）
for i in range(5):
    user_email = ''.join(random.sample('1234567890abcdef', 5)) + "@sina.com"
    print(user_email)


print(email_element.get_attribute("placeholder"))
email_element.send_keys("JHzhang@sina.com")
print(email_element.get_attribute("value"))

user_name_element_node = driver.find_elements_by_class_name("controls")[1]
user_element = user_name_element_node.find_element_by_class_name("form-control")
user_element.send_keys("JHzhang")
driver.find_element_by_name("password").send_keys("123456789")
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")

# time.sleep(3)
# driver.close()