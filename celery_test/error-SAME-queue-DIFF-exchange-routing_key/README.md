**错误的用例**


- 使用了相同的queue(queue_same), 
- 使用不同的exchange: c7(exchange_c7), c8(exchange_c8)
- 使用不同的routing_key: c7(abc), c8(xyz)
- c7发出一个task时, 通过exchange(exchange_c7),去`_kombu.binding.exchange_c7`找到了1个路由规则

```
1) "abc\x06\x16\x06\x16queue_same"
```

- c8发出一个task, 通过exchange(exchange_c8),取`_kombu.binding.exchange_c8`找到了1个路由规则

```
1) "xyz\x06\x16\x06\x16queue_same"
```


即: 
- 将routing_key为abc的task,路由到queue_same
- 将routing_key为xyz的task,路由到queue_same

- 因为c7和c8的都监听queue(queue_same)相同, 所以worker c7会收到c8的task, c8也会收到c7的task.
- 而task(c7)再worker(c8)中是不存在的, 所以worker(c8)收到task(c7)将报错.