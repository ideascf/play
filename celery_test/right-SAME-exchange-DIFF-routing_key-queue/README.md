**正确的用例**


- 使用了不同的QUEUE: c10(queue_c10), c11(queue_c11) 
- 使用相同的exchange(exchange_same)
- 使用不同的routing_key: c10(abc), c11(xyz)
- 发出一个task时, 通过exchange(celery),去`_kombu.binding.celery`找到了两个路由规则

```
1) "abc\x06\x16\x06\x16queue_c10"
2) "xyz\x06\x16\x06\x16queue_c11"
```

即: 
- 将routing_key为abc的task,路由到queue_c10
- 将routing_key为xyz的task,路由到queue_c11

- 因为c10和c11监听了不同的queue, 所以c10收到routing_key为abc的task, c11收到routing_key为xyz的task.