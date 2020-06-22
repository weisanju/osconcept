1. 设置超时,代理等配置

```
@Configuration
public class ApiConfig {
    @Bean
    public RestTemplate restTemplate(ClientHttpRequestFactory factory) {
        return new RestTemplate(factory);
    }

    @Bean
    public ClientHttpRequestFactory simpleClientHttpRequestFactory() {
        SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
        factory.setReadTimeout(5000);//单位为ms
        factory.setConnectTimeout(5000);//单位为ms
        return factory;
    }
}
```

2. 编写API 返回对象

```
@ApiModel("用户")
public class User {
    @ApiModelProperty("编号")
    private Long id;

    @ApiModelProperty("用户名")
    private String username;

    @ApiModelProperty("姓")
    private String firstName;

    @ApiModelProperty("名")
    private String lastName;

    @ApiModelProperty("邮箱")
    private String email;

    @ApiModelProperty(hidden = true)// 密码不传输
    @JsonIgnore
    private String password;

    @ApiModelProperty("状态")
    private Integer userStatus;

    // get set

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", email='" + email + '\'' +
                ", password='" + password + '\'' +
                ", userStatus=" + userStatus +
                '}';
    }
}
```

3. 异常实体类

   ```
   package com.itunion.model;
   import java.o.Serializable;
   public class ErrorBody implements Serializable {
       private Integer code;
       private String message;
       private long timestamp = System.currentTimeMillis();
   
       // get set
       @Override
       public String toString() {
           return "ErrorBody{" +
                   "code=" + code +
                   ", message='" + message + '\'' +
                   ", timestamp=" + timestamp +
                   '}';
       }
   }
   ```

   

4. 