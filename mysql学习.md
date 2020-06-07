# mysql配置文件解析



查看版本 version()



# mysql语法规范

不区分大小写

建议 关键字大写 表明列名 小写

sql格式可以根据需要缩进 换行



# 语法分类

DQL

DML

DDL

TCL

DCL



# 函数

## 单行函数

### 字符函数

查找

替换

填充

去除

### 数学函数

取整

取余

小数取值

### 日期函数

时间:now()

日期:curdate()

时间不包含日期:curtime()

year()获取日期类型或者字符串类型的年

month()/monthname():获取月名

str_to_date(str,date) 

date_format

datediff

### 其他函数

version()

database()

user()

### 流程控制函数

*select  if(10<5,'大','小')*

*case expr when value_1 then statement; else statement end*

*case when expr1 then statement; when expr2 then statement else statement end*

## 聚合函数

*sum,avg,max,min,count*



# 连接查询

内连接

* 等值连接
* 非等值连接
* 自连接

外连接

* 左外
* 右外
* 全外

交叉连接

# 子查询

## 按结果集的行列数不同分类

标量子查询:结果集只有一行一列 

列子查询 结果集只有一列 多行, 搭配多行操作符使用 in,any/some, all

行子查询:结果集 一行多列

表子查询:多行多列

## 按出现的位置

select后面,只支持标量子查询

from 后面:表子查询

where后面:标量子查询,列子查询,行子查询

having后面

exists后面:表子查询



# 数据类型

数值类型

*age int unsigned* 无符号int类型

*t1 int(7) zerofill unisnged* 七位格式控制,不足七位0填充

枚举类型

*c1 enum('a','b','c')*

*set* 类型

c1 set('a','b','c','d')

日期类型

date

time

datetime:

timestamp:不建议使用,2038年截止

| 日期和时间类型 | 字节数 | 最小值              | 最大值              |
| -------------- | ------ | ------------------- | ------------------- |
| date           | 4      | 1000-01-01          | 9999-12-31          |
| datetime       | 8      | 1000-01-01 00:00:00 | 9999-12-31 23:59:59 |
| timestamp      | 4      | 19700101080001      | 2038年              |
| time           | 3      |                     |                     |
| year           | 1      | 1901                | 2155                |

timestamp 取决于时区的影响



# 约束

常见约束

* not null
* default
* primary key
* unique 可以为空
* check 约束检查
* foreign key 外键约束

* 表级约束

  constraint pk primary key(id)

  constraint pk check(gender='1'or gender='0') 

  constraint fk_stuinfo_major foreign key(majorid) references major(id)

  联合主键

* 约束管理
  * alter table 表名 modify column 字段名 字段类型  新约束
  * alter table 表明 add [contraint 约束名] 约束类型(字段名) [外键引用]
  * alter table stuinfo drop primary key
  * 列级约束 不支持起名字



# 标识列

系统提供的默认的序列值

* *auto_increment*:步长与初始值,可以在mysql环境变量查看
* 自增长列必须时唯一的
* 一个表只能有一个
* 只能是数值类型
* 可以通过 set auto_increment_increment  =3 设置步长
* 手动给定初始值设置 初始值



# TCL

* 开启事务

  *set autocommit = 0*

  *start transaction*

  *commit;*

  *rollback*

* 隔离级别
  * 脏读
  * 不可重复读:针对更新,同一个事务的多次查询 数据不一致
  * 幻读:针对插入,同一个事务中 准备更新数据时,其他事务提交了新的行

* mysql隔离级别设置
  * *select @@tx_isolation*
  * *set session transaction isolation level read uncommited*
  * set names gbk
* mysql隔离级别
  * read uncommited
    * 可以读到别人没有提交的数据
  * *read commited*
    * 读已提交
    * 可避免脏读
  * *repeatable read*
    * 可以重复读,但无法避免幻读
  * serializable 串行化
    * 一次只执行一个事务



# 视图

create view as select 

# 变量

## 系统变量

### 全局变量/会话变量

```
查看所有某部分变量
show [session|global] variables  [like] "variable_name"
查看系统变量的某个值
select @@[global|session].系统变量 ;
系统变量赋值
set [global|session] 系统容变量名 = 值
set @@[global|session].系统变量名 = 值
global,session 不写的话 默认为 session

```

## 自定义变量

### 用户变量

用户自定义变量,作用于当前会话

```
声明
set @用户变量名=值
set @用户变量名 := 值
select @用户变量名:= 值;
赋值
select 字段名 into @变量名 from 表
使用
select @变量名
```

### 局部变量

在 *begin end* 块之内的 变量,必须在第一行

需要限定类型

```
声明
declare 变量名 类型 default 值;
赋值
set 局部变量名 [:]= 值
select 局部变量名
```



