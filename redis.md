# 简介

是一个高性能的key-value数据库

Redis支持数据的持久化

Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储

Redis支持数据的备份，即master-slave模式的数据备份

# 入门

[下载地址](https://github.com/dmajkic/redis/downloads。)

运行命令:`redis-server.exe redis.conf`

`redis-cli.exe -h 127.0.0.1 -p 6379`

# Redis 数据备份与恢复

* `CONFIG get dir`

* save命令

* 后台bgsave

# Redis 安全

* `CONFIG get requirepass`
* 设置密码:`CONFIG set requirepass "xjq"`
* 验证密码:`AUTH <password>`

# Redis 性能测试

`redis-benchmark [option] [option value]`

|      |           |                                            |           |
| ---- | --------- | ------------------------------------------ | --------- |
| 1    | **-h**    | 指定服务器主机名                           | 127.0.0.1 |
| 2    | **-p**    | 指定服务器端口                             | 6379      |
| 3    | **-s**    | 指定服务器 socket                          |           |
| 4    | **-c**    | 指定并发连接数                             | 50        |
| 5    | **-n**    | 指定请求数                                 | 10000     |
| 6    | **-d**    | 以字节的形式指定 SET/GET 值的数据大小      | 2         |
| 7    | **-k**    | 1=keep alive 0=reconnect                   | 1         |
| 8    | **-r**    | SET/GET/INCR 使用随机 key, SADD 使用随机值 |           |
| 9    | **-P**    | 通过管道传输 <numreq> 请求                 | 1         |
| 10   | **-q**    | 强制退出 redis。仅显示 query/sec 值        |           |
| 11   | **--csv** | 以 CSV 格式输出                            |           |
| 12   | **-l**    | 生成循环，永久执行测试                     |           |
| 13   | **-t**    | 仅运行以逗号分隔的测试命令列表。           |           |
| 14   | **-I**    | Idle 模式。仅打开 N 个 idle 连接并等待。   |           |

# 客户端命令

| S.N. | 命令               | 描述                                       |
| :--- | :----------------- | :----------------------------------------- |
| 1    | **CLIENT LIST**    | 返回连接到 redis 服务的客户端列表          |
| 2    | **CLIENT SETNAME** | 设置当前连接的名称                         |
| 3    | **CLIENT GETNAME** | 获取通过 CLIENT SETNAME 命令设置的服务名称 |
| 4    | **CLIENT PAUSE**   | 挂起客户端连接，指定挂起的时间以毫秒计     |
| 5    | **CLIENT KILL**    | 关闭客户端连接                             |



# Java使用redis

