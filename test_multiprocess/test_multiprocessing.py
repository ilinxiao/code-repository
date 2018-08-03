import multiprocessing
import threading

class TestTask:
    
    def __init__(self):
        print('缓存初始化中...')
        
    def run(self, start, over):
        # print('%d-%d' % (start, over))
        print('thread ident:%s - digital is:' % threading.current_thread().ident, end=',')
        for i in range(start, over):
            print('%d' % (i), end=',')
            pass
        print()
            
class Run:
    
    def __init__(self, task=None):
        self.task = task
        
    def threaded_print(self, start=1, end=25, part=5):
        print('多线程打印数字，从%d到%d。' %(start, end))
        #确定多少个数字
        nums = (end - start) + 1
        part_num = nums//part
        for j in range(1, part+1):
            sub_start = (j-1) * part_num + start
            sub_end = j * part_num + start
            thread = threading.Thread(target=self.task.run, args=[sub_start, sub_end])
            thread.setDaemon(True)
            thread.start()
        
    def process_print(self, process_num,**kwargs):
        print('开始多进程打印...')
        processes = []
        ori_start, ori_end = -1,-1
        if 'end' in kwargs.keys():
            ori_end = kwargs['end']
        
        if 'start' in kwargs.keys():
            ori_start = kwargs['start']
        
        for i in range(process_num):
            
            if ori_start>=0 and ori_end >=0: 
                start = i * (ori_end//process_num) + 1
                end = (ori_end//process_num) * (i+1)
                # print('at i=%d, start is:%d, end is:%d' % (i, start, end))
                kwargs['start'] = start
                kwargs['end'] = end
                
            p = multiprocessing.Process(target=self.threaded_print, kwargs=kwargs)
            p.start()
            processes.append(p)
            
        for p in processes:
            p.join()
            
        print('done.')
        
if __name__ == '__main__':
    task = TestTask()
    """
    arg1:进程数目
    start:打印起始数字
    end:打印结束数字
    part:线程数量
    """
    Run(task=task).process_print(2, start=1, end=200, part=10)
    # Run(task=task).process_print(1)
    
    
'''
遇到的错误：
Fatal Python error: could not acquire lock for <_io.BufferedWriter name='<stdout>'> at interpreter shutdown, possibly due to daemon threads
原因分析：
守护线程与主线程之间的冲突，当主线程已经完成子守护线程仍在执行任务，比如这里的守护线程仍然在往stdout打印数字，这就引起了冲突。因为主线程结束时，调用
finalize函数将包括stdout在内的一些执行环境变量已经关闭或回收了。--初步解释，需要验证一下主线程确实在子线程退出前已经退出。
'''