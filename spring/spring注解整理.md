# IOC

## bean加载

| 注解名             | 作用                   |
| ------------------ | ---------------------- |
| Component          | 将对象加入到容器管理   |
| Service            | 将对象加入到容器管理   |
| Repository         | 将对象加入到容器管理   |
| Configuration,Bean | 配置类                 |
| ComponentScan      | 扫描所有 component注解 |

## profile条件加载bean

```
@PropertySource("classpath:/user.properties")
@Configuration
public class MainConfigOfProfile implements EmbeddedValueResolverAware{
	
	@Profile("test")
	@Bean("testUser")
	public User testUser()  {
		User a =new User();
    return a;
	}
	
	@Profile("dev")
	@Bean("devUser")
	public User devUser()  {
		User a =new User();
    return a;
	}
 
}
```



## bean的作用域

@Scope 

bean的作用范围

Singleton 

Protetype 

Request 

Session 

GlobalSession

# DI

## 外部值注入

1. 注入普通字符串 :@Value("normal")
2. 注入操作系统属性 :@Value("#{systemProperties['os.name']}")
3. 注入表达式结果: @Value("#{ T(java.lang.Math).random() * 100.0 }")
4. 注入其他Bean属性：注入beanInject对象的属性another:@Value("#{beanInject.another}")
5. 注入属性对象 : @Value("classpath:com/hry/spring/configinject/config.txt")
6. 注入URL资源: @Value("http://www.baidu.com")

## 属性注入

@PropertySource(value = {"classpath:test.properties"})

## bean注入

| 注解名    | 作用                              |
| --------- | --------------------------------- |
| Autowired | 首先查询类型,如果有多个根据名称找 |
| Resource  | 根据名称注入                      |

## 条件注入

```
@Configuration
public class BeanConfig {
 
    //只有一个类时，大括号可以省略
    //如果WindowsCondition的实现方法返回true，则注入这个bean    
    @Conditional({WindowsCondition.class})
    @Bean(name = "bill")
    public Window window(){
        return new Window();
    }
 
    //如果LinuxCondition的实现方法返回true，则注入这个bean
    @Conditional({LinuxCondition.class})
    @Bean("linux")
    public Linex linux(){
        return new Linex();
    }
}
```



# AOP

| 注解名   | 作用              |
| -------- | ----------------- |
| Aspect   | 注解类上,定义切面 |
| PointCut | 定义切点          |
| After    |                   |
| Before   |                   |
| Around   |                   |

# 异步

## @EnableAsync

## @Async

```
    @Async
    public void startMyTreadTask() {
        System.out.println("this is my async task");
    }
```

# 定时任务

## @EnableScheduling

定时任务注解扫描器，会扫描包体下的所有定时任务

```
@SpringBootApplication
@EnableScheduling //开启定时任务
public class MainApplication {

    public static void main(String[] args) {
        SpringApplication.run(MainApplication.class, args);
    }
}
```

## @Scheduled

```
@Scheduled(cron = "0 0 2 * * ?")　
```
![cron语法](https://i.loli.net/2020/06/26/o5Gi9gdPF4VT3ac.png)



# 缓存

## @EnableCaching

```
@Configuration
@EnableCaching
public class CachingConfig {

    @Bean
    public CacheManager cacheManager() {
        SimpleCacheManager cacheManager = new SimpleCacheManager();
        cacheManager.setCaches(Arrays.asList(new ConcurrentMapCache("sampleCache")));
        return cacheManager;
    }
}
```

## @Cacheable

```
@Cacheable(value = { "sampleCache","sampleCache2" },key="targetClass.getName()+'.'+methodName+'.'+#id")
    public String getUser(int id) {
        if (id == 1) {
            return "1";
        } else {
            return "2";
        }
    }
```



# webmvc

## @RequestMapping

url映射

## @ResponseBody

将controller的方法返回的对象通过适当的转换器转换为指定的格式之后，写入到response对象的body区

## @RequestBody

用来接收前端传递给后端的body中的数据

## @PathVariable

URL路径参数，比如/user/{id}中的id参数

## @RestController

@Controller + @ResponseBody

## @PostMapping

@RequestMapping+POST方法简写

## @RequestHeader 

请求头

## @RequestParam

URL请求参数，比如/user?id=1中的id参数

## web异常处理

@ControllerAdvice + @ExceptionHandler

用于处理controller层面的异常