import configparser

class ReadIni():
    def __init__(self,file_name=None,label=None):

        if file_name == None:
            file_name = './config/LocalElement.ini'
        if label == None:
            self.label = 'RegisterElement'
        else:
            self.label = label
        self.cf = self.load_ini(file_name)

    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self,key):
        data = self.cf.get(self.label, key)
        return data

if __name__ == '__main__':
    read_init = ReadIni()
    print(read_init.get_value('user_name'))

