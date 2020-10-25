"""
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
"""

# 动物类
class Animal():
    eyes = 0
    legs = 0

    def __init__(self, name, eyes, legs):
        self.name = name
        self.eyes = eyes
        self.legs = legs

    def get_name(self):
        print(f"我是{self.name}")

    def get_eyes(self):
        print(f"我有{self.eyes}只眼睛")

    def get_legs(self):
        print(f"我有{self.legs}条腿")

# 交通工具类
class Vehicle():
    wheel = 0
    km = 0

    def __init__(self,name, wheel, km):
        self.name = name
        self.wheel = wheel
        self.km = km

    def get_name(self):
        print(f"我是{self.name}")

    def get_wheel(self):
        print(f"我有{self.wheel}个轮子")

    def get_km(self):
        print(f"我能行驶{self.km}公里")

# 书籍类
class Book():

    def __init__(self,name, catagory, page):
        self.name = name
        self.category = catagory
        self.page = page

    def get_name(self):
        print(f"我是{self.name}图书")

    def get_category(self):
        print(f"我是{self.category}类别")

    def get_page(self):
        print(f"我有{self.page}页")

# 电脑类
class Computer():
    def __init__(self,name, cpu, memory):
        self.name = name
        self.cpu = cpu
        self.memory = memory

    def get_name(self):
        print(f"我是{self.name}品牌电脑")

    def get_cpu(self):
        print(f"我的CPU是{self.cpu}")

    def get_memory(self):
        print(f"我的内存是{self.memory}")

# 手机类
class Phone():
    def __init__(self,name, chip, memory):
        self.name = name
        self.chip = chip
        self.memory = memory

    def get_name(self):
        print(f"我是{self.name}品牌手机")

    def get_cpu(self):
        print(f"我的芯片是{self.chip}")

    def get_memory(self):
        print(f"我的内存是{self.memory}")