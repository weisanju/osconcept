IOC容器

*ApplicationContext*是IOC最普遍的容器接口,它提供了实例化,配置,组装bean的功能,它从  基于xml的元数据文件或JavaCode的元数据配置 来完成上述功能

## SETUP

### 配置元数据

* 基于xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="..." class="...">  
        <!-- collaborators and configuration for this bean go here -->
    </bean>

    <bean id="..." class="...">
        <!-- collaborators and configuration for this bean go here -->
    </bean>

    <!-- more bean definitions go here -->

</beans>
```

```xml
<beans>
    <import resource="services.xml"/>
    <import resource="resources/messageSource.xml"/>
    <import resource="/resources/themeSource.xml"/>

    <bean id="bean1" class="..."/>
    <bean id="bean2" class="..."/>
</beans>
```



* 基于javaCode

### 实例化容器

```java
ApplicationContext context = new ClassPathXmlApplicationContext("services.xml", "daos.xml");
//通用容器对象
ApplicationContext context = new GenericGroovyApplicationContext("services.groovy", "daos.groovy");
//加入xmlbean定义
new XmlBeanDefinitionReader(context).loadBeanDefinitions("services.xml", "daos.xml");
context.refresh();
//加入grouvybean定义
new GroovyBeanDefinitionReader(context).loadBeanDefinitions("services.groovy", "daos.groovy");
context.refresh();
```

### 使用容器

```java
// xml容器对象
ApplicationContext context = new ClassPathXmlApplicationContext("services.xml", "daos.xml");
// retrieve configured instance
PetStoreService service = context.getBean("petStore", PetStoreService.class);
```

## BeanDefintion

* bean定义描述了以何种方式创建bean

* 除了从bean定义创建bean,还可以从外部注册bean

  ```java
  getBeanFactory().registerSingleton(..)
  getBeanFactory().registerBeanDefinition(..)
  ```

### bean属性

| Property                 | Explained in…                                                |
| :----------------------- | :----------------------------------------------------------- |
| Class                    | [Instantiating Beans](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-class) |
| Name                     | [Naming Beans](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-beanname) |
| Scope                    | [Bean Scopes](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-scopes) |
| Constructor arguments    | [Dependency Injection](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-collaborators) |
| Properties               | [Dependency Injection](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-collaborators) |
| Autowiring mode          | [Autowiring Collaborators](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-autowire) |
| Lazy initialization mode | [Lazy-initialized Beans](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-lazy-init) |
| Initialization method    | [Initialization Callbacks](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-lifecycle-initializingbean) |
| Destruction method       | [Destruction Callbacks](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-lifecycle-disposablebean) |

### bean别名

id唯一,name可以多个,以 空格,逗号,分号,分隔

```xml
<alias name="myApp-dataSource" alias="subsystemA-dataSource"/>
```

### bean实例化

```xml
构造方法
<bean id="exampleBean" class="examples.ExampleBean"/>
静态工厂
<bean id="clientService"
    class="examples.ClientService"
    factory-method="createInstance"/>
实例工厂
<!-- the factory bean, which contains a method called createInstance() -->
<bean id="serviceLocator" class="examples.DefaultServiceLocator">
    <!-- inject any dependencies required by this locator bean -->
</bean>

<!-- the bean to be created via the factory bean -->
<bean id="clientService"
    factory-bean="serviceLocator"
    factory-method="createClientServiceInstance"/>

```

## Dependency 

### 依赖注入

```
构造注入-引用类型
<bean id="beanOne" class="x.y.ThingOne">
        <constructor-arg ref="beanTwo"/>
        <constructor-arg ref="beanThree"/>
</bean>
构造注入-基本类型
<bean id="exampleBean" class="examples.ExampleBean">
    <constructor-arg type="int" value="7500000"/>
    <constructor-arg type="java.lang.String" value="42"/>
</bean>

构造注入-按索引注入
<bean id="exampleBean" class="examples.ExampleBean">
    <constructor-arg index="0" value="7500000"/>
    <constructor-arg index="1" value="42"/>
</bean>
构造注入-按参数名注入-
前提是 jvm开启Debug选项
可以使用 @ConstructorProperties注解给定参数名
<bean id="exampleBean" class="examples.ExampleBean">
    <constructor-arg name="years" value="7500000"/>
    <constructor-arg name="ultimateAnswer" value="42"/>
</bean>
```

```java
    @ConstructorProperties({"years", "ultimateAnswer"})
    public ExampleBean(int years, String ultimateAnswer) {
        this.years = years;
        this.ultimateAnswer = ultimateAnswer;
    }
```



* setter注入

```xml
<bean id="exampleBean" class="examples.ExampleBean">
    <properties name="ddd" ref="dd"/>
