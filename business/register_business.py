from Imooc_selenium.handle.register_handle import RegisterHandle
'''
第二层
业务层，亦是case与handle的桥梁
内容包括业务参数
被测试用例调用
'''
class RegisterBusiness():
    # 执行操作
    def __init__(self):
        self.register = RegisterHandle()

    def login_email_error(self,email,name,password,code):
        self.register.send_user_email(email)
        if self.register.get_user_text("请输入有效的电子邮件地址"):
            print("检验成功")
        elif self.register.get_user_text("字符长度必须大于等于4，一个中文")
        self.register.send_user_name(name)
        self.register.send_user_password(password)
        self.register.send_user_code(code)

    def register_function(self,email,username,password,code,assertCode,assertText):
        self.user_base(email,username,password,code)

        if self.register_h.get_user_text(assertCode,assertText) == None:
            return True
        else:
            return False