# 存储过程

一组编译好的sql语句集合

```
create procedure 存储过程名(参数列表)
beign
	方法体
end
参数列表
模式 参数名 参数类型
in stuname varchar(20)
in|out|inout
```

* 存储过程一句话 可以省略 *begin end*
* 每条语句必须加分号 结束符, 可以通过 *delimter* 重新设置
* 调用: *call* 存储过程名(实参列表);
* out模式的参数 可以当作 用户自定义变量一样访问

* *drop procedure p1*
* *desc p1*
* *show create procedure p2*

# 函数

只能有一个返回

```
create function 函数名 (参数列表) returns 返回类型
beign
	函数体
end

select 函数名(参数列表)

```

`` 区分 关键字与字段名表名

mysql中的 +  号  只起到 加法作用,不是数值型变量会试图转换 成数值型

对 null值 进行混合 运算时 也为null

ifnull(expr1,expr2) 判断是否为空

*where last_name like '$_' escape '$'*  申明转义字符

count(*) myisam 引擎 count(\*) 效率高,建议使用 *count(\*)*

order by 后面 支持 *select* 中引用的别名

not 关键字 可以 与 *between and* 配合

sql语言 索引都是从 1开始的

*trim('aa' from 'str')* 去头尾的某些字符串

所有分组函数都忽略null值,且null元素不参与计数

a > any(select ....) 表示 a > 集合任何一个就可以, 即 a>最小值即可

多表删除

delete  a1,a2 from table1 a1 join table2 a2 on 连接条件 where筛选条件

truncate会重置 表的 自增长序列, 而delete不会

create database if not exists books

alter database books character set gbk

create table 表名(

​	列名 列的类型(长度) 约束,

​	列名 列的类型(长度) 约束,

)

表的修改

列名

*alter table book change column publishdata pubDate datetime*

列的类型与约束

*alter table book modify column pubdate* 

添加列

*add column*

删除列

*drop column*

修改表名

*rename to* 

复制表结构 create table copy like author

复制表结构与数据  create table copy2 select * from author

# 流程控制

## 分支结构

case

```
delimeter $
create procedure test_case(in score int)
begin
	case 
	when score >= 90 and score <=100 then select '1';
	when score >= 80 then select '2';
	when score >= 70 then selecet '3';
	else select '4';
	end case ;
end $
```

if

```
if 条件1 then 语句1;
elseif 条件2 then 语句2;
else 语句;
end if;
```

循环结构

```
while,loop,repeat
循环控制
iterate:类似continue
leave:break类似

标签:while 进入循环的条件 do
	循环体;
end while 标签;

标签:loop
	循环体;
end loop 标签

标签:repeat
	循环体;
until 结束循环的条件
end repeat 标签
```



179集

# mysql文件组织

| 文件名    | 作用                                      |
| --------- | ----------------------------------------- |
| log-bin   | 用于主从复制                              |
| log-error | 用于记录mysql启停日志                     |
| log       | 查询日志,默认不开启,记录每条查询sql的日志 |
| data目录  | 数据库数据存放的位置                      |
| frm文件   | 存放数据库定数据                          |
| myd文件   | 数据文件                                  |
| myi       | 索引文件                                  |

数据文件存放路径

配置文件目录:my.cnf

命令目录

启停脚本目录

# mysql逻辑架构

