#多线程

import threading
import time


exitFlag = 0

threadLock = threading.Lock()
threads = []


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()      #如果exitFlag不等于0 则退出
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


#使用threading模块创建线程，继承threading.Thread 创建一个新的子类。
class MyThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        #获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()
#        print("退出线程： " + self.name)


if __name__ == '__main__':
    thread1 = MyThread(1, "Thread-1", 1)
    thread2 = MyThread(2, "Thread-2", 2)

    thread1.start()
    thread2.start()
    #添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)
    for t in threads:
        t.join()
    print("退出线程")




