import logging
import os
import datetime

class UserLog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        consle = logging.StreamHandler()
        self.logger.addHandler(consle)
        self.logger.debug("info")

        # 文件名字
        # 获取当前文件所在目录
        base_dir = os.path.dirname(os.path.abspath(__file__))
        print("This is base_dir :",base_dir)

        # 在获取当前目录的前提下通过join增加logs路径
        log_dir = os.path.join(base_dir, "logs1")
        print("This is log_dir :",log_dir)

        # 定义日志文件名为当前日期（定义格式）加后缀名
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        print("This is log_file name :",log_file)

        # 定义最终拼接完成的日志目录路径（包括文件名）
        log_name = log_dir + "/" + log_file
        print("This is laster log_name :",log_name)

        # 文件输出日志
        self.file_handle = logging.FileHandler(log_name,'a', encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s %(filename)s %(funcName)s %(levelno)s %(levelname)s %(message)s'
        )

        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

        # self.logger.debug("teste12138")

        # self.logger.removeHandler(file_handle)
        # file_handle.close()

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('张哥就是牛逼')
    user.close_handle()