</bean>
```



推荐使用构造注入注入必须的变量, 使用setter注入不是必须的变量

### 值注入

* 字面量

  字符串和基本数据类型

* 集合

   `<list/>`, `<set/>`, `<map/>`, and `<props/>`

  ```xml
  <bean id="moreComplexObject" class="example.ComplexObject">
      <!-- results in a setAdminEmails(java.util.Properties) call -->
      <property name="adminEmails">
          <props>
              <prop key="administrator">administrator@example.org</prop>
              <prop key="support">support@example.org</prop>
              <prop key="development">development@example.org</prop>
          </props>
      </property>
      <!-- results in a setSomeList(java.util.List) call -->
      <property name="someList">
          <list>
              <value>a list element followed by a reference</value>
              <ref bean="myDataSource" />
          </list>
      </property>
      <!-- results in a setSomeMap(java.util.Map) call -->
      <property name="someMap">
          <map>
              <entry key="an entry" value="just some string"/>
              <entry key ="a ref" value-ref="myDataSource"/>
          </map>
      </property>
      <!-- results in a setSomeSet(java.util.Set) call -->
      <property name="someSet">
          <set>
              <value>just some string</value>
              <ref bean="myDataSource" />
          </set>
      </property>
  </bean>
  
  集合合并 merge=true
  <beans>
      <bean id="parent" abstract="true" class="example.ComplexObject">
          <property name="adminEmails">
              <props>
                  <prop key="administrator">administrator@example.com</prop>
                  <prop key="support">support@example.com</prop>
              </props>
          </property>
      </bean>
      <bean id="child" parent="parent">
          <property name="adminEmails">
              <!-- the merge is specified on the child collection definition -->
              <props merge="true">
                  <prop key="sales">sales@example.com</prop>
                  <prop key="support">support@example.co.uk</prop>
              </props>
          </property>
      </bean>
  <beans>
  ```

* 空串与null

  ```xml
  等价于 ""
  <bean class="ExampleBean">
      <property name="email" value=""/>
  </bean>
  
  
  <bean class="ExampleBean">
      <property name="email">
          <null/>
      </property>
  </bean>
  ```

  

### 名称空间注入

```xml
p名称空间
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:p="http://www.springframework.org/schema/p"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
    https://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="myDataSource" class="org.apache.commons.dbcp.BasicDataSource"
        destroy-method="close"
        p:driverClassName="com.mysql.jdbc.Driver"
        p:url="jdbc:mysql://localhost:3306/mydb"
        p:username="root"
        p:password="masterkaoli"/>

</beans>
c名称空间
<!-- c-namespace index declaration -->
<bean id="beanOne" class="x.y.ThingOne" c:_0-ref="beanTwo" c:_1-ref="beanThree"
    c:_2="something@somewhere.com"/>

```

### 复合值注入

```xml
<bean id="something" class="things.ThingOne">
    <property name="fred.bob.sammy" value="123" />
</bean>
```



### properties实例注入

```xml
<bean id="mappings"
    class="org.springframework.context.support.PropertySourcesPlaceholderConfigurer">

    <!-- typed as a java.util.Properties -->
    <property name="properties">
        <value>
            jdbc.driver.className=com.mysql.jdbc.Driver
            jdbc.url=jdbc:mysql://localhost:3306/mydb
        </value>
    </property>
</bean>
```

### *idref*

```xml
避免 值与引用混淆
<!-- in the child (descendant) context -->
<bean id="accountService" <!-- bean name is the same as the parent bean -->
    class="org.springframework.aop.framework.ProxyFactoryBean">
    <property name="target">
        <ref parent="accountService"/> <!-- notice how we refer to the parent bean -->
    </property>
    <!-- insert other configuration and dependencies as required here -->
</bean>
```

### *depends-on*

在某个bean之前实例化,用于两个不直接依赖的bean

```
<bean id="beanOne" class="ExampleBean" depends-on="manager"/>
<bean id="manager" class="ManagerBean" />
```

### Context手动获取

使用场景: 两个bean的生命周期不一致,使用自动注入只会调用一次,

可以使用 getBean(String name)来获得

```java
// a class that uses a stateful Command-style class to perform some processing
package fiona.apple;

// Spring-API imports
import org.springframework.beans.BeansException;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;

public class CommandManager implements ApplicationContextAware {

    private ApplicationContext applicationContext;

    public Object process(Map commandState) {
        // grab a new instance of the appropriate Command
        Command command = createCommand();
        // set the state on the (hopefully brand new) Command instance
        command.setState(commandState);
        return command.execute();
    }

    protected Command createCommand() {
        // notice the Spring API dependency!
        return this.applicationContext.getBean("command", Command.class);
    }

    public void setApplicationContext(
            ApplicationContext applicationContext) throws BeansException {
        this.applicationContext = applicationContext;
    }
}
```

### 抽象方法注入

```xml
<!-- a stateful bean deployed as a prototype (non-singleton) -->
<bean id="myCommand" class="fiona.apple.AsyncCommand" scope="prototype">
    <!-- inject dependencies here as required -->
</bean>

<!-- commandProcessor uses statefulCommandHelper -->
<bean id="commandManager" class="fiona.apple.CommandManager">
    <lookup-method name="createCommand" bean="myCommand"/>
</bean>
```



```java
package fiona.apple;

// no more Spring imports!

public abstract class CommandManager {

    public Object process(Object commandState) {
        // grab a new instance of the appropriate Command interface
        Command command = createCommand();
        // set the state on the (hopefully brand new) Command instance
        command.setState(commandState);
        return command.execute();
    }

    // okay... but where is the implementation of this method?
    protected abstract Command createCommand();
}

或者使用注解
@Lookup("name")
    如果不写名称则根据 方法的返回值类型查找,如果不写名字则需要写具体类名
    
​ Spring的Lookup method inject实现原理的是使用CGLIB动态生成一个类去继承CommandManager，重写createCommand方法。然后根据@Lookup中指定的bean Name或者createCommand方法的返回类型判断需要返回的bean。createCommand可以是abstract和可以不是。因为使用的是继承，所以CommandManager类和createCommand方法都不能是final的。

createCommand方法的签名需要满足如下要求

<public|protected> [abstract] <return-type> theMethodName(no-arguments);
```

### 方法替换

待替换的方法

```java
public class MyValueCalculator {

    public String computeValue(String input) {
        // some real code...
    }

    // some other methods...
}
```

重新实现的方法

```java
public class ReplacementComputeValue implements MethodReplacer {

    public Object reimplement(Object o, Method m, Object[] args) throws Throwable {
        // get the input value, work with it, and return a computed result
        String input = (String) args[0];
        ...
        return ...;
    }
}
```

配置

```
<bean id="myValueCalculator" class="x.y.z.MyValueCalculator">
    <!-- arbitrary method replacement -->
    <replaced-method name="computeValue" replacer="replacementComputeValue">
        <arg-type>String</arg-type>
    </replaced-method>
