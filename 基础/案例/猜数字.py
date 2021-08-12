# coding:utf-8
import random
secret = random.randint(1,10)
b = int(secret)
a = 0
t = 5
print("请猜测生成的随机数",end="")
while (b != a) and (t >0):
    a = int(input(''))
    if (a > b):
        print("猜大了")
        print("再猜猜",end='')
    elif (a < b):
        print("猜小了")
        print("再猜猜",end='')
    else:
        print("回答正确!"+"  正确答案是:",b)
    t = t - 1
print("GG")
