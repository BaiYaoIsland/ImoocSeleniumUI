import os

#获取当前目录的上级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#获取当前文件的绝对路径
FILE_DIR = os.path.abspath(__file__)

#获取文件的绝对目录
FOLER_PATH = os.path.abspath(os.path.dirname(__file__))

print(BASE_DIR + "\n" + FILE_DIR + "\n" + FOLER_PATH)