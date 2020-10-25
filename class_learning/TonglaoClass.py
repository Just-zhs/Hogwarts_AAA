"""
作业2
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

"""


# 天山童姥类
class TongLao():
    hp = 0
    power = 0

    def __init__(self, hp, power):
        # 构造函数传入hp，attack
        self.hp = hp
        self.power = power

    def see_people(self, name):
        # 定义see_people方法，传入name，分支内处理各种输入的name
        if name == 'WYZ':
            print("师弟！！！！")
        elif name == '李秋水':
            print("师弟是我的！")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print("暂时只支持输入WYZ，李秋水，丁春秋")

    def fight_zms(self, enemy_hp, enemy_power):
        # fight_zms方法（天山折梅手）将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power
        self.hp = self.hp / 2
        self.power = self.power * 10

        self.hp = self.hp - enemy_power
        enemy_hp = enemy_hp - self.power
        # 对hp小于0的情况处理
        if self.hp < 0:
            self.hp = 0
        if enemy_hp < 0:
            enemy_hp = 0

        # 进行一回合制对打，打完之后，比较双方血量。血多的一方获胜
        print(f"我的剩余血量为{int(self.hp)}")
        print(f"敌人的剩余血量为{enemy_hp}")
        if self.hp < enemy_hp:
            # 打印我和敌人的剩余血量
            print("我输了")
        elif self.hp == enemy_hp:
            print("平手")
        else:
            print("我赢了")


if __name__ == '__main__':
    asd = TongLao(100, 50)
    asd.see_people('WYZ')
    asd.see_people('李秋水')
    asd.see_people('丁春秋')
    asd.see_people(123)
    asd.fight_zms(125, 10)
