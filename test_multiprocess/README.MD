# 多进程多线程
打印指定区间(start,end)的数字，用多进程和多线程拆分执行。
写这段代码的原因是为了分析TypeError: can't pickle _thread.lock objects错误的原因
详情请参见：https://segmentfault.com/n/1330000015845770

---
在写这段代码的时候也遇到了：
```
Fatal Python error: could not acquire lock for <_io.BufferedWriter name='<stdout>'> at interpreter shutdown, possibly due to daemon threads
```
原因的分析参见代码注释底部。[stack overflow相关问题](https://stackoverflow.com/questions/45267439/fatal-python-error-and-bufferedwriter/45389681#45389681)
另外一个跟[python多线程的相关讨论](https://segmentfault.com/q/1010000012483275)也比较有意思。其中一个回答中说道，多线程多进程程序还是需要控制好逻辑和调度很重要。十分赞同，在此记录下以后或许能用到。

#  生产者消费者Python实现
producer_consumer.py：生产者消费问题的原型
condition_producer_consumer.py：使用Threading.Condition实现问题
queue_producer_consumer.py：queue实现，实际是对Condition的封装
参考：http://blog.jobbole.com/52412/