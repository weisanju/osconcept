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



1. 
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
*  多个参数 按顺序
*  或者按 类型
*  按 索引值 index

# setter依赖注入

* `<property name="spellChecker" ref="spellChecker"/>`

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