</bean>

<bean id="replacementComputeValue" class="a.b.c.ReplacementComputeValue"/>
构造参数类型主要是为了区别 重载的方法
只能配置
```

## scope

### 属性列表

| Scope                                                        | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [singleton](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-scopes-singleton) | 单例                                                         |
| [prototype](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-scopes-prototype) | 多例                                                         |
| [request](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-scopes-request) | 每来一个 Http请求中 就会产生一个                             |
| [session](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-scopes-session) | Httpsession                                                  |
| [application](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-scopes-application) | Scopes a single bean definition to the lifecycle of a `ServletContext`. Only valid in the context of a web-aware Spring `ApplicationContext`. |
| [websocket](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/web.html#websocket-stomp-websocket-scope) | Scopes a single bean definition to the lifecycle of a `WebSocket`. Only valid in the context of a web-aware Spring `ApplicationContext`. |

### 生存周期不一致的bean 访问方式

* 单例a依赖注入 prototype的实例b时, 每次访问b, b不会变,就是直接访问,不会去scope中取
* 如果 proxyMode=ScopedProxyMode.TARGET_CLASS 或者*interface*,则 会访问b时 会生成一个代理类,里面根据 scope取值

```
package com.weisanju.javaconfig.config;

import org.springframework.context.annotation.Scope;
import org.springframework.context.annotation.ScopedProxyMode;
import org.springframework.stereotype.Component;

@Component
@Scope(proxyMode=ScopedProxyMode.NO,value = "prototype")
public class MyValueCalculator {
    public String computeValue(String input) {
        System.out.println(input);
        return input;
    }
}
在被注入的时候指定代理形式
```

### 自定义 *scope*

1. 实现 *org.springframework.beans.factory.config.Scope*接口

   基于 时间的作用域

   ```java
   /**
    * 首先自定义作用域范围类TimeScope:
    * Scope接口提供了五个方法，只有get()和remove()是必须实现，get()中写获取逻辑，
    * 如果已有存储中没有该名称的bean，则通过objectFactory.getObject()创建实例。
    */
   @Slf4j
   public class TimeScope implements Scope {
   
       private static Map<String, Map<Integer, Object>> scopeBeanMap = new HashMap<>();
   
       @Override
       public Object get(String name, ObjectFactory<?> objectFactory) {
           Integer hour = Calendar.getInstance().get(Calendar.HOUR_OF_DAY);
           // 当前是一天内的第多少分钟
           Integer minute = hour * 60 + Calendar.getInstance().get(Calendar.MINUTE);
           log.info("当前是第 {} 分钟", minute);
           Map<Integer, Object> objectMap = scopeBeanMap.get(name);
           Object object = null;
           if (Objects.isNull(objectMap)) {
               objectMap = new HashMap<>();
               object = objectFactory.getObject();
               objectMap.put(minute, object);
               scopeBeanMap.put(name, objectMap);
           } else {
               object = objectMap.get(minute);
               if (Objects.isNull(object)) {
                   object = objectFactory.getObject();
                   objectMap.put(minute, object);
                   scopeBeanMap.put(name, objectMap);
               }
           }
           return object;
       }
   
       @Override
       public Object remove(String name) {
           return scopeBeanMap.remove(name);
       }
   
       @Override
       public void registerDestructionCallback(String name, Runnable callback) {
       }
       @Override
       public Object resolveContextualObject(String key) {
           return null;
       }
       @Override
       public String getConversationId() {
           return null;
       }
   }
   ```

   

2. 注册到 *org.springframework.beans.factory.config.CustomScopeConfigurer* 上

   ```java
   @Configuration
   @Slf4j
   public class BeanScopeConfig {
       @Bean
       public CustomScopeConfigurer customScopeConfigurer() {
           CustomScopeConfigurer customScopeConfigurer = new CustomScopeConfigurer();
           Map<String, Object> map = new HashMap<>();
           map.put("timeScope", new TimeScope());
           customScopeConfigurer.setScopes(map);
           return customScopeConfigurer;
       }
       
       @Bean
       @Scope(value = "timeScope", proxyMode = ScopedProxyMode.TARGET_CLASS)
       public TimeScopeBean timeScopeBean() {
           TimeScopeBean timeScopeBean = new TimeScopeBean();
           timeScopeBean.setCurrentTime(System.currentTimeMillis());
           log.info("time scope bean");
           return timeScopeBean;
       }
   }
   ```

   

3. 使用 

   *@Scope(proxyMode=ScopedProxyMode.TARGET_CLASS,value = "thread")*

## 自定义bean的特性

### 三类回调形式

[Lifecycle Callbacks](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-lifecycle) 生命周期回调

[`ApplicationContextAware` and `BeanNameAware`](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-aware) bean注入的回调

[Other `Aware` Interfaces](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#aware-list) 其他的回调接口

### 生命周期回调

#### Bean生命周期回调

* 通过 实现 *InitializingBean* ,*DisposableBean*,*DisposableBean*
* 推荐使用 @PostConstruct` and `@PreDestroy ,这可与 spring特定接口 松耦合
* 或者使用 bean定义 init-method` and `destroy-method 属性

* spring通过 *BeanPostProcessor* 接口 进行回调处理,如果需要自定义可以自行实现
* 被管理的bean可以实现 *Lifecycle* 接口

**Initialization Callbacks**

* 发生于 容器初始完 所有必须的属性时
* 推荐使用 * [`@PostConstruct`](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-postconstruct-and-predestroy-annotations) * 或者使用  Beandefinition 的  init-method` and `destroy-method 或者java注解的@Bean的属性,initMethod

**Destruction Callbacks**

* 类似于上面

**Default Initialization and Destroy Methods**

或者指定全局默认的 init,destroy方法

```
<beans default-init-method="init">

    <bean id="blogService" class="com.something.DefaultBlogService">
        <property name="blogDao" ref="blogDao" />
    </bean>

