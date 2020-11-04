import random
import string

def name_gener():
    a = "".join(random.sample(string.ascii_letters, 8))
    b = str('测试' + a)
    return b

def account_gener():
    a = "".join(random.sample(string.ascii_letters, 8))
    return a

def number_gener():
    b = "".join(random.sample(string.digits, 10))
    c = str('1' + b)
    return c

if __name__ == '__main__':
    name = name_gener()
    print(name)
    account = account_gener()
    print(account)
    num = number_gener()
    print(num)
