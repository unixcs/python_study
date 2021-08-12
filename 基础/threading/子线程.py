# 子线程就是运行在 线程(1) 中的 线程(2)
# 线程1 = 主线程   线程2 = 子线程

import threading
import time

def c(i):
    a = threading.current_thread().name
    print("我是子线程%d   " % i, a)

    # time.sleep(2)
    # print("1")


o = threading.current_thread().name
print(o)
for i in range(1, 10):

    t = threading.Thread(target=c, args=(i, ))
    t.start()

    # c(i)