</beans>
// destroy-method
```

**以上各个 回调实现的组合调用顺序**

Multiple lifecycle mechanisms configured for the same bean, with different initialization methods, are called as follows:

1. Methods annotated with `@PostConstruct`
2. `afterPropertiesSet()` as defined by the `InitializingBean` callback interface
3. A custom configured `init()` method

Destroy methods are called in the same order:

1. Methods annotated with `@PreDestroy`
2. `destroy()` as defined by the `DisposableBean` callback interface
3. A custom configured `destroy()` method

#### Startup and Shutdown Callbacks

* *Lifecycle* 定义了 bean自己的 生命周期

* 容器会在收到 start stop信号后,将调用所有实现了该接口的方法,容器将委托给 *LifecycleProcessor* 去处理

* 只会在显示启动,或者显示停止时调用,要更细粒度的控制, 参照*SmartLifecycle*

  ```
  	Note that the regular org.springframework.context.Lifecycle interface is a plain contract for explicit start and stop notifications and does not imply auto-startup at context refresh time. For fine-grained control over auto-startup of a specific bean (including startup phases), consider implementing org.springframework.context.SmartLifecycle instead.
  
  Also, please note that stop notifications are not guaranteed to come before destruction. On regular shutdown, all Lifecycle beans first receive a stop notification before the general destruction callbacks are being propagated. However, on hot refresh during a context’s lifetime or on aborted refresh attempts, only destroy methods are called.
  ```

* bean 对象 之间的 start,stop决定于 *depends-on* 和显示依赖注入,对于 某一类型 与另一类型的顺序 这 在 *SmartLifecycle* 有实现

  ```java
  public interface Phased {
      int getPhase();
  }
  ```

* 当启动时, 最小的 *phase* 先启动, 关闭时 最大的 phase先关闭

* 对于普通的  “normal” `Lifecycle`  ,他们的 phase为0

* `SmartLifecycle` 的stop方法有回调,所有实现 `SmartLifecycle` 接口的 类 必须在 stop完后 回调该 stop方法

  ```
  	default void stop(Runnable callback) {
  		stop();
  		callback.run();
  	}
  ```

* processor的默认实现 在各个 bean关闭时的 默认超时时间 30s

  ```java
  <bean id="lifecycleProcessor" class="org.springframework.context.support.DefaultLifecycleProcessor">
      <!-- timeout value in milliseconds -->
      <property name="timeoutPerShutdownPhase" value="10000"/>
  </bean>
  ```

* processor还提供了  *onRefresh* 的回调 , 它会判断 `SmartLifecycle`  的isAutoStart 的标志

#### 优雅的关闭非web的容器

* springWebmvc的容器已经实现了该特性

* 在jvm那里 注册一个 钩子回调,实际上是 在jvm那里 注册一个 线程用于关闭

  ```
          ConfigurableApplicationContext ctx = new ClassPathXmlApplicationContext("beans.xml");
  
          // add a shutdown hook for the above context...
          ctx.registerShutdownHook();
          
          
  {
  		if (this.shutdownHook == null) {
  			// No shutdown hook registered yet.
  			this.shutdownHook = new Thread(SHUTDOWN_HOOK_THREAD_NAME) {
  				@Override
  				public void run() {
  					synchronized (startupShutdownMonitor) {
  						doClose();
  					}
  				}
  			};
  			Runtime.getRuntime().addShutdownHook(this.shutdownHook);
  		}
  	}
  ```

  

### `ApplicationContextAware` and `BeanNameAware`

* 用于获取 容器引用或者 bean引用,推荐使用 注解注入

* `BeanNameAware` 回调 迟于 各种属性填充前, 早于 各种初始化回调前

### Other `Aware` Interfaces

| Name                             | Injected Dependency                                          | Explained in…                                                |
| :------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| `ApplicationContextAware`        | Declaring `ApplicationContext`.                              | [`ApplicationContextAware` and `BeanNameAware`](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-aware) |
| `ApplicationEventPublisherAware` | Event publisher of the enclosing `ApplicationContext`.       | [Additional Capabilities of the `ApplicationContext`](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#context-introduction) |
| `BeanClassLoaderAware`           | Class loader used to load the bean classes.                  | [Instantiating Beans](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-class) |
| `BeanFactoryAware`               | Declaring `BeanFactory`.                                     | [`ApplicationContextAware` and `BeanNameAware`](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-aware) |
| `BeanNameAware`                  | Name of the declaring bean.                                  | [`ApplicationContextAware` and `BeanNameAware`](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#beans-factory-aware) |
| `BootstrapContextAware`          | Resource adapter `BootstrapContext` the container runs in. Typically available only in JCA-aware `ApplicationContext` instances. | [JCA CCI](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/integration.html#cci) |
| `LoadTimeWeaverAware`            | Defined weaver for processing class definition at load time. | [Load-time Weaving with AspectJ in the Spring Framework](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#aop-aj-ltw) |
| `MessageSourceAware`             | Configured strategy for resolving messages (with support for parametrization and internationalization). | [Additional Capabilities of the `ApplicationContext`](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#context-introduction) |
| `NotificationPublisherAware`     | Spring JMX notification publisher.                           | [Notifications](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/integration.html#jmx-notifications) |
| `ResourceLoaderAware`            | Configured loader for low-level access to resources.         | [Resources](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/core.html#resources) |
| `ServletConfigAware`             | Current `ServletConfig` the container runs in. Valid only in a web-aware Spring `ApplicationContext`. | [Spring MVC](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/web.html#mvc) |
| `ServletContextAware`            | Current `ServletContext` the container runs in. Valid only in a web-aware Spring `ApplicationContext`. | [Spring MVC](https://docs.spring.io/spring/docs/5.2.7.RELEASE/spring-framework-reference/web.html#mvc) |

## Bean Definition Inheritance

bean定义继承

* bean继承以 子类为准
* 父类可以如果不写 class,必须abstract为true
* bean之间的同名属性必须是 兼容的
* 如果abstract 定义为 true 则该bean定义为模板,不会产生实例

```xml
<bean id="inheritedTestBean" abstract="true"
        class="org.springframework.beans.TestBean">
    <property name="name" value="parent"/>
    <property name="age" value="1"/>
