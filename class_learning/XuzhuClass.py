"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""
from class_learning.TonglaoClass import TongLao
# 导入童姥类

class Xuzhu(TongLao):
    # 定义虚竹类
    def __init__(self, hp, power):
        # 构造函数继承童姥类
        super().__init__(hp, power)

    def read(self):
        # 定义read方法
        print("罪过罪过")

    def see_people(self, name):
        # 改造see_people方法，使其调用read方法
        self.read()

    def fight_zms(self, enemy_hp, enemy_power):
        # 改造fight_zms方法，使其调用read方法
        self.read()


if __name__ == '__main__':
    asd = Xuzhu(100, 20)
    asd.see_people("www")
    asd.fight_zms(10, 20)
    asd.read()
