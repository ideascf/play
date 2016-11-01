**错误的用例**


- 使用了不同的DEFAULT_QUEUE: queue_c3, queue_c4, 
- 使用默认的exchange(celery) 
- 使用默认的routing_key(celery).
- 发出一个task时, 通过exchange(celery),去`_kombu.binding.celery`找到了两个路由规则

```
1) "celery\x06\x16\x06\x16queue_c4"
2) "celery\x06\x16\x06\x16queue_c3"
```

即: 将routing_key为celery的task,**同时路由**到queue_c4 和 queue_c3. 

- 因为c3和c4的routing_key相同, 所以worker c3 和 c4,会同时收到同一个task.