</bean>

<bean id="inheritsWithDifferentClass"
        class="org.springframework.beans.DerivedTestBean"
        parent="inheritedTestBean" init-method="initialize">  
    <property name="name" value="override"/>
    <!-- the age property value of 1 will be inherited from parent -->
</bean>

//不指定class
<bean id="inheritedTestBeanWithoutClass" abstract="true">
    <property name="name" value="parent"/>
    <property name="age" value="1"/>
</bean>

<bean id="inheritsWithClass" class="org.springframework.beans.DerivedTestBean"
        parent="inheritedTestBeanWithoutClass" init-method="initialize">
    <property name="name" value="override"/>
    <!-- age will inherit the value of 1 from the parent bean definition-->
</bean>
```

## Container Extension Points

容器扩展点

spring容器提供各种接口 以供开发人员扩展

### `BeanPostProcessor`

* *BeanPostProcessor*  可以设置任意个
* 通过order属性 排序
* 作用域是 容器中,容器间得另外注册
* *BeanFactoryPostProcessor* 可以改变BeanDefintion
* 回调发生在每个bean对象 创建后, *`InitializingBean.afterPropertiesSet()` or any declared `init` method*  容器初始化完,或者任何申明得初始化方法,在其他bean初始化后
* 它可以对任何 bean采取行动, 一般用于bean的代理
* 容器会根据 配置元数据(xml,或java) 注册 这些 beanpostProcessor  
* beanpostprocessor 的初始化需要早于其他bean的初始化
* 编程方式 注册
  * *ConfigurableBeanFactory.addBeanPostProcessor*通过这个 手动注册,当你有业务逻辑时
  * 不会遵守 order 顺序,注册的顺序决定 执行顺序
  * 调用发生在 自动检测bean之前
* *AOP auto-proxying* 是基于这个接口的 ,所以任何引用该类型的 类都不应该 对其 使用AOP

**Example**

*RequiredAnnotationBeanPostProcessor* 依赖注入时 确保属性的必输项都输入( 现在更推荐 构造器注入)已过期

###  `BeanFactoryPostProcessor`

Customizing Configuration Metadata with a `BeanFactoryPostProcessor`

* 用来修改bean定义本身,这种改变时不可逆的
* 通过实现 *order*接口 来配置  BeanFactoryPostProcessor间的 顺序
* 作用域时容器范围内
* 所有的postProcessor会忽略 懒加载

**Example**

`PropertySourcesPlaceholderConfigurer`

可以使用*PropertySource*替代

* 可以配置多个外部属性配置文件,用来替换  ${}表达式

* 或者手写配置文件

* 如果它失败了则 这时 容器处于 `preInstantiateSingletons()` phase of an `ApplicationContext` for a non-lazy-init bean

  预加载阶段

```xml
<bean class="org.springframework.beans.factory.config.PropertySourcesPlaceholderConfigurer">
    <property name="locations">
        <value>classpath:com/something/strategy.properties</value>
    </property>
    <property name="properties">
        <value>custom.strategy.class=com.something.DefaultStrategy</value>
    </property>
</bean>

<bean id="serviceStrategy" class="${custom.strategy.class}"/>
```

**`PropertyOverrideConfigurer`**

替换 Bean定义的 参数属性

使用标签 :*<context:property-override location="classpath:override.properties"/>*

```
person.name=大师傅似的
beanname.properteis=value
```

```
@Bean
public PropertyOverrideConfigurer propertyOverrideConfigurer(){
    PropertyOverrideConfigurer propertyOverrideConfigurer = new PropertyOverrideConfigurer();
    propertyOverrideConfigurer.setFileEncoding("UTF-8");
    propertyOverrideConfigurer.setLocation(new ClassPathResource("my.properties"));
    return propertyOverrideConfigurer;
}
```

###  `FactoryBean`

Customizing Instantiation Logic with a factoryBean

实现自定义 bean定义 逻辑

## Annotation-based Container Configuration

* 基于注解的注入 比XML 注入更早执行,所以xml的注入会覆盖注解的注入
* 基于注解的注入实际上是 一个个beanPostProcessor
* 隐式注册这些beanPostProcessor :  <context:annotation-config/>
  *  [`AutowiredAnnotationBeanPostProcessor`](https://docs.spring.io/spring-framework/docs/5.2.7.RELEASE/javadoc-api/org/springframework/beans/factory/annotation/AutowiredAnnotationBeanPostProcessor.html)
  * [`CommonAnnotationBeanPostProcessor`](https://docs.spring.io/spring-framework/docs/5.2.7.RELEASE/javadoc-api/org/springframework/context/annotation/CommonAnnotationBeanPostProcessor.html)
  * [`PersistenceAnnotationBeanPostProcessor`](https://docs.spring.io/spring-framework/docs/5.2.7.RELEASE/javadoc-api/org/springframework/orm/jpa/support/PersistenceAnnotationBeanPostProcessor.html) 
  * [`RequiredAnnotationBeanPostProcessor`](https://docs.spring.io/spring-framework/docs/5.2.7.RELEASE/javadoc-api/org/springframework/beans/factory/annotation/RequiredAnnotationBeanPostProcessor.html)

### 	@Required

标识该setter方法的注入必须, 已过期,推荐使用构造器注入

```
public class SimpleMovieLister {

