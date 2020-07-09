"""
# @Time : 2020/7/9 0009 19:19
# @Author : zhangxue
# 编程的思维方式，遇到一个庞大的功能，
# 先把流程顺序写清楚，然后把每一步都分出来写，然后合在一起
"""

# 函数的嵌套定义，在函数内定义其他函数
# 求四个值中最大的
# 先判断两个值中最大的

# def max2(x,y):
#     if x > y:
#         return x
#     else:
#         return y
#
# def max4(a,b,c,d):
#     res1 = max2(a,b)
#     res2 = max2(res1,c)
#     res3 = max2(res2,d)
#     return res3
#
# a = max4(1,2,3,4)
# print(a)


# # # 求圆的周长和面积
#
# def yuan(r,action=0):
#
#     def zhouchang():
#         return 2 * r * 3.14
#
#     def mianji():
#         return r * r * 3.14
#
#     if action == 0:
#          return zhouchang()
#     else:
#         return mianji()
# a = yuan(3,action=0)
# print(a)

