for i in range(1, 10):                  #i 是竖向1-9
    for j in range(1, i+1):             #j 是横向 1-(1,9)
        # 打印语句中，大括号及其里面的字符 (称作格式化字段) 将会被 .format() 中的参数替换,注意有个点的
        print('{}x{}={}\t'.format(i, j, i*j), end='')
    print()      # 打印完一个i 换行
 
