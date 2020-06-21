# maven设置多环境

```
<profiles>
    <profile>
        <!--本地开发环境-->
        <id>dev</id>
        <properties>
            <package.environment>dev</package.environment>
        </properties>
        <activation>
            <activeByDefault>true</activeByDefault>
        </activation>
    </profile>
    <profile>
        <!--tb环境-->
        <id>tb</id>
        <properties>
            <package.environment>tb</package.environment>
        </properties>
    </profile>
</profiles>
```



# *maven*配置 *mybatis*  逆向工程

```
<finalName>ase</finalName>
<plugin>
                <groupId>org.mybatis.generator</groupId>
                <artifactId>mybatis-generator-maven-plugin</artifactId>
                <version>1.3.2</version>
                   <configuration>
                    <configurationFile>src/main/resources/generatorConfig.xml</configurationFile>
                    <verbose>true</verbose>
                    <overwrite>true</overwrite>
                </configuration>

                <dependencies>
                    <dependency>
                        <groupId>org.mybatis.generator</groupId>
                        <artifactId>mybatis-generator-core</artifactId>
                        <version>1.3.2</version>
                    </dependency>
                    <dependency>
                        <groupId>mysql</groupId>
                        <artifactId>mysql-connector-java</artifactId>
                        <version>${mysql-connector-java.version}</version><!--$NO-MVN-MAN-VER$-->
                    </dependency>
                </dependencies>
</plugin>
```

不要压制所有注释

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE generatorConfiguration
        PUBLIC "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"
        "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd">


<generatorConfiguration>
    <!--导入属性配置-->
    <properties resource="db.properties"/>




    <!--指定特定数据库的jdbc驱动jar包的位置-->
    <!-- 暂时不清楚怎么指定相对路径，只能指定maven仓库中的jar包 -->
    <!--<classPathEntry location="C:\DevelopmentKit\maven_repository\mysql\mysql-connector-java\5.1.32\mysql-connector-java-5.1.32.jar"/>-->

    <context id="default" targetRuntime="MyBatis3">

        <plugin type="org.mybatis.generator.plugins.ToStringPlugin"></plugin>
        <!-- optional，旨在创建class时，对注释进行控制 -->
        <commentGenerator>
            <property name="suppressDate" value="true"/>
           <!-- <property name="suppressAllComments" value="true"/>-->
            <property name="javaFileEncoding" value="UTF-8"/>
        </commentGenerator>

        <!--jdbc的数据库连接，直接写死也可以 -->
        <jdbcConnection
                driverClass="${jdbc.driverClass}"
                connectionURL="${jdbc.url}"
                userId="${jdbc.username}"
                password="${jdbc.password}"
        >
        </jdbcConnection>

        <!-- 非必需，类型处理器，在数据库类型和java类型之间的转换控制-->
        <javaTypeResolver>
            <property name="forceBigDecimals" value="false"/>
        </javaTypeResolver>


        <!-- Model模型生成器,用来生成含有主键key的类，记录类 以及查询Example类
            targetPackage     指定生成的model生成所在的包名
            targetProject     指定在该项目下所在的路径
        -->
        <javaModelGenerator targetPackage="mapper.entity" targetProject="src/main/java">
            <!-- 是否允许子包，即targetPackage.schemaName.tableName -->
            <property name="enableSubPackages" value="false"/>
            <!-- 是否对model添加 构造函数 -->
            <property name="constructorBased" value="false"/>
            <!-- 建立的Model对象是否 不可改变  即生成的Model对象不会有 setter方法，只有构造方法 -->
            <property name="immutable" value="false"/>
            <!-- 设置是否在getter方法中，对String类型字段调用trim()方法 -->
            <property name="trimStrings" value="false"/>
        </javaModelGenerator>

        <!--mapper映射文件生成所在的目录 为每一个数据库的表生成对应的SqlMap文件 -->
        <sqlMapGenerator targetPackage="mapper" targetProject="src/main/resources">
            <property name="enableSubPackages" value="false"/>
        </sqlMapGenerator>

        <!-- 客户端代码，生成易于使用的针对Model对象和XML配置文件 的代码
                type="ANNOTATEDMAPPER",生成Java Model 和基于注解的Mapper对象
                type="MIXEDMAPPER",生成基于注解的Java Model 和相应的Mapper对象
                type="XMLMAPPER",生成SQLMap XML文件和独立的Mapper接口
        -->

        <!-- targetPackage：mapper接口dao生成的位置 -->
        <javaClientGenerator type="XMLMAPPER" targetPackage="mapper.xml" targetProject="src/main/java">
            <!-- enableSubPackages:是否让schema作为包的后缀 -->
            <property name="enableSubPackages" value="false" />
        </javaClientGenerator>


        <table  tableName="company"
               domainObjectName="Company"
               enableCountByExample="true"
               enableUpdateByExample="true"
               enableDeleteByExample="true"
               enableSelectByExample="true"
               selectByExampleQueryId="true">
            <!-- 上面的属性都可以使用子标签形式表示 -->
            <!-- 是否使用真实字段名，设置为false将自动驼峰转换 -->
            <property name="useActualColumnNames" value="false" />
            <!-- 还可以对表中的字段进行类型转换 -->
            <!-- 这里转换的原因是会自动将个位的int值自动转化为Boolean，所以指定为Integer -->
         <!--   <columnOverride column="sex" javaType="Integer"/>-->
        </table>
