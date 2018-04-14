#!/usr/bin/env python
# -*- coding: utf-8 -*-
from redis import WatchError

__author__ = 'Terry'

import redis


pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
#
# name = r.get('name')
# print(name)
# r.set('name', 'py_name')
# print(r.get('name'))
#
# l = r.lrange('list_test', 0, 1000)
# print(l)
#
# pipe = r.pipeline()
# print(pipe.set('foo', 'bar').sadd('faz', 'baz').incr('auto_number').execute())


with r.pipeline() as pipe:
    while True:
        try:
            # 监控 OUR-SEQUENCE-KEY  密钥
            pipe.watch('OUR-SEQUENCE-KEY')
            # 监听后，管道会进行 立刻执行命令 模式，除非我们设置为缓存模式
            # 这样允许我们获得序列的值
            current_value = pipe.get('OUR-SEQUENCE-KEY')
            next_value = int(current_value) + 1
            # 使用 multi 恢复到缓存模式
            pipe.multi()
            pipe.set('OUR-SEQUENCE-KEY', next_value)

            # 执行许多行动

            # 最后执行 命令
            pipe.execute()
            # 一直执行到这里，所以命令全部实现
            # 退出
            break
        except WatchError as e:
            # 另一个客户端修改了 OUR-SEQUENCE-KEY 的值，
            # 在我们监听之后，到最后 执行之前 这个时间段内
            # 回滚，重新执行
            continue