![逻辑架构图](https://i.loli.net/2020/06/07/Me6goXFNGzmYuhK.png)



连接接入层:*connection pool* 

* 负责认证, 线程重用,连接限制,内存检查,缓存

sql 接口层

* DML DDL,存储过程, 视图,触发器

查询sql解析器

优化器

缓存池

管理工具

- 备份恢复
- 安全副本
- 集群
- 配置
- 迁移
- 元数据

可插拔的存储引擎

* myisam
* innoDB
* Memory



大致分为四层

第一层是 连接层, 解决谁可以连,怎么通信的问题

第二层是 sql处理层,包括解析,优化等,解决要查什么的问题

第三层是 存储存 , 解决 数据底层 是如何存

第四层是 管理层, 负责 备份,恢复,集群等

# 存储引擎

查看

```
show engine
show variables like '%storgeengine%'
```

| 对比项 | MyISAM     | InnoDB                        |
| ------ | ---------- | ----------------------------- |
| 主外键 | 不支持     | 支持                          |
| 事务   | 不支持     | 支持                          |
| 行表锁 | 表锁       | 行锁                          |
| 缓存   | 只缓存索引 | 可以缓存真实数据,对内存有要求 |
| 表空间 | 小         | 大                            |
| 关注点 | 性能       | 事务                          |

*XtraDB* 存储引擎

# mysql优化

sql性能下降的原因

* sql本身写得烂
* 索引失效
* 关联查询太多(设计缺陷)
* 服务器调优 不给力

sql执行顺序

```
from
join on
where
group by
having
select
distinct
order by
limit
```

七种连接理论

- join
- left join
- right join
- fuller join
- left join and b.key is null
- right join  and a.key is null
- fuller join  and a.key is null or b.key is null

索引

* 索引是一种数据结构,排好序的快速查找数据结构
* 在数据之外,数据库系统还维护者满足特定 查找算法的数据结构,这些数据结构以某种方式引用数据
* 索引的每个结点包含索引键值(即对应数据库索引字段),和指向对应数据记录的物理地址

索引分类

* 单值索引: 索引的key只有一个 字段
* 唯一索引
* 复合索引

建立索引的建议

* 主键自动建立索引
* 频繁条件查询字段作为索引
* join的字段建立索引
* 复合索引 一般好于 单值索引
* 排序的字段 可以建立索引
* 分组的字段 也可以建立索引

* 字段分布均匀, 经常更新的字段 ,记录少的表 不需要建立索引

mysql性能分析: *explan* + *sql*语句



* explan表解析
  * ID:表示表的读取顺序

    * id相同的情况下:执行顺序由上至下

    * id不同的情况下: id越大,越先被执行( 例如最里面的越先被执行)

      

  * select_type:数据是以何种方式读取的

    * simple

      简单的子查询,不包含子查询或者*union*

    * primary

      查询中若包含多层子查询,最外层的查询为*primary*查询

    * subquery

      子查询

    * derived

      * 子查询衍生的虚表的表名格式为 derived${id},

      * 其中id为explan表 的 id,表示由这个id代表的某步骤产生的临时表

    * union

      * 若第二个select 出现在 union之后,则被标记为 union
      * 若union包含在 from子句的 子查询中,则外层的select将被标记为 drived

    * union result

      * 从union表获取结果的select

  * table:表明

  * type:实际索引使用方式

    * 访问类型:性能升序增加

      * ALL

        全表扫描

      * index

        * *full index scan* 全索引扫描
        * 遍历索引树
        * 通常取 的值 是索引

      * range

        * 只检索给定范围的行,使用一个索引来选择行 
        * 例如between in,> < 等
        * 索引开始于某一点,结束于某一点

      * ref

        * 非唯一性索引扫描,返回匹配某个单独值得所有行

      * eq_ref

        * 唯一性索引扫描,对于每个索引键 只有一条记录与之匹配
        * 常见于主键或唯一扫描

      * const

        * 只有一条记录匹配,通常常见于 主键和唯一性索引
        * 只有一条记录被匹配

      * system

        表只有一行记录,等于系统表,是const类型的特例

    * system>const>eq_ref>ref>fulltext>ref_or_null>index_merge>unique_subquery>index_subquery>rang>index>all

    * 保证达到 range级别 即可,最好能达到ref

  * possibleKeys:可能用到的索引

    * 因为一张表索引只能使用一个

  * keys:实际使用到的索引

    * 覆盖索引

      查询的字段 刚好建立了索引,且查询顺序一致

  * key_len

    * 表示索引中使用的字节数,可通过该计算查询中使用的索引的长度,长度越短越好
    * 根据表定义计算得出得 索引字节数

  * ref:显示该次查询 使用的索引的值 是 引用得哪个地方的

    * const 引用的常量
    * test.t1.id 引用 某个库的某个表的某个字段

  * rows

    * 找到记录大致要读取的行数
    * 每张表有多少行被优化器查询
    * 根据表统计信息,及索引选用情况,大致估算出找到所需的记录需要读取的行数

  * extra:表示不适合在其他列中显示,但十分重要的额外信息

    * *using filesort*	没有用到索引的排序,因为联合索引 字段顺序问题

      ```
      example
      index(col1,col2,col3)
      col1='ac' order by col2,col3
      这种情况是会用到索引
      如何建索引 , 就 如何按照索引走
      ```

    * *using temporary*:使用了临时表,保存中间结果,常见于order by,group by

      * 对于联合索引 请按照建立的顺序使用

    * *using index*

      * select操作中使用了覆盖索引,效率不错
      * 如果同时出现了*usingwhere* 表明索引被用来 执行索引键值的查找
      * 如果没有出现 *using where* 表明索引用来读取数据而非执行查找

    * *using where*

      * 使用*where*过滤

    * *using join buffer*

      * 使用了连接缓存

    * *impossiable where*

      * 不可能的 where过滤条件

    * *select table optimized away*

      * 在没有groupby子句的情况下,基于索引优化 MIN/MAX操作
      * 或 对于MyISAM 存储引擎 优化 count(*) 操作,不必等到执行阶段计算

    * *distinct*

      