<!--
        <table tableName="tb_item" domainObjectName="Item" enableCountByExample="false" enableUpdateByExample="false" enableDeleteByExample="false" enableSelectByExample="false" selectByExampleQueryId="false"></table>
        <table tableName="tb_order" domainObjectName="Order" enableCountByExample="false" enableUpdateByExample="false" enableDeleteByExample="false" enableSelectByExample="false" selectByExampleQueryId="false"></table>
        <table tableName="tb_orderdetail" domainObjectName="OrderDetail" enableCountByExample="false" enableUpdateByExample="false" enableDeleteByExample="false" enableSelectByExample="false" selectByExampleQueryId="false"></table>

-->

        <!-- geelynote mybatis插件的搭建 -->
    </context>
</generatorConfiguration>
```



# *maven*配置 lib依赖 配置 与包分离

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.example</groupId>
    <artifactId>dispatch</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <dependency>
            <groupId>org.mybatis.generator</groupId>
            <artifactId>mybatis-generator-core</artifactId>
            <version>1.3.2</version>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <!--打包jar-->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <configuration>
                    <!--不打包资源文件-->
                    <excludes>
                        <exclude>*.**</exclude>
                        <exclude>*/*.xml</exclude>
                    </excludes>
                    <archive>
                        <manifest>
                            <addClasspath>true</addClasspath>
                            <!--MANIFEST.MF 中 Class-Path 加入前缀-->
                            <classpathPrefix>lib/</classpathPrefix>
                            <!--jar包不包含唯一版本标识-->
                            <useUniqueVersions>false</useUniqueVersions>
                            <!--指定入口类-->
                            <mainClass>Demo</mainClass>
                        </manifest>
                        <manifestEntries>
                            <!--MANIFEST.MF 中 Class-Path 加入资源文件目录-->
                            <Class-Path>./resources/</Class-Path>
                        </manifestEntries>
                    </archive>
                    <outputDirectory>${project.build.directory}</outputDirectory>
                </configuration>
            </plugin>

            <!--拷贝依赖 copy-dependencies-->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-dependency-plugin</artifactId>
                <executions>
                    <execution>
                        <id>copy-dependencies</id>
                        <phase>package</phase>
                        <goals>
                            <goal>copy-dependencies</goal>
                        </goals>
                        <configuration>
                            <outputDirectory>
                                ${project.build.directory}/lib/
                            </outputDirectory>
                        </configuration>
                    </execution>
                </executions>
            </plugin>

            <!--拷贝资源文件 copy-resources-->
            <plugin>
                <artifactId>maven-resources-plugin</artifactId>
                <executions>
                    <execution>
                        <id>copy-resources</id>
                        <phase>package</phase>
                        <goals>
                            <goal>copy-resources</goal>
                        </goals>
                        <configuration>
                            <resources>
                                <resource>
                                    <!--<directory>src/main/resources</directory>-->
                                    <directory>config</directory>
                                </resource>
                            </resources>
                            <outputDirectory>${project.build.directory}/config</outputDirectory>
                        </configuration>
                    </execution>
                </executions>
            </plugin>

            <!--spring boot repackage，依赖 maven-jar-plugin 打包的jar包 重新打包成 spring boot 的jar包-->
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <!--重写包含依赖，包含不存在的依赖，jar里没有pom里的依赖-->
                    <includes>
                        <include>
                            <groupId>null</groupId>
                            <artifactId>null</artifactId>
                        </include>
                    </includes>
                    <layout>ZIP</layout>
                    <!--使用外部配置文件，jar包里没有资源文件-->
                    <addResources>true</addResources>
                    <outputDirectory>${project.build.directory}</outputDirectory>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal>
                        </goals>
                        <configuration>
                            <!--配置jar包特殊标识 配置后，保留原文件，生成新文件 *-run.jar -->
                            <!--配置jar包特殊标识 不配置，原文件命名为 *.jar.original，生成新文件 *.jar -->
                            <!--<classifier>run</classifier>-->
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```





# maven多模块配置

```
父模块指定子模块
	<modules>
		<module>xxl-job-core</module>
		<module>xxl-job-admin</module>
		<module>xxl-job-executor-samples</module>
    </modules>
子模块指定父模块
	<parent>
		<groupId>com.xuxueli</groupId>
		<artifactId>xxl-job</artifactId>
		<version>2.2.1-SNAPSHOT</version>
	</parent>
```

# Maven中的dependencyManagement 

```
//只是对版本进行管理，不会实际引入jar  
<dependencyManagement>  
      <dependencies>  
            <dependency>  
                <groupId>org.springframework</groupId>  
                <artifactId>spring-core</artifactId>  
                <version>3.2.7</version>  
            </dependency>  
    </dependencies>  
</dependencyManagement>  
  
//会实际下载jar包  
<dependencies>  
       <dependency>  
                <groupId>org.springframework</groupId>  
                <artifactId>spring-core</artifactId>  
       </dependency>  
</dependencies>  
```



# maven编译 java源码等级

