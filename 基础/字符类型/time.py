# coding:utf-8
# 实现每隔1秒中在屏幕上打印一次“hello, world”并持续打印一个小时，
# 我们肯定不能够直接把print('hello, world')这句代码写3600遍，这里同样需要循环结构。


import time

for i in range(0, 3600, 1):  # 起始位，结束位，步长
    q = i + 1
    print("hello, word >>>>> 这是第%d次" % q)
    time.sleep(1)
