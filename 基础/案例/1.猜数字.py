import random
a = random.randint(1,10)            #生成随机数 a

print(type(a))

b = input('请输入')                 #输入数字 b
print(type (b))
c = int(b)

while a!=c:                         # a!=b 时开始循环
    
    b = input("输错了，请重新输入")

    c = int(b)

    if a == c:
        print('输入正确！')
    else:
        print('还是不对')

    

print('游戏结束')

