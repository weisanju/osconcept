*Security Assertion Markup Language*
安全性标记断言的标记语言


1. 用户尝试访问SP提供的服务。

2. SP根据配置生成一个 SAML格式的身份验证请求数据包。
   
3. 
4. 
5. 配置包括
   1. ADFS服务器地址,
   2. 证书,
   3. IDP返回SP消息数据的URL地址,
   4. 身份认证协议等信息,通过浏览器重定向到ADFS服务器进行SAML身份认证.

IDP解码SAML请求,并对用户进行身份验证,IDP要求提供有效登录凭据以验证用户身份。
IDP生成一个 SAML 响应，其中包含经过验证的用户的用户名等信息。按照 SAML 2.0 规范，此响应将使用IDP的 DSA/RSA 公钥和私钥进行数字签名。
IDP将信息返回到用户的浏览器。根据配置的返回路径，浏览器将该信息转发到 SP。
SP使用IDP的公钥验证 SAML 响应。如果成功验证该响应，SP则会将用户重定向到目标网址。
用户成功登陆系统。.

web端启用基于SAML的SSO,使用OneLogin的开源SAML Java工具包
https://github.com/onelogin/java-saml
https://developers.onelogin.com/saml/java



IDP与SP互信配置

1.SP信任IDP
https://adserver.testdomain.com/FederationMetadata/2007-06/FederationMetadata.xml

2.IDP信任SP
在AD FS管理工具中添加信赖方信任（Relying Party Trust）

在Microsoft的AD FS语境中
SAML SP被称作Relying Party（依赖方，信赖方），
(这是因为AD FS支持OAuth/OIDC/WS-Federation，而这三个协议中的单点登录消费方都被称作Relying Party，因此AD FS在对SAML协议支持中并没有采用SAML特有的术语Service Provider，而是统一采用Relying Party来指定不同协议中的单点登录消费方。)


LDAP

ADFS


SAML

<xml>
    yonghu
    
<xml>

user




ASE
