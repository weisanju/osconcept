# spring框架

数据访问/集成

web(MVC/remoting)

AOP Aspects Instrumentation Messaging

CoreContainer

Test





# 核心容器组成

## spring-core

基础部分

## spring-beans

提供BeanFactory

## spring-context

建立在 core,beans 模块的基础上,以JNDI方式访问对象

Context模块继承自Bean模块，并且添加了国际化,事件传播、资源加载和透明地创建上下文（比如，通过Servelet容器）等功能

也支持Java EE的功能

## spring-context-support

提供了对第三方库集成到Spring上下文的支持

如缓存（EhCache, Guava, JCache）

调度（CommonJ, Quartz）

模板引擎（FreeMarker, JasperReports, Velocity）等



## spring-expression

强大的表达式语言，用于在运行时查询和操作对象图

支持set和get属性值、属性赋值、方法调用、访问数组集合及索引的内容、逻辑算术运算、命名变量、通过名字从Spring IoC容器检索对象，还支持列表的投影、选择以及聚合等。



# spring-IOC容器

* 是spring的核心功能,将创建对象,把他们连接一起,配置他们,并管理整个生命周期
* spring提供了两个不通类型的容器
  * [ Spring BeanFactory 容器](https://www.w3cschool.cn/wkspring/j3181mm3.html)
    * 由org.springframework.beans.factory.BeanFactory 接口来定义
    * 它的实现类包括BeanFactoryAware，InitializingBean，DisposableBean
  * [Spring ApplicationContext 容器](https://www.w3cschool.cn/wkspring/yqdx1mm5.html)
    * 企业特定的功能，例如从一个属性文件中解析文本信息的能力，发布应用程序事件给感兴趣的事件监听器的能力
    * org.springframework.context.ApplicationContext 接口定义。



# Spring 的 BeanFactory 容器

* 在 Spring 中，有大量对 BeanFactory 接口的实现。其中，最常被使用的是 **XmlBeanFactory** 类,一般使用的是 ApplicationContext

# Spring ApplicationContext 容器

* Application Context 是 BeanFactory 的子接口
* 常用的三个实现
  * **FileSystemXmlApplicationContext**
  * **ClassPathXmlApplicationContext**
  * **WebXmlApplicationContext**

# springBean定义

* bean 是由用容器提供的配置元数据创建的

* 配置元素据

  - 如何创建一个 bean
  - bean 的生命周期的详细信息
  - bean 的依赖关系

* bean定义

  | 属性                     | 描述                                                         |
  | ------------------------ | ------------------------------------------------------------ |
  | class                    | 这个属性是强制性的，并且指定用来创建 bean 的 bean 类。       |
  | name                     | 这个属性指定唯一的 bean 标识符。在基于 XML 的配置元数据中，你可以使用 ID 和/或 name 属性来指定 bean 标识符。 |
  | scope                    | 这个属性指定由特定的 bean 定义创建的对象的作用域，它将会在 bean 作用域的章节中进行讨论。 |
  | constructor-arg          | 它是用来注入依赖关系的，并会在接下来的章节中进行讨论。       |
  | properties               | 它是用来注入依赖关系的，并会在接下来的章节中进行讨论。       |
  | autowiring mode          | 它是用来注入依赖关系的，并会在接下来的章节中进行讨论。       |
  | lazy-initialization mode | 延迟初始化的 bean 告诉 IoC 容器在它第一次被请求时，而不是在启动时去创建一个 bean 实例。 |
  | initialization 方法      | 在 bean 的所有必需的属性被容器设置之后，调用回调方法。它将会在 bean 的生命周期章节中进行讨论。 |
  | destruction 方法         | 当包含该 bean 的容器被销毁时，使用回调方法。它将会在 bean 的生命周期章节中进行讨论。 |



* spring配置元数据

  * 基于 XML 的配置文件

  * 基于注解的配置

  * 基于 Java 的配置

    

* spring bean 作用域

  | 作用域         | 描述                                                         |
  | -------------- | ------------------------------------------------------------ |
  | singleton      | 在spring IoC容器仅存在一个Bean实例，Bean以单例方式存在，默认值 |
  | prototype      | 每次从容器中调用Bean时，都返回一个新的实例，即每次调用getBean()时，相当于执行newXxxBean() |
  | request        | 每次HTTP请求都会创建一个新的Bean，该作用域仅适用于WebApplicationContext环境 |
  | session        | 同一个HTTP Session共享一个Bean，不同Session使用不同的Bean，仅适用于WebApplicationContext环境 |
  | global-session | 一般用于Portlet应用环境，该运用域仅适用于WebApplicationContext环境 |
  * 根据经验对有状态的bean应该使用prototype作用域，而对无状态的bean则应该使用singleton作用域

* spring bean的 生命周期

  Bean的定义——Bean的初始化——Bean的使用——Bean的销毁

* Spring Bean 后置处理器

  * 定义所有bean的 初始化之前，初始化之后的 处理
  * 接口 ：BeanPostProcessor ->postProcessBeforeInitialization(),postProcessAfterInitialization()

* spring继承

  * parent = “beanName"

  * Bean 定义模板:abstract="true"

    ```xml
     <bean id="beanTeamplate" abstract="true">
          <property name="message1" value="Hello World!"/>
          <property name="message2" value="Hello Second World!"/>
          <property name="message3" value="Namaste India!"/>
       </bean>
    
       <bean id="helloIndia" class="com.tutorialspoint.HelloIndia" parent="beanTeamplate">
          <property name="message1" value="Hello India!"/>
          <property name="message3" value="Namaste India!"/>
       </bean>
    ```

    

# spring依赖注入

主要是分两种注入类型

* 基于 构造函数注入依赖
* 基于 无参构造实例化后，调用setter方法

# 构造函数注入依赖

*  `<constructor-arg ref="spellChecker"/>`
* 多个参数 按顺序
* 或者按 类型
* 按 索引值 index

# setter依赖注入

*  `<property name="spellChecker" ref="spellChecker"/>`

* 使用p-namespace 简化配置

  ```xml
   <bean id="john-classic" class="com.example.Person"
        p:name="John Doe"
        p:spouse-ref="jane"/>
     </bean>
  ```

* 注入内部bean

  ```xml
       <property name="spellChecker">
           <bean id="spellChecker" class="com.tutorialspoint.SpellChecker"/>
         </property>
  ```

  

* 注入集合

  * `<list>`

    ```xml
    <property name="addressList">
             <list>
                <value>INDIA</value>
                <value>Pakistan</value>
                <value>USA</value>
                <value>USA</value>
             </list>
          </property>
    ```

    

  * `<set>`

    ```xml
             <set>
                <value>INDIA</value>
                <value>Pakistan</value>
                <value>USA</value>
                <value>USA</value>
            </set>
    ```

    

  * `<map>`

    ```xml
     <map>
                <entry key="1" value="INDIA"/>
                <entry key="2" value="Pakistan"/>
                <entry key="3" value="USA"/>
                <entry key="4" value="USA"/>
             </map>
    ```

    

  * `<props>`

    ```xml
      <property name="addressProp">
             <props>
                <prop key="one">INDIA</prop>
                <prop key="two">Pakistan</prop>
                <prop key="three">USA</prop>
                <prop key="four">USA</prop>
             </props>
          </property>
    ```

    

* 注入空串与null值

  `<property name="email" value=""/>`

  ` <property name="email"><null/></property>`

  

# 自动装配

可以不使用  constructor-arg ,property 下，自动装配，减少XML配置数量

## 自动装配模式

| 模式                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| no                                                           | 这是默认的设置，它意味着没有自动装配，你应该使用显式的bean引用来连线。你不用为了连线做特殊的事。在依赖注入章节你已经看到这个了。 |
| [byName](https://www.w3cschool.cn/wkspring/fwdz1mmb.html)    | 由属性名自动装配。Spring 容器看到在 XML 配置文件中 bean 的自动装配的属性设置为 byName。然后尝试匹配，并且将它的属性与在配置文件中被定义为相同名称的 beans 的属性进行连接。 |
| [byType](https://www.w3cschool.cn/wkspring/8dhy1mmd.html)    | 由属性数据类型自动装配。Spring 容器看到在 XML 配置文件中 bean 的自动装配的属性设置为 byType。然后如果它的**类型**匹配配置文件中的一个确切的 bean 名称，它将尝试匹配和连接属性的类型。如果存在不止一个这样的 bean，则一个致命的异常将会被抛出。 |
| [constructor](https://www.w3cschool.cn/wkspring/jtlb1mmf.html) | 类似于 byType，但该类型适用于构造函数参数类型。如果在容器中没有一个构造函数参数类型的 bean，则一个致命错误将会发生。 |
| autodetect                                                   | Spring首先尝试通过 constructor 使用自动装配来连接，如果它不执行，Spring 尝试通过 byType 来自动装配。 |

# 基于注解的自动配置

| 序号 | 注解 & 描述                                                  |
| ---- | ------------------------------------------------------------ |
| 1    | [@Required](https://www.w3cschool.cn/wkspring/9sle1mmh.html)@Required 注解应用于 bean 属性的 setter 方法。 |
| 2    | [@Autowired](https://www.w3cschool.cn/wkspring/rw2h1mmj.html)@Autowired 注解可以应用到 bean 属性的 setter 方法，非 setter 方法，构造函数和属性。 |
| 3    | [@Qualifier](https://www.w3cschool.cn/wkspring/knqr1mm2.html)通过指定确切的将被连线的 bean，@Autowired 和 @Qualifier 注解可以用来删除混乱。 |

# 基于 Java 的springBean配置

@Configuration用于 标识 这是一个 注解类

@Bean 注解  注入一个bean

@Import 从其他 配置类中导入 配置

声明周期回调：@Bean(initMethod = "init", destroyMethod = "cleanup" )

@Scope  指定 是否单例

# Spring 中的事件处理

* spring通过发布事件来 控制bean生命周期

* 当上下文启动时，ContextStartedEvent 发布，当上下文停止ContextStoppedEvent 发布。

* 通过 ApplicationEvent 类和 ApplicationListener 接口来提供在 ApplicationContext 中处理事件
* 如果一个 bean 实现 ApplicationListener，那么每次 ApplicationEvent 被发布到 ApplicationContext 上，那个 bean 会被通知。

| 序号 | Spring 内置事件 & 描述                                       |
| ---- | ------------------------------------------------------------ |
| 1    | **ContextRefreshedEvent**ApplicationContext 被初始化或刷新时，该事件被发布。这也可以在 ConfigurableApplicationContext 接口中使用 refresh() 方法来发生。 |
| 2    | **ContextStartedEvent**当使用 ConfigurableApplicationContext 接口中的 start() 方法启动 ApplicationContext 时，该事件被发布。你可以调查你的数据库，或者你可以在接受到这个事件后重启任何停止的应用程序。 |
| 3    | **ContextStoppedEvent**当使用 ConfigurableApplicationContext 接口中的 stop() 方法停止 ApplicationContext 时，发布这个事件。你可以在接受到这个事件后做必要的清理的工作。 |
| 4    | **ContextClosedEvent**当使用 ConfigurableApplicationContext 接口中的 close() 方法关闭 ApplicationContext 时，该事件被发布。一个已关闭的上下文到达生命周期末端；它不能被刷新或重启。 |
| 5    | **RequestHandledEvent**这是一个 web-specific 事件，告诉所有 bean HTTP 请求已经被服务。 |

## 监听上下文事件

实现 ApplicationListener 接口的 onApplicationEvent()

## 自定义事件

1. 自定义事件 继承  extends ApplicationEvent

2. 获取事件发布者   implements ApplicationEventPublisherAware，注入ApplicationEventPublisher

3. 自定义事件处理：实现implements ApplicationListener 监听器

   

# SpringAOP 

拦截某个方法 在之前之后添加方法



## AOP 术语

在我们开始使用 AOP 工作之前，让我们熟悉一下 AOP 概念和术语。这些术语并不特定于 Spring，而是与 AOP 有关的。

| 项            | 描述                                                         |
| ------------- | ------------------------------------------------------------ |
| Aspect        | 一个模块具有一组提供横切需求的 APIs。例如，一个日志模块为了记录日志将被 AOP 方面调用。应用程序可以拥有任意数量的方面，这取决于需求。 |
| Join point    | 在你的应用程序中它代表一个点，你可以在插件 AOP 方面。你也能说，它是在实际的应用程序中，其中一个操作将使用 Spring AOP 框架。 |
| Advice        | 这是实际行动之前或之后执行的方法。这是在程序执行期间通过 Spring AOP 框架实际被调用的代码。 |
| Pointcut      | 这是一组一个或多个连接点，通知应该被执行。你可以使用表达式或模式指定切入点正如我们将在 AOP 的例子中看到的。 |
| Introduction  | 引用允许你添加新方法或属性到现有的类中。                     |
| Target object | 被一个或者多个方面所通知的对象，这个对象永远是一个被代理对象。也称为被通知对象。 |
| Weaving       | Weaving 把方面连接到其它的应用程序类型或者对象上，并创建一个被通知的对象。这些可以在编译时，类加载时和运行时完成。 |



## 通知类型

| 通知           | 描述                                                         |
| -------------- | ------------------------------------------------------------ |
| 前置通知       | 在一个方法执行之前，执行通知。                               |
| 后置通知       | 在一个方法执行之后，不考虑其结果，执行通知。                 |
| 返回后通知     | 在一个方法执行之后，只有在方法成功完成时，才能执行通知。     |
| 抛出异常后通知 | 在一个方法执行之后，只有在方法退出抛出异常时，才能执行通知。 |
| 环绕通知       | 在建议方法调用之前和之后，执行通知。                         |

## 两种实现方式

基于XML的配置

基于AspectJ 的 注解

# 基于XML的配置

1. 定义一个config
2. 定义一个 切面
3. 定义一个切入点
4. 定义拦截的方法

```xml
<aop:config>
   <aop:aspect id="myAspect" ref="aBean">
      <aop:pointcut id="businessService" expression="execution(* com.xyz.myapp.service.*.*(..))"/>
      <aop:before pointcut-ref="businessService" 
         method="doRequiredTask"/>
      <!-- an after advice definition -->
      <aop:after pointcut-ref="businessService" 
         method="doRequiredTask"/>
      <!-- an after-returning advice definition -->
      <!--The doRequiredTask method must have parameter named retVal -->
      <aop:after-returning pointcut-ref="businessService"
         returning="retVal"
         method="doRequiredTask"/>
      <!-- an after-throwing advice definition -->
      <!--The doRequiredTask method must have parameter named ex -->
      <aop:after-throwing pointcut-ref="businessService"
         throwing="ex"
         method="doRequiredTask"/>
      <!-- an around advice definition -->
      <aop:around pointcut-ref="businessService" 
         method="doRequiredTask"/>
   ...
   </aop:aspect>
</aop:config>
```

# Spring 中基于 AOP 的 @AspectJ

## @Aspect 

声明bean 为 切面配置类

## @Pointcut

@pointcut("execution(* com.tutorialspoint.*.*(..))")   private void selectAll(){} 

申明方法为 切入点

## @Before("selectAll()")

前置切入



# SpringJDBC

spring提供**JdbcTemplate**  供使用

## 步骤

创建数据源

```xml
<bean id="dataSource"
class="org.springframework.jdbc.datasource.DriverManagerDataSource">
   <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
   <property name="url" value="jdbc:mysql://localhost:3306/TEST"/>
   <property name="username" value="root"/>
   <property name="password" value="password"/>
</bean>

```

执行 SQL 语句

```
String SQL = "select count(*) from Student";
int rowCount = jdbcTemplateObject.queryForInt( SQL );
```

返回long:jdbcTemplateObject.queryForLong

返回字符串：jdbcTemplateObject.queryForObject

返回对象：

```java
String SQL = "select * from Student where id = ?";
Student student = jdbcTemplateObject.queryForObject(SQL, 
                  new Object[]{10}, new StudentMapper());
public class StudentMapper implements RowMapper<Student> {
   public Student mapRow(ResultSet rs, int rowNum) throws SQLException {
      Student student = new Student();
      student.setID(rs.getInt("id"));
      student.setName(rs.getString("name"));
      student.setAge(rs.getInt("age"));
      return student;
   }
}
```

查询并返回多个对象

`List<Student> students = jdbcTemplateObject.query(SQL,                         new StudentMapper());`

执行DML

```java
String SQL = "insert into Student (name, age) values (?, ?)"; jdbcTemplateObject.update( SQL, new Object[]{"Zara", 11} );
```

执行 DDL 语句

```java
String SQL = "CREATE TABLE Student( " +
   "ID   INT NOT NULL AUTO_INCREMENT, " +
   "NAME VARCHAR(20) NOT NULL, " +
   "AGE  INT NOT NULL, " +
   "PRIMARY KEY (ID));"
jdbcTemplateObject.execute( SQL );
```



# Spring 事务管理

事务的概念:ACID

## 编程式 

灵活，维护困难

事务管理者 根据事务定义 获取一个事务

```
TransactionDefinition def = new DefaultTransactionDefinition();
TransactionStatus status = transactionManager.getTransaction(def);
```



## 声明式

基于xml的配置

1. 定义切面
2. 定义事务advice

```xml
 <tx:advice id="txAdvice"  transaction-manager="transactionManager">
      <tx:attributes>
      <tx:method name="create"/>
      </tx:attributes>
   </tx:advice>

   <aop:config>
      <aop:pointcut id="createOperation" 
      expression="execution(* com.tutorialspoint.StudentJDBCTemplate.create(..))"/>
      <aop:advisor advice-ref="txAdvice" pointcut-ref="createOperation"/>
   </aop:config>

   <!-- Initialization for TransactionManager -->
   <bean id="transactionManager"
   class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
      <property name="dataSource"  ref="dataSource" />    
   </bean>

   <!-- Definition for studentJDBCTemplate bean -->
   <bean id="studentJDBCTemplate"  
   class="com.tutorialspoint.StudentJDBCTemplate">
      <property name="dataSource"  ref="dataSource" />  
   </bean>
```



## Spring对事务的抽象

PlatformTransactionManager  接口定义

| 序号 | 方法 & 描述                                                  |
| ---- | ------------------------------------------------------------ |
| 1    | **TransactionStatus getTransaction(TransactionDefinition definition)**根据指定的传播行为，该方法返回当前活动事务或创建一个新的事务。 |
| 2    | **void commit(TransactionStatus status)**该方法提交给定的事务和关于它的状态。 |
| 3    | **void rollback(TransactionStatus status)**该方法执行一个给定事务的回滚。 |

TransactionDefinition  对事务的定义包括：传播行为，隔离等级，名称，超时，是否只读

| 序号 | 方法 & 描述                                                  |
| ---- | ------------------------------------------------------------ |
| 1    | **int getPropagationBehavior()**该方法返回传播行为。Spring 提供了与 EJB CMT 类似的所有的事务传播选项。 |
| 2    | **int getIsolationLevel()**该方法返回该事务独立于其他事务的工作的程度。 |
| 3    | **String getName()**该方法返回该事务的名称。                 |
| 4    | **int getTimeout()**该方法返回以秒为单位的时间间隔，事务必须在该时间间隔内完成。 |
| 5    | **boolean isReadOnly()**该方法返回该事务是否是只读的。       |

隔离级别

| 序号 | 隔离 & 描述                                                  |
| ---- | ------------------------------------------------------------ |
| 1    | **TransactionDefinition.ISOLATION_DEFAULT**这是默认的隔离级别。 |
| 2    | **TransactionDefinition.ISOLATION_READ_COMMITTED**表明能够阻止误读；可以发生不可重复读和虚读。 |
| 3    | **TransactionDefinition.ISOLATION_READ_UNCOMMITTED**表明可以发生误读、不可重复读和虚读。 |
| 4    | **TransactionDefinition.ISOLATION_REPEATABLE_READ**表明能够阻止误读和不可重复读；可以发生虚读。 |
| 5    | **TransactionDefinition.ISOLATION_SERIALIZABLE**表明能够阻止误读、不可重复读和虚读。 |

传播类型的可能值:

| 序号 | 传播 & 描述                                                  |
| ---- | ------------------------------------------------------------ |
| 1    | **TransactionDefinition.PROPAGATION_MANDATORY**支持当前事务；如果不存在当前事务，则抛出一个异常。 |
| 2    | **TransactionDefinition.PROPAGATION_NESTED**如果存在当前事务，则在一个嵌套的事务中执行。 |
| 3    | **TransactionDefinition.PROPAGATION_NEVER**不支持当前事务；如果存在当前事务，则抛出一个异常。 |
| 4    | **TransactionDefinition.PROPAGATION_NOT_SUPPORTED**不支持当前事务；而总是执行非事务性。 |
| 5    | **TransactionDefinition.PROPAGATION_REQUIRED**支持当前事务；如果不存在事务，则创建一个新的事务。 |
| 6    | **TransactionDefinition.PROPAGATION_REQUIRES_NEW**创建一个新事务，如果存在一个事务，则把当前事务挂起。 |
| 7    | **TransactionDefinition.PROPAGATION_SUPPORTS**支持当前事务；如果不存在，则执行非事务性。 |
| 8    | **TransactionDefinition.TIMEOUT_DEFAULT**使用默认超时的底层事务系统，或者如果不支持超时则没有。 |

TransactionStatus  接口

| 1    | **boolean hasSavepoint()**该方法返回该事务内部是否有一个保存点，也就是说，基于一个保存点已经创建了嵌套事务。 |
| ---- | ------------------------------------------------------------ |
| 2    | **boolean isCompleted()**该方法返回该事务是否完成，也就是说，它是否已经提交或回滚。 |
| 3    | **boolean isNewTransaction()**在当前事务时新的情况下，该方法返回 true。 |
| 4    | **boolean isRollbackOnly()**该方法返回该事务是否已标记为 rollback-only。 |
| 5    | **void setRollbackOnly()**该方法设置该事务为 rollback-only 标记。 |

# SpringWebMVC

Spring Web 模型-视图-控制（MVC）框架是围绕 *DispatcherServlet* 设计的

1. DispatchServlet 收到 Http请求后，根据 *HandlerMapping* 来选择并且调用适当的*控制器*
2. 控制器接受请求，调用适当的service，service设置适当的模型数据，返回视图名到DispatchServlet
3. *DispatcherServlet* 会从 *ViewResolver* 获取帮助，为请求检取定义视图
4. 一旦确定视图，*DispatcherServlet* 将把模型数据传递给视图

HandlerMapping、Controller 和 ViewResolver 是 *WebApplicationContext* 的一部分

## HandlerMapping映射配置

DispatchServlet配置在web.xml 中

```
<servlet>
      <servlet-name>HelloWeb</servlet-name>
      <servlet-class>
         org.springframework.web.servlet.DispatcherServlet
      </servlet-class>
      <load-on-startup>1</load-on-startup>
</servlet>
```

该框架将尝试加载位于该应用程序的 *WebContent/WEB-INF* 目录中文件名为 `[servlet-name]-servlet.xml` 的应用程序内容

想要改变默认位置,不使用默认名,配置在web.xml中

```xml
<context-param>
   <param-name>contextConfigLocation</param-name>
   <param-value>/WEB-INF/HelloWeb-servlet.xml</param-value>
</context-param>
<listener>
   <listener-class>
      org.springframework.web.context.ContextLoaderListener
   </listener-class>
</listener>
```

**HelloWeb-servlet.xml** 文件的请求配置

```xml
   <context:component-scan base-package="com.tutorialspoint" />

   <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
      <property name="prefix" value="/WEB-INF/jsp/" />
      <property name="suffix" value=".jsp" />
   </bean>
```

 **HelloWeb-servlet.xml** 文件的一些要点：

* 用于创建 bean 定义，重新定义在全局范围内具有相同名称的任何已定义的 bean
* context:component-scan: 激活 Spring MVC 注释扫描功能，该功能允许使用注释，如 @Controller 和 @RequestMapping
* *InternalResourceViewResolver* :将使用定义的规则来解决视图名称
* 按照上述定义的规则，一个名称为 **hello** 的逻辑视图将发送给位于 `/WEB-INF/jsp/hello.jsp` 中实现的视图

## 定义控制器

**@Controller** 注释表明一个特定类是一个控制器的作用。

**@RequestMapping** 注释用于映射 URL 到整个类或一个特定的处理方法。

## 创建 JSP 视图

Spring MVC 支持许多类型的视图

包括 JSP、HTML、PDF、Excel 工作表、XML、Velocity 模板、XSLT、JSON、Atom 和 RSS 提要、JasperReports 



@ModelAttribute：解析表单变量

重定向：return "redirect:finalPage";

## Web 静态页面

 标签被用来映射静态页面

 `<mvc:resources mapping="/pages/**" location="/WEB-INF/pages/" />`

## 异常处理

```xml
<bean class="org.springframework.web.servlet.handler.
      SimpleMappingExceptionResolver">
   <property name="exceptionMappings">
      <props>
         <prop key="com.tutorialspoint.SpringException">
            ExceptionPage
         </prop>
      </props>
   </property>
   <property name="defaultErrorView" value="error"/>
</bean>

```

${exception}  可以访问异常对象

