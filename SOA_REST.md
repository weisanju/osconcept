# RPC

像使用本地方法一样调用服务端的方法

而客户端通过各种定制的协议 告诉服务端 调用哪个方法，传递哪些参数

# REST

## 有三个主要内容

资源：URL定位

表现层：资源展示

状态变换：通过HTTP四个动词操作，POST,GET,PUT,DELETE

## REST的优点

将基于HTTP的 业务数据与 HTTP协议本身分离

可以在web服务与客户之间 做个代理服务，直接禁止 DELETE PUT请求，而不需要解析业务数据

缓存问题

可以根据 GET 的方法 更快的判断是否使用缓存

## REST基于HTTP操作集语义

createResource：创建一个新的资源，put

getResourceRepresentation：获取资源信息，get

deleteResource：删除资源，delete

modifyResource：更改资源，POST

getMetaInformation：获取资源元数据信息，HEAD







# SOAP

简单对象访问协议











