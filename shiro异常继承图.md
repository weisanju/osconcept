# shiro异常继承

```
Throwable (java.lang)
    Exception (java.lang)
        RuntimeException (java.lang)
            ShiroException (org.apache.shiro)
                AuthorizationException (org.apache.shiro.authz)
                    UnauthenticatedException (org.apache.shiro.authz)
                    UnauthorizedException (org.apache.shiro.authz)
                    
                AuthenticationException (org.apache.shiro.authc)
                    AccountException (org.apache.shiro.authc)
                        DisabledAccountException (org.apache.shiro.authc)
                            LockedAccountException (org.apache.shiro.authc)
                        ConcurrentAccessException (org.apache.shiro.authc)
                        ExcessiveAttemptsException (org.apache.shiro.authc)
                        UnknownAccountException (org.apache.shiro.authc)
                    CredentialsException (org.apache.shiro.authc)
                        IncorrectCredentialsException (org.apache.shiro.authc)
                        ExpiredCredentialsException (org.apache.shiro.authc)
                    UnsupportedTokenException (org.apache.shiro.authc.pam)


```

# 分析

* *shiroException* 分为 认证异常 和授权异常
* 授权异常 包括 未认证,未授权
* 认证异常包括
  * 账户异常
    * 账户不可用-> 账户锁定
    * 单账户多访问
    * 多次尝试登录不成功
    * 未知账户
  * 密码凭证异常
    * 密码不正确
    * 密码过期
  * 不支持的该认证方式