    private MovieFinder movieFinder;

    @Required
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }

    // ...
}
```

### @Autowired

构造方法上(当 只有一个构造方法时,不是很必要)

```java
public class MovieRecommender {

    private final CustomerPreferenceDao customerPreferenceDao;

    @Autowired
    public MovieRecommender(CustomerPreferenceDao customerPreferenceDao) {
        this.customerPreferenceDao = customerPreferenceDao;
    }
}
```

setter注入

```
public class SimpleMovieLister {

    private MovieFinder movieFinder;

    @Autowired
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }

    // ...
}
```

字段注入

```java
 @Autowired
    private MovieCatalog movieCatalog;
```

可以注入某一类Bean

可以@Order或者order接口,实现注入的排序,否则顺序以注册顺序为准,@Order也会影响依赖注入顺序

```java
public class MovieRecommender {
    @Autowired
    private MovieCatalog[] movieCatalogs;
}
public class MovieRecommender {
    private Set<MovieCatalog> movieCatalogs;
    @Autowired
    public void setMovieCatalogs(Set<MovieCatalog> movieCatalogs) {
        this.movieCatalogs = movieCatalogs;
    }
}
```

Map注入

这回注入所有 beanname,和某一类型的bean

```java
public class MovieRecommender {
    private Map<String, MovieCatalog> movieCatalogs;
    @Autowired
    public void setMovieCatalogs(Map<String, MovieCatalog> movieCatalogs) {
        this.movieCatalogs = movieCatalogs;
    }
}
```

可以不启用

```
public class SimpleMovieLister {
    private MovieFinder movieFinder;
    @Autowired(required = false)
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }
}
```

注入Optional类

```java
public class SimpleMovieLister {
    @Autowired
    public void setMovieFinder(Optional<MovieFinder> movieFinder) {
    }
}
```

可以使用@nullable

```java
    @Autowired
    public void setMovieFinder(@Nullable MovieFinder movieFinder) {
        ...
    }
```

可以注入spring相关的bean

```
BeanFactory, ApplicationContext, Environment, ResourceLoader, ApplicationEventPublisher, and MessageSource
ConfigurableApplicationContext or ResourcePatternResolver
public class MovieRecommender {

    @Autowired
    private ApplicationContext context;

    public MovieRecommender() {
    }
}
```

**注意事项**

* 一个bean可能有多个 构造器, 但只有一个 构造器能 @Autowired(required = true),其他的必须是false
* 通过 匹配容器中的bean 满足依赖关系最多的 构造器 将会被使用,如果都不满足 使用默认构造器
* '@Autowired`, `@Inject`, `@Value`, and `@Resource' 这些注入 不能用于BeanPostProcessor或者BeanFactoryPostProcessor

### @Primary

* 通过类型注册可能有多个类型的候选者,可以使用primary指定

```java
@Configuration
public class MovieConfiguration {

    @Bean
    @Primary
    public MovieCatalog firstMovieCatalog() { ... }

    @Bean
    public MovieCatalog secondMovieCatalog() { ... }

    // ...
}
```

xml配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd">

    <context:annotation-config/>

    <bean class="example.SimpleMovieCatalog" primary="true">
        <!-- inject any dependencies required by this bean -->
    </bean>

    <bean class="example.SimpleMovieCatalog">
        <!-- inject any dependencies required by this bean -->
    </bean>

    <bean id="movieRecommender" class="example.MovieRecommender"/>

</beans>
```

### @Qualifiers

* 与id不同,类似于 手动给定bean分类, 类似于某种bean的过滤器

* 这在注入 集合类的时候 作用尤为明显 `Set<MovieCatalog>`
* 如果没有其他指示器(类似primary,qualifier) ,而且存在多个候选者,则spring会根据 注入字段名或参数名匹配bean
* 如果你想通过bean名匹配,最好使用@Resource, @Autowired的语义是:先找同类型的,然后寻找指定的Qualifer
* 可以通过@Resource引用集合
* qualifier可以自引用,但顺序是最后的

```java
public class MovieRecommender {

    @Autowired
    @Qualifier("main")
    private MovieCatalog movieCatalog;

    // ...
}


public class MovieRecommender {

    private MovieCatalog movieCatalog;

    private CustomerPreferenceDao customerPreferenceDao;

    @Autowired
    public void prepare(@Qualifier("main") MovieCatalog movieCatalog,
            CustomerPreferenceDao customerPreferenceDao) {
        this.movieCatalog = movieCatalog;
        this.customerPreferenceDao = customerPreferenceDao;
    }

    // ...
}
```

xml配置

```hxml
 <bean class="example.SimpleMovieCatalog">
        <qualifier value="main"/> 

        <!-- inject any dependencies required by this bean -->
    </bean>
```

**创建自己的qualifier注解**,给qualifier分类

```java
@Target({ElementType.FIELD, ElementType.PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
@Qualifier
public @interface Genre {

    String value();
}
```

使用注解

```java
public class MovieRecommender {

    @Autowired
    @Genre("Action")
    private MovieCatalog actionCatalog;

    private MovieCatalog comedyCatalog;

    @Autowired
    public void setComedyCatalog(@Genre("Comedy") MovieCatalog comedyCatalog) {
        this.comedyCatalog = comedyCatalog;
    }

    // ...
}
```

可以使用短类名,或者全限定类名

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd">

    <context:annotation-config/>

    <bean class="example.SimpleMovieCatalog">
        <qualifier type="Genre" value="Action"/>
        <!-- inject any dependencies required by this bean -->
    </bean>

    <bean class="example.SimpleMovieCatalog">
        <qualifier type="example.Genre" value="Comedy"/>
        <!-- inject any dependencies required by this bean -->
    </bean>

    <bean id="movieRecommender" class="example.MovieRecommender"/>

