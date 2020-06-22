# 关于Ansible

Ansible是一个IT自动化工具，能够配置系统，部署软件，编码高级的IT任务例如 持续部署或者 0宕机 滚动更新



# 安装Ansible

## 安装Ansible自身

`sudo yum install ansible`

## 安装shell命令行自动补全

`yum install epel-release`

`yum install python-argcomplete`

## 自动补全设置

`activate-global-python-argcomplete`



# 概念

## 控制节点

能够运行Ansible命令 和playbooks 通过

`/usr/bin/ansible or/usr/bin/ansible-playbook`

## 受管节点

Ansible管理的网络设备

## Inventory

一系列的受管节点，清单文件也叫做 hostfile,可以为每个受管节点指定IP，也可以用来创建或者嵌套组，方便扩容，

## Modules

ansible功能单位，每一个module都有专门的 功能，从管理特定数据库的用户到 管理特定类型的网络设备VLAN接口，可以执行一个模块的一个task，也可以执行多个模块的多个功能，也就是剧本

## tasks

Ansible的 执行动作单位

## playbooks

* 有序的任务列表
* 以YAML方式写的

# 构建清单

* 清单文件是 受管主机的IP或主机名 列表
* 组名 用 [groupname]标识，组之间用 组名分隔
* 可以使用YAML格式

* 组

  * 有两个默认组，all, ungruoped
  * all组包含每一个主机
  * ungrouped 包含没有组的主机
  * 每一个组至少有两个组 all，ungrouped
  * 每一个主机 可以放在多个组

* 主机名 符号

  * 数值区间：`www[01:50].example.com`
  * 字母区间：`db-p[a:f].example.com`

* 添加变量

  * INI：`host1 http_port=80 maxRequestsPerChild=808`

  * YAML：

    ```yaml
    atlanta:
      host1:
        http_port: 80
        maxRequestsPerChild: 808
    
    ```

* 添加组变量，`:vars`

  ​	

  ```
  [atlanta]
  host1
  host2
  
  [atlanta:vars]
  ntp_server=ntp.atlanta.example.com
  proxy=proxy.atlanta.example.com
  ```

  ```
  atlanta:
    hosts:
      host1:
      host2:
    vars:
      ntp_server: ntp.atlanta.example.com
      proxy: proxy.atlanta.example.com
  ```

  

* 使用children: 给组分组

  ```yaml
  all:
    children:
      usa:
        children:
          southeast:
            children:
              atlanta:
                hosts:
                  host1:
                  host2:
              raleigh:
                hosts:
                  host2:
                  host3:
            vars:
              some_server: foo.southeast.example.com
              halon_system_timeout: 30
              self_destruct_countdown: 60
              escape_pods: 2
          northeast:
          northwest:
          southwest:
  ```

* 子组的变量 会覆盖父组的变量

* 主机变量与 组变量 可以定义在如下路径

  ```
  /etc/ansible/group_vars/raleigh # can optionally end in '.yml', '.yaml', or '.json'
  /etc/ansible/group_vars/webservers
  /etc/ansible/host_vars/foosball
  ```

  

# 动态清单

description

* 如果你的配置根据需求 时常变动，你可能需要从多个源头 载入hosts，例如云服务提供商，LDAP，Cobber,或者其他企业的CMDB
* Ansible提供两种方式，连接外部存储
  * inventory plugins：推荐使用plugins
  * inventory scripts
* 红帽的 RedHatAnsibleTower 提供GUI界面编辑与同步，并提供web and Rest服务

example with Cobber

* Ansible能与cobber无缝集成。cobber主要用于OS安装，DHCP,DNS 管理，从当轻量级的CMDB



# 模式：定位主机和组

* `ansible <pattern> -m <module_name> -a "<module options>""`

* pattern 是 playbook的 hosts 选项

* pattern模式

  | Description            | Pattern(s)                   | Targets                                             |
  | ---------------------- | ---------------------------- | --------------------------------------------------- |
  | All hosts              | all (or *)                   |                                                     |
  | One host               | host1                        |                                                     |
  | Multiple hosts         | host1:host2 (or host1,host2) |                                                     |
  | One group              | webservers                   |                                                     |
  | Multiple groups        | webservers:dbservers         | all hosts in webservers plus all hosts in dbservers |
  | Excluding groups       | webservers:!atlanta          | all hosts in webservers except those in atlanta     |
  | Intersection of groups | webservers:&staging          | any hosts in webservers that are also in staging    |

* pattern高级用法

  * 使用变量 ， ansible-playbook， -e 传递的ansible-playbook

  * 使用组定位，

    ```
    webservers[0]       # == cobweb
    webservers[-1]      # == weber
    webservers[0:2]     # == webservers[0],webservers[1]
                        # == cobweb,webbing
    webservers[1:]      # == webbing,weber
    webservers[:3]      # == cobweb,webbing,weber
    ```

  * 使用正则表达式 ，以 ~ 开头的

  * 在命令行选项指定 --limit 

    * ```
      ansible-playbook site.yml --limit datacenter2 //指定主机
      ```

    * ```
      ansible-playbook site.yml --limit @retry_hosts.txt //指定从文件读主机
      ```

# 临时命令行

* 语法：`ansible [pattern] -m [module] -a "[module options]"`

* ```
  重启
  ansible atlanta -a "/sbin/reboot" -f 10
  ansible atlanta -a "/sbin/reboot" -f 10 -u username //默认以当前用户运行
  ansible atlanta -a "/sbin/reboot" -f 10 -u username --become [--ask-become-pass]
  --ask-become-pass or -K ：提示密码输入
  shellmode
  -m 指定命令模块，默认是 commandModule
  ansible raleigh -m shell -a 'echo $TERM'
  
  管理文件
  copy Mode
  ansible atlanta -m copy -a "src=/etc/hosts dest=/tmp/hosts"
  filemode
  ansible webservers -m file -a "dest=/srv/foo/b.txt mode=600 owner=mdehaan group=mdehaan"
  ansible webservers -m file -a "dest=/path/to/c mode=755 owner=mdehaan group=mdehaan state=directory"
  ansible webservers -m file -a "dest=/path/to/c state=absent"
  
  管理包
  ansible webservers -m yum -a "name=acme state=present"
  ansible webservers -m yum -a "name=acme-1.5 state=present"
  ansible webservers -m yum -a "name=acme state=latest"
  //确保 包是没有安装的
  ansible webservers -m yum -a "name=acme state=absent"
  
  管理用户和组
  ansible all -m user -a "name=foo password=<crypted password here>"
  ansible all -m user -a "name=foo state=absent"
  
  管理服务
  ansible webservers -m service -a "name=httpd state=started"
  ansible webservers -m service -a "name=httpd state=restarted"
  ansible webservers -m service -a "name=httpd state=stopped"
  
  收集信息
  ansible all -m setup
  
  //如果没有其他对应的module
  就是用默认的module，使用shell命令
  ```