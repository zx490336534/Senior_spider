#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
from redis import WatchError

__author__ = 'Terry'

# host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
# decode_responses=True，写入的键值对中的value为str类型，为 False 写入的则为字节类型，默认为False。
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# print(r.get('name'))
# r.set('name', 'test111')
# print(r.get('name'))
#
# #  手动指明连接池，但是我们项目中不需要
# pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
# r = redis.Redis(connection_pool=pool)

# 批量执行命令 ，管道中的命令不是 原子性 的，前面的命令执行成功了，后面的出错，前面还是成功了！！！
# pipe = r.pipeline(transaction=True)
# pipe.set('name', 'python')
# pipe.set('age', 22)
# pipe.execute()

# 事务
with r.pipeline() as pipe:
    while True:
        try:
            # 监控 OUR-SEQUENCE-KEY  密钥
            pipe.watch('li')
            # 监听后，管道会进行 立刻执行命令 模式，除非我们设置为缓存模式
            # 这样允许我们获得序列的值
            # current_value = pipe.get('OUR-SEQUENCE-KEY')
            # next_value = int(current_value) + 1
            # 使用 multi 恢复到缓存模式
            # 手动开启一个事务
            # 中间的所有命令都是 原子性， 全部成功或者全部失败
            pipe.multi()
            # pipe.set('OUR-SEQUENCE-KEY', next_value)
            pipe.set('name', 'watch111')
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