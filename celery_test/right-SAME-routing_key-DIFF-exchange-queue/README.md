**正确的用例**


- 使用了不同的QUEUE: c12(queue_c12), c13(queue_c13) 
- 使用不同的exchange: c12(exchange_c12), c13(exchange_c13)
- 使用相同的routing_key: aaa
- c12发出一个task时, 通过exchange(exchange_c12),去`_kombu.binding.exchange_c12`找到了1个路由规则

```
1) "aaa\x06\x16\x06\x16queue_c12"
```

- c13发出一个task时, 通过exchange(exchange_c13),去`_kombu.binding.exchange_c13`找到了1个路由规则

```
1) "aaa\x06\x16\x06\x16queue_c13"
```


即: 
- 将exchange(exchange_c12),routing_key为aaa的task,路由到queue_c12
- 将exchange(exchange_c13),routing_key为aaa的task,路由到queue_c13

- 因为c12和c13监听了不同的queue, 并且task使用了不同的exchange. 所以 c12和c13都能正确的收到routing_key为aaa的task.