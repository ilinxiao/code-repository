from threading import Thread, Condition
import time
import random

queue = []
condition = Condition()
MAX_NUM = 5

class ProducerThread(Thread):
    def run(self):
        nums = range(MAX_NUM) #Will create the list [0, 1, 2, 3, 4]
        global queue
        while True:
            num = random.choice(nums) #Selects a random number from list [0, 1, 2, 3, 4]
            condition.acquire()
            if len(queue) >= MAX_NUM:
                print("队列已满。")
                condition.wait()
                print('队列有空余，继续执行。')
            queue.append(num)
            print("Produced", num )
            condition.notify()
            condition.release()
            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                condition.wait()
                print("Nothing in queue, but consumer will try to consume")
            num = queue.pop(0)
            print("Consumed", num )
            condition.notify()
            condition.release()
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()