</beans>
```

给qualifier添加类别,属性

```java
@Target({ElementType.FIELD, ElementType.PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
@Qualifier
public @interface MovieQualifier {

    String genre();

    Format format();
}
public enum Format {
    VHS, DVD, BLURAY
}
```

按照分类注入

```java
public class MovieRecommender {

    @Autowired
    @MovieQualifier(format=Format.VHS, genre="Action")
    private MovieCatalog actionVhsCatalog;

    @Autowired
    @MovieQualifier(format=Format.VHS, genre="Comedy")
    private MovieCatalog comedyVhsCatalog;

    @Autowired
    @MovieQualifier(format=Format.DVD, genre="Action")
    private MovieCatalog actionDvdCatalog;

    @Autowired
    @MovieQualifier(format=Format.BLURAY, genre="Comedy")
    private MovieCatalog comedyBluRayCatalog;

    // ...
}
```

同样可以使用meta标签 简写 qualifier标签,会自动查找该qualifier的值

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd">

    <context:annotation-config/>

    <bean class="example.SimpleMovieCatalog">
        <qualifier type="MovieQualifier">
            <attribute key="format" value="VHS"/>
            <attribute key="genre" value="Action"/>
        </qualifier>
        <!-- inject any dependencies required by this bean -->
    </bean>

    <bean class="example.SimpleMovieCatalog">
        <qualifier type="MovieQualifier">
            <attribute key="format" value="VHS"/>
            <attribute key="genre" value="Comedy"/>
        </qualifier>
        <!-- inject any dependencies required by this bean -->
    </bean>

    <bean class="example.SimpleMovieCatalog">
        <meta key="format" value="DVD"/>
        <meta key="genre" value="Action"/>
        <!-- inject any dependencies required by this bean -->
    </bean>

    <bean class="example.SimpleMovieCatalog">
        <meta key="format" value="BLURAY"/>
        <meta key="genre" value="Comedy"/>
        <!-- inject any dependencies required by this bean -->
    </bean>

</beans>
```

### Using Generics

使用泛型自动注入

假设下面的类 实现了 某个泛型接口

```j
Store<String>` and `Store<Integer>
```



```java
@Configuration
public class MyConfiguration {

    @Bean
    public StringStore stringStore() {
        return new StringStore();
    }

    @Bean
    public IntegerStore integerStore() {
        return new IntegerStore();
    }
}


@Autowired
private Store<String> s1; // <String> qualifier, injects the stringStore bean

@Autowired
private Store<Integer> s2; // <Integer> qualifier, injects the integerStore bean
```

泛型同样支持 集合类

```java
@Autowired
private List<Store<Integer>> s;
```

### CustomAutowireConfigurer

*`CustomAutowireConfigurer` 是一个 BeanFactoryPostProcessor*  可以让你注册自己的 qualifier

xml配置

```xml
<bean id="customAutowireConfigurer"
        class="org.springframework.beans.factory.annotation.CustomAutowireConfigurer">
    <property name="customQualifierTypes">
        <set>
            <value>example.CustomQualifier</value>
        </set>
    </property>
</bean>
```

*AutowireCandidateResolver* (QualifierAnnotationAutowireCandidateResolver)选取候选者的方式

* autowire-candidate 每一个bean的 自动注入候选者
* 在`<beans>`中的 default-autowire-candidates
* @qualifier的限定类
* CustomAutowireConfigurer 中的候选类

### @Resource

* 如果没有指定名字 取 方法参数名或者 字段名
* 名称是由 ApplicationContext 提供查找(由CommonAnnotationBeanPostProcessor 注入)

### @Value

注入外部属性

```java
@Component
public class MovieRecommender {

    private final String catalog;

    public MovieRecommender(@Value("${catalog.name}") String catalog) {
        this.catalog = catalog;
    }
}

@Configuration
@PropertySource("classpath:application.properties")
public class AppConfig { }

catalog.name=MovieCatalog
```

如果想要严格控制 不存在的值可以如下申明

```java
@Configuration
public class AppConfig {

     @Bean
     public static PropertySourcesPlaceholderConfigurer propertyPlaceholderConfigurer() {
           return new PropertySourcesPlaceholderConfigurer();
     }
}

```

* 当配置这个JavaConfig Bean时,必须是static
* 可以设置前缀后缀 分隔符,setPlaceholderPrefix`, `setPlaceholderSuffix`, or `setValueSeparator
* *PropertySourcesPlaceholderConfigurer* springboot自动带一个,会从 application.properties` and `application.yml解析

* 值转换的过程 可以自定义ConversionService

  ```java
  @Configuration
  public class AppConfig {
  
      @Bean
      public ConversionService conversionService() {
          DefaultFormattingConversionService conversionService = new DefaultFormattingConversionService();
          conversionService.addConverter(new MyCustomConverter());
          return conversionService;
      }
  }
  ```

* 支持 EL表达式

  ```java
  @Component
  public class MovieRecommender {
  
      private final String catalog;
  
      public MovieRecommender(@Value("#{systemProperties['user.catalog'] + 'Catalog' }") String catalog) {
          this.catalog = catalog;
      }
  }
  
  @Component
  public class MovieRecommender {
  
      private final Map<String, Integer> countOfMoviesPerCatalog;
  
      public MovieRecommender(
              @Value("#{{'Thriller': 100, 'Comedy': 300}}") Map<String, Integer> countOfMoviesPerCatalog) {
          this.countOfMoviesPerCatalog = countOfMoviesPerCatalog;
      }
  }
  ```

### @PostConstruct @PreDestroy

* 这两个注解也是 *CommonAnnotationBeanPostProcessor* 实现的
*  `@Resource`, the `@PostConstruct` and `@PreDestroy`  这个在 java9被移包,在11被分离需要手动引入javax.annotation-api



## 类路径扫描,容器管理

### Component

模板注解,@Repository`, `@Service`, and `@Controller是 它的特例,目前没有什么区别,以后可能会增加区别

### 使用元注解或组合注解

元注解

```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Component 
public @interface Service {

    // ...
}

Component 导致 service 跟 component同样对待
```

组合注解

@RestController等价于 @Controller` and `@ResponseBody

元注解可以重新申明 属性自定义属性的值

```java
@Target({ElementType.TYPE, ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Scope(WebApplicationContext.SCOPE_SESSION)
public @interface SessionScope {

    /**
     * Alias for {@link Scope#proxyMode}.
     * <p>Defaults to {@link ScopedProxyMode#TARGET_CLASS}.
     */
    @AliasFor(annotation = Scope.class)
    ScopedProxyMode proxyMode() default ScopedProxyMode.TARGET_CLASS;

}

@Service
@SessionScope
public class SessionScopedService {
    // ...
}
```

### 自动注册bean定义

spring会自动注册带有 模板注解component的类,并生成相应的bean定义 在applicationContext中

```java
@Service
public class SimpleMovieLister {

    private MovieFinder movieFinder;

    public SimpleMovieLister(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }
}
```

为了自动注册上面的类型必须 要在 带有 @Configuration的 类中 申明 ,包扫描,包之间可以用 空格, 逗号,冒号

```java
@Configuration
@ComponentScan(basePackages = "org.example")
public class AppConfig  {
    // ...
}

//@ComponentScan("org.example")简写形式

//xml 形式
 <context:component-scan base-package="org.example"/>
 它会激活 <context:annotation-config>注解
```

使用Ant编译工程时, you do not activate the files-only switch of the JAR task

同时 AutowiredAnnotationBeanPostProcessor` and `CommonAnnotationBeanPostProcessor这两个beanPostProcessor也会被注册

```
You can disable the registration of AutowiredAnnotationBeanPostProcessor and CommonAnnotationBeanPostProcessor by including the annotation-config attribute with a value of false.
```

### 使用过滤器 自定义扫描

* '@Component`, `@Repository`, `@Service`, `@Controller`, `@Configuration'默认只扫描带有这些注解的类 

* 通过ComponentScan的 includeFilters ,excludeFilters 属性 设定不同类型的过滤器去 取 或者排除 相应的类

* 过滤器的类型

  | ilter Type           | Example Expression           | Description                                                  |
  | :------------------- | :--------------------------- | :----------------------------------------------------------- |
  | annotation (default) | `org.example.SomeAnnotation` | 指定  注释类上或者元类上的注解类                             |
  | assignable           | `org.example.SomeClass`      | A class (or interface) that the target components are assignable to (extend or implement). |
  | aspectj              | `org.example..*Service+`     | 使用 aspectj注入语法                                         |
  | regex                | `org\.example\.Default.*`    | 使用正则匹配类全限定名                                       |
  | custom               | `org.example.MyTypeFilter`   | A custom implementation of the `org.springframework.core.type.TypeFilter` interface. |

* 使用

  ```java
  @Configuration
  @ComponentScan(basePackages = "org.example",
          includeFilters = @Filter(type = FilterType.REGEX, pattern = ".*Stub.*Repository"),
          excludeFilters = @Filter(Repository.class))
  public class AppConfig {
      ...
  }
  ```

  ```xml
  <beans>
      <context:component-scan base-package="org.example">
          <context:include-filter type="regex"
                  expression=".*Stub.*Repository"/>
          <context:exclude-filter type="annotation"
                  expression="org.springframework.stereotype.Repository"/>
      </context:component-scan>
  </beans>
  
  ```

  

* 'useDefaultFilters=false use-default-filters="false"' 可以使得系统不会自动 *`@Component`, `@Repository`, `@Service`, `@Controller`, `@RestController`, or `@Configuration`.* 扫描这些注解

### 使用component定义元数据

* 可以使用component定义元数据
* 方法级别的bean定义,类似于 提供一个工厂方法

```java
@Component
public class FactoryMethodComponent {

    @Bean
    @Qualifier("public")
    public TestBean publicInstance() {
        return new TestBean("publicInstance");
    }

    public void doWork() {
        // Component method implementation omitted
    }
}
```

```java
@Component
public class FactoryMethodComponent {

    private static int i;

    @Bean
    @Qualifier("public")
    public TestBean publicInstance() {
        return new TestBean("publicInstance");
    }

    // use of a custom qualifier and autowiring of method parameters
    @Bean
    protected TestBean protectedInstance(
            @Qualifier("public") TestBean spouse,
            @Value("#{privateInstance.age}") String country) {
        TestBean tb = new TestBean("protectedInstance", 1);
        tb.setSpouse(spouse);
        tb.setCountry(country);
        return tb;
    }

    @Bean
    private TestBean privateInstance() {
        return new TestBean("privateInstance", i++);
    }

    @Bean
    @RequestScope
    public TestBean requestScopedInstance() {
        return new TestBean("requestScopedInstance", 3);
    }
}
```

```java
@Component
public class FactoryMethodComponent {

    @Bean @Scope("prototype")
    public TestBean prototypeInstance(InjectionPoint injectionPoint) {
        return new TestBean("prototypeInstance for " + injectionPoint.getMember());
    }
}
```

As of Spring Framework 4.3,可以使用 InjectionPoint(DependencyDescriptor更详细的子类) 可以访问到请求注入点,当然这适用于 原型作用域,

* 在普通 component的 @bean与 @configuration的@Bean不同
  * configuration 中 cglib会对其增强, 参与到spring容器的生命周期来
  * component 没有其他语义