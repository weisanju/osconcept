# 什么是AD域？

是用来 存储并管理 用户账户，计算机账户，打印机，共享文件夹等局域网资源



# AD域对象与属性？

AD域将 用户，计算机，打印机等抽象成对象，通过一些列属性去描述他们



# DC（domain controller）

对象数据储存在 DC内，一个域可以有多台DC，每台DC是平等的，各自存储着一份几乎相同的AD。当任何一台DC添加了一个用户账户后，此账户会被自动复制到其他 DC 的AD。能够使所有DC的 AD同步，也有 RODC只读的域控制器



# LDAP

* (lightweight  directory access protocol ) 轻量目录访问协议
* 是用来查询与更新 AD的 通信协议，AD利用 LDAPnaming path 来表示对象在 AD的位置，以便访问

## 数据组织方式

* LDAP的 DN(distinguished name)有三个属性
  * CN (Common name):通用名称，一般为用户名
  * OU (Organizational unit):组织单位，一般为公司或者部门
  * DC (domain component) 组件，
* RDN(relative):表示DN完整路径中的部分路径
* BaseDN:跟 也就是 domain component 组件
* GUID:128位数值，系统会自动为每一个对象指定唯一GUID
* UPN(user principal name):用户主体名称 比DN更短，更容易记忆的UPN，
  * 例如 张三 的UPN 可以表示为 zhangsan@synopsys.com

# AD与LDAP 的关系

AD是一个数据库，LDAP是一种管理该数据库的服务协议

openLADP 与 AD(Microsoft) 是对LDAP 协议的具体实现

# GC gloabl catalog

全局编录，虽然所有域 共享一个 AD，但是AD数据却分散在各个域内，为了让用户，应用程序更快的找到域内的其他资源，于是就有了GC,GC存储了所有域内的每一个对象的部分属性



