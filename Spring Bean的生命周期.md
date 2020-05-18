# springBean内部生命周期

1. 工厂后处理接口

   BeanFactoryPostProcessor

2. 初步实例化

   调用构造

   注入值

3. 注入bean名调用

   BeanNameAware接口

4. 注入BeanFactory

   BeanFactoryAware

5. 初始化前

   调用 BeanPostProcessor->before

6. bean的所有属性均已被设置之后

   调用InitializingBean->afterPropertiesSet

7. 调用init-method

8. 初始化后

   调用 BeanPostProcessor->after

9. 调用销毁接口

   DiposibleBean接口

10. 调用destroy-method



实例化之前：修改bean定义

通过BeanFactoryPostProcessor接口，可以自定义，有以下实现

* AspectJWeavingEnabler,
* ConfigurationClassPostProcessor
*  CustomAutowireConfigurer

实例化bean

* 调用构造
* 调用setter属性注入
* 注入其他属性 XXXAware
  * beanName
  * beanFactory
* 属性注入完毕之后，调用bean后置处理器 初始化前