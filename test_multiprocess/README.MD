# 多进程多线程
打印指定区间(start,end)的数字，用多进程和多线程拆分执行。
写这段代码的原因是为了分析TypeError: can't pickle _thread.lock objects错误的原因
详情请参见：https://segmentfault.com/n/1330000015845770

---
在写这段代码的时候也遇到了：
```
Fatal Python error: could not acquire lock for <_io.BufferedWriter name='<stdout>'> at interpreter shutdown, possibly due to daemon threads
```
原因的分析参见代码注释底部。
