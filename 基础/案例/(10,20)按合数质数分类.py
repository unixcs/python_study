for num in range (10,20):
    for i in range(2,num):
        if num % i == 0:
            print(num , '是合数')
            break
        else:
            print(num , '是质数')
            break

