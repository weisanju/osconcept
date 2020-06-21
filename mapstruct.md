# MapStruct介绍

* mapStructut是一个基于注解的,用来生成类型安全的bean映射类
* 在编译时期Mapstruct会生成接口的实现,基于普通的方法调用,没有反射

* 主要包含了两个组件
  * *org.mapstruct:mapstruct*: 注解
  * *org.mapstruct:mapstruct-processor*: 生成实现类的处理器

# 使用方式

## *Maven configuration*

```
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.8.1</version>
<configuration>
        <source>1.8</source>
        <target>1.8</target>
        <annotationProcessorPaths>
            <path>
                <groupId>org.mapstruct</groupId>
                <artifactId>mapstruct-processor</artifactId>
                <version>${org.mapstruct.version}</version>
            </path>
        </annotationProcessorPaths>
    </configuration>
</plugin>
```

## 简介

1. @Mapper 定义在要生成代码的 接口

2. @Mapping 定义在方法上,标识如何转换

   1. 可以有多个@Mapping

   ```
   @Mapping(source = "numberOfSeats", target = "seatCount")
   ```

3. 转换的类要符合JavaBean定义

4. 首先根据 注解匹配,然后自动 根据 类型和名称 匹配

5. 支持链式调用

6. @BeanMapping(ignoreByDefault = true) 不会自动匹配,只能显示指定

7. 如果源类型与 目标类型 不同,会进行隐式转换,或者调用或者创建另一个映射方法,且他们不是 集合类型

8. mapstruct考虑了 源和目标的所有公共属性,也包括他们的父类

## Mapping Composition (experimental)

组合注解:用来处理 多个不同种类的bean可能存在 相同的字段

```
定义在注解上
@Retention(RetentionPolicy.CLASS)
@Mapping(target = "id", ignore = true)
@Mapping(target = "creationDate", expression = "java(new java.util.Date())")
@Mapping(target = "name", source = "groupName")
public @interface ToEntity { }

使用定义的注解
@Mapper
public interface StorageMapper {

    StorageMapper INSTANCE = Mappers.getMapper( StorageMapper.class );

    @ToEntity
    @Mapping( target = "weightLimit", source = "maxWeight")
    ShelveEntity map(ShelveDto source);

    @ToEntity
    @Mapping( target = "label", source = "designation")
    BoxEntity map(BoxDto source);
}

```



## 增加自定义方法

### 使用接口默认方法

```
@Mapper
public interface CarMapper {

    @Mapping(...)
    ...
    CarDto carToCarDto(Car car);

    default PersonDto personToPersonDto(Person person) {
        //hand-written mapping logic
    }
}
```

### 使用抽象类继承

```
@Mapper
public abstract class CarMapper {

    @Mapping(...)
    ...
    public abstract CarDto carToCarDto(Car car);

    public PersonDto personToPersonDto(Person person) {
        //hand-written mapping logic
    }
}
```

## 来自多源

如果多源中字段名有歧义就会报错

```
@Mapper
public interface AddressMapper {

    @Mapping(source = "person.description", target = "description")
    @Mapping(source = "address.houseNo", target = "houseNumber")
    DeliveryAddressDto personAndAddressToDeliveryAddressDto(Person person, Address address);
}
```

## 嵌套的bean属性处理

使用. 表明 将 record对象中所有的属性映射到target

```
@Mapper
 public interface CustomerMapper {

     @Mapping( target = "name", source = "record.name" )
     @Mapping( target = ".", source = "record" )
     @Mapping( target = ".", source = "account" )
     Customer customerDtoToCustomer(CustomerDto customerDto);
 }
```

## 更新使用 源类型 更新目标类型

```
@Mapper
public interface CarMapper {

    void updateCarFromDto(CarDto carDto, @MappingTarget Car car);
}
```



## 直接字段访问映射

支持 public的 字段,没有getter,setter

```
    @InheritInverseConfiguration
    CustomerDto fromCustomer(Customer customer);
```

## 使用构建器



