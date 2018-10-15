from threading import Thread
import time
import random
from queue import Queue 

MAX_NUM = 5
queue = Queue(MAX_NUM)

class ProducerThread(Thread):
    def run(self):
        nums = range(MAX_NUM) #Will create the list [0, 1, 2, 3, 4]
        global queue
        while True:
            num = random.choice(nums) #Selects a random number from list [0, 1, 2, 3, 4]
            queue.put(num)
            print("Produced", num )
            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            num = queue.get()
            print("Consumed", num )
            queue.task_done() #关键
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()