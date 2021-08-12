# 设置子线程守护进程
# 主线程结束时直接销毁子线程

from threading import *
from time import *


def dance():
    print(current_thread())
    for i in range(6):
        print('跳舞...')
        sleep(0.2)


if __name__ == '__main__':
    # 将该线程设置为守护主线程
    dance_thread = Thread(target=dance)
    dance_thread.setDaemon(True)    # 守护进程   # 如果不设置守护进程，主线程等待子线程执行完再结束
    dance_thread.start()
    sleep(0.5)
    print('over')
