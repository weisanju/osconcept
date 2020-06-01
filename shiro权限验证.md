# 描述

ApacheShiro 是*java*的一个安全框架,提供认证,授权,加密,会话管理的解决方案



# 功能特点

## *primary* *concerns*

*authentication*:认证

*authorization*:授权

*sessionManager*:会话管理

*cryptography* :加密

## *supporting* *features*

*websupport* *web*:集成到*web*环境

*caching*:缓存用户信息

*concurrency*:并发验证,在多线程应用中 ,在一个线程中开启另一个线程,能把权限自动传播过去

*testing* :提供测试支持

*run as* : 允许用户假装为另外一个用户 去访问

*remember* *me* :记住



# 抽象概念

## *subject* 

​	访问资源对象的主体

## *SecurityManager*

​	*shiro*核心,总控,负责管理所有*subject*,进行认证授权,及会话缓存的管理

## *Authenticator* 

* 默认实现的认证器

* 可以自定义实现,指定*AuthenticationStrategy*

## *authrizer*

* 授权器

## *Realm*

* 有一个或多个*realm* 可以认为是安全实体数据源,即用于获取安全实体的

## *SessionManager*

* 管理*session*的生命周期

## *sessionDao*

* 控制session的存放位置

## *cacheManager*

* 缓存管理器,缓存用户,角色,权限等

## *Cryptography*

* 密码模块

# Shiro过滤器

当 Shiro 被运用到 web 项目时，Shiro 会自动创建一些默认的过滤器对客户端请求进行过滤

| 过滤器简称        | 对应的 Java 类(父包头org.apache.shiro.web.filter) | 示例                           | 解析                                                         |
| :---------------- | :------------------------------------------------ | ------------------------------ | ------------------------------------------------------------ |
| anon              | authc.AnonymousFilter                             | */admins/**=anon*              | 表示该 uri 可以匿名访问                                      |
| authc             | authc.FormAuthenticationFilter                    | */admins/**=auth*              | 表示该 uri 需要认证才能访问                                  |
| authcBasic        | authc.BasicHttpAuthenticationFilter               | */admins/**=authcBasic*        | 表示该 uri 需要 httpBasic 认证                               |
| perms             | authz.PermissionsAuthorizationFilter              | */admins/**=perms[user:add:*]* | 需要认证用户拥有 user:add:* 权限才能访问                     |
| port              | authz.PortFilter                                  | */admins/**=port[8081]*        | 表示该 uri 需要使用 8081 端口                                |
| rest              | authz.HttpMethodPermissionFilter                  | */admins/**=rest[user]*        | 相当于 /admins/**=perms[user:method]，其中，method 表示  get、post、delete 等 |
| roles             | authz.RolesAuthorizationFilter                    | */admins/**=roles[admin]*      | 表示该 uri 需要认证用户拥有 admin 角色才能访问               |
| ssl               | authz.SslFilter                                   | */admins/**=ssl*               | 表示该 uri 需要使用 https 协议                               |
| user              | authc.UserFilter                                  | */admins/**=user*              | 表示该 uri 需要认证或通过记住我认证才能访问                  |
| logout            | authc.LogoutFilter                                | */logout=logout*               | 表示注销,可以当作固定配置                                    |
| noSessionCreation | session.NoSessionCreationFilter                   |                                |                                                              |



# 快速入门

## 添加依赖

```xml
<dependency>
    <groupId>commons-logging</groupId>
    <artifactId>commons-logging</artifactId>
    <version>1.1.3</version>
</dependency>

<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-core</artifactId>
    <version>1.4.0</version>
</dependency>
```

## 配置文件

```
[users]
# admin=admin 分别表示账号和密码，administrator 表示逗号前边的账号拥有 administrator 这个角色。
admin=admin,administrator
zhangsan=zhangsan,manager
lisi=lisi,guest

[roles]
# administrator 表示角色名称，* 表示这个角色拥有所有权限
administrator=*
manager=user:*,department:*
guest=user:query,department:query
其中，每个用户可以拥有多个角色，通过逗号分隔。每个角色可以拥有多个权限，同样通过逗号分隔。
```