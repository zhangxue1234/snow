"""
# @Time : 2020/7/9 0009 18:53
# @Author : zhangxue
"""

def login():
    print("登录成功")

def transfer():
    print("转账成功")

def withdraw():
    print("提现成功")

data = {
    '0':("退出",None),
    '1':("登录",login),
    '2':("转账",transfer),
    '3':("提现",withdraw)
}

while True:
    for k in data:
        print(k,data[k][0])
    choice = input("请输入命令编号：").strip()
    if not choice.isdigit():
        print("输入数字吧，不然会报错哦")
        continue

    if choice == '0':
        break

    if choice in data:
        data[choice][1]()
    else:
        print("没有这个指令")
        break
