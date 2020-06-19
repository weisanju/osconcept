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

