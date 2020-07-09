"""
# @Time : 2020/7/9 0009 18:36
# @Author : zhangxue
"""
# 函数的精髓是可以把函数当变量值用
def foo():
    print("from foo")
a = foo
# 获得的是函数内存地址
print(a)

# 把foo的内存地址放到列表中
l = [foo,1]

# 获取到foo的内存地址加上（）,可以调用foo函数
l[0]()

