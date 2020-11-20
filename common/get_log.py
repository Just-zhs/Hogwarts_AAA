import logging
import os


class Logs():
    # 获取根文件地址
    BASE_PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # print(os.path.realpath(__file__))
    # print(os.path.dirname(os.path.realpath(__file__)))
    # print(BASE_PATH)
    # print(__file__)


    def __init__(self):
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')


    def set_handle_stream(self):
        self.handle_stream=logging.StreamHandler()
        self.handle_stream.setLevel(logging.DEBUG)
        self.handle_stream.setFormatter(self.formatter)
        self.logger.addHandler(self.handle_stream)

    def set_handle_file(self):
        file_path=os.path.join(self.BASE_PATH,'log/log.log')
        self.handle_file=logging.FileHandler(file_path,mode="w")
        self.handle_file.setLevel(logging.DEBUG)
        self.handle_file.setFormatter(self.formatter)
        self.logger.addHandler(self.handle_file)

    def get_log(self):
        self.set_handle_file()
        self.set_handle_stream()
        return self.logger

log=Logs().get_log()

if __name__=="__main__":
    log.info("测试用")


