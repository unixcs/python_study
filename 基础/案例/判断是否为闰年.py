# -*- coding: utf-8 -*-
time = 3        #三次机会
while time >0:  
    temp = input("请输入年份")   
    if temp.isdigit():      #判断是输入的值是否为纯数字
        y = int(temp)
        if y/400 == int(y/400):
            print('是闰年')
        else:
            if(y/4 == int(y/4) and y/100 != int(y/100)):
               print('是闰年')
            else:
                print('不是闰年')
    else:
        print("请输正确的年份")
    time = time - 1
print("GG")