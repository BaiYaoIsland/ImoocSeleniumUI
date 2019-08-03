import logging
import os
import datetime

class UserLog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # # 控制台输出日志
        consle = logging.StreamHandler()
        self.logger.addHandler(consle)
        self.logger.debug("info")
        # 文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, "logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        log_name = log_dir + "/" + log_file
        print(log_dir + "\n" + log_file + "\n" + log_name)

        # 文件输出日志
        file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s----> %(funcName)s %(levelno)s %(levelname)s -----%(message)s')
        file_handle.setFormatter(formatter)
        self.logger.addHandler(file_handle)
        self.logger.debug("teste1234")

        self.logger.removeHandler(file_handle)
        file_handle.close()
    def get_log(self):
        return self.logger

if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('test')