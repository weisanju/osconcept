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

* 访问资源对象的主体
* 通过 `Subject currentUser = SecurityUtils.getSubject();`

## *SecurityManager*

* *shiro*核心,总控,负责管理所有*subject*,进行认证授权,及会话缓存的管理

* 实例化

  * web程序通常通过  *Shiro Servlet Filter* 来实例化
  * 通常每个应用只有一个 *manager*
  * 可以通过 ini配置文件,*spring XML*去实例化它

* 配置示例

  ```
  [main]
  cm = org.apache.shiro.authc.credential.HashedCredentialsMatcher
  cm.hashAlgorithm = SHA-512
  cm.hashIterations = 1024
  # Base64 encoding (less text):
  cm.storedCredentialsHexEncoded = false
  [users]
  jdoe = TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJpcyByZWFzb2
  asmith = IHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbXNoZWQsIG5vdCB
  ```

* 更多*INI*配置方法 详见 http://shiro.apache.org/documentation.html

  

* *API*调用

  ```java
  Factory<SecurityManager> factory = new IniSecurityManagerFactory("classpath:shiro.ini");
  SecurityManager manager = factory.getInstance();
  SecurityUtils.setSecurityManager(manager);
  ```

## *Realm*

* 有一个或多个*realm* 可以认为是安全实体数据源,用于获取安全实体的对象

* Realm配置 LDAP

  ```
  [main]
  ldapRealm = org.apache.shiro.realm.ldap.JndiLdapRealm
  ldapRealm.userDnTemplate = uid={0},ou=users,dc=mycompany,dc=com
  ldapRealm.contextFactory.url = ldap://ldapHost:389
  ldapRealm.contextFactory.authenticationMechanism = DIGEST-MD5
  ```

  

## *Authenticator* 

* 默认实现的认证器

* 可以自定义实现,指定*AuthenticationStrategy*

* 认证有三步

  * 收集用户信息,(*principals*) 和认证信息(*credentials*)
  * 提交 *principals* 和 *credentials*
  * 返回结果

* *API*

  ```
  AuthenticationToken token = new UsernamePasswordToken(username, password);
  Subject currentUser = SecurityUtils.getSubject();
  currentUser.login(token);
  ```

* 当调用 登录方法时,*securityManager* 会将 *token* 发送各个 *realm* 去验证,验证失败后可以 捕获下面异常

  ```
  //3. Login:
  try {
      currentUser.login(token);
  } catch (IncorrectCredentialsException ice) { …
  } catch (LockedAccountException lae) { …
  }
  …
  catch (AuthenticationException ae) {…
  } 
  ```

  

## *authrizer*

* 授权器

* *API*

  * *roleCheck*

    ```java
    if ( subject.hasRole(“administrator”) ) {
        //show the ‘Create User’ button
    } else {
        //grey-out the button?
    }
    ```

  * *Permission Check*

    ```java
    if ( subject.isPermitted(“user:create”) ) {
        //show the ‘Create User’ button
    } else {
        //grey-out the button?
    } 
    ```

    

  * *Instance-Level Permission Check* 实例级别的访问控制

    ```java
    if ( subject.isPermitted(“user:delete:jsmith”) ) {
        //delete the ‘jsmith’ user
    } else {
        //don’t delete ‘jsmith’
    }
    ```

  * [访问控制文档](http://shiro.apache.org/permissions.html)

    

## *SessionManager*

* 管理*session*的生命周期

* 提供 独立于容器的 分布式*session*解决方案

* *API*

  ```java
  Session session = subject.getSession();
  Session session = subject.getSession(boolean create);
  session.getAttribute(“key”, someValue);
  Date start = session.getStartTimestamp();
  Date timestamp = session.getLastAccessTime();
  session.setTimeout(millis);
  ```

## *Cryptography*

* 密码模块

## *sessionDao*

* 控制session的存放位置

## *cacheManager*

* 缓存管理器,缓存用户,角色,权限等

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

## web支持

**ShiroFilter in web.xml**

```xml
<filter>
    <filter-name>ShiroFilter</filter-name>
    <filter-class>
        org.apache.shiro.web.servlet.IniShiroFilter
    </filter-class>
    <!-- no init-param means load the INI config
        from classpath:shiro.ini --> 
</filter>

<filter-mapping>
     <filter-name>ShiroFilter</filter-name>
     <url-pattern>/*</url-pattern>
</filter-mapping>
过滤器将会过滤每个 请求,只有满足
```

## *INI* *URL*过滤器指定

* 右边时过滤器的名字, 有序的逗号分隔, *(anon, user, perms, authc shiro提供的内置过滤器)* 可以自定义

## Web Session Management

