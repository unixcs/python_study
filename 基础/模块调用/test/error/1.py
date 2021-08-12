def test1():
    print("----11-----")
    print(num)
    print("----221-----")

def test2():
    print("---211---")
    test1()
    print("---222---")

def test3():
    try:
        print("--311--")
        test1()
        print("---333---")
        except Exception as e：
        print("出现一个异常。。%s"%e)

test3()