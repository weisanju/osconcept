# XML

## XML语法规则

* 必须有跟元素

* XML声明 可选

  `<?xml version="1.0" encoding="utf-8"?>`

* 所有的 XML 元素都必须有一个关闭标签

* XML 标签对大小写敏感

* XML 必须正确嵌套

* XML 属性值必须加引号

* 实体引用：特殊字符用实体引用替代

  | 实体引用 | 符号 | 含义           |
  | -------- | ---- | -------------- |
  | `&lt;`   | <    | less than      |
  | `&gt;`   | >    | greater than   |
  | `&amp;`  | &    | ampersand      |
  | `&apos;` | '    | apostrophe     |
  | `&quot;` | "    | quotation mark |

* XML 中的注释

  `<!-- This is a comment -->`

* 空格会被保留

  HTML 会把多个连续的空格字符裁减（合并）为一个：

* XML 以 LF 存储换行

## XML元素

* XML 元素指的是从（且包括）开始标签直到（且包括）结束标签的部分。

* 一个元素可以包含：
  * 其他元素
  * 文本
  * 属性
  * 或混合以上所有...
* 元素命名规则
  * 字母数字其他字符
  * 不能以数字标点符号开始
  * 不能以字母xml开始
  * 不能有空格
  * 避免使用 : -  . 的字符

## XML属性

XML 中，您应该尽量避免使用属性。如果信息感觉起来很像数据，那么请使用元素吧

元数据（有关数据的数据）应当存储为属性，而数据本身应当存储为元素。

## XML验证

* 合法的 XML 文档是"形式良好"的 XML 文档，这也符合文档类型定义（DTD,documentTyoeDefinition ）的规则
* `<!DOCTYPE note system "note.dtd"`

* DTD 的目的是定义 XML 文档的结构

* W3C 支持一种基于 XML 的 DTD 代替者，它名为 XML Schema

## 使用 CSS /XSLT显示 XML

* `<?xml-stylesheet type="text/css" href="cd_catalog.css"?>`

* 使用 CSS 格式化 XML 不是常用的方法。W3C 推荐使用 XSLT。
* XSLT（eXtensible Stylesheet Language Transformations）远比 CSS 更加完善。
* 通过使用 XSLT，您可以把 XML 文档转换成 HTML 格式。

## XML 命名空间

* XML 命名空间提供避免元素命名冲突的方法。

* 在 XML 中的命名冲突可以通过使用名称前缀从而容易地避免。

  ```
  <h:table>
  <h:tr>
  <h:td>Apples</h:td>
  <h:td>Bananas</h:td>
  </h:tr>
  </h:table>
  ```

* 当在 XML 中使用前缀时，一个所谓的用于前缀的**命名空间**必须被定义。xmlns:*前缀*="*URI*"

  ```
  <h:table xmlns:h="http://www.w3.org/TR/html4/">
  <h:tr>
  <h:td>Apples</h:td>
  <h:td>Bananas</h:td>
  </h:tr>
  </h:table>
  ```

* 元素定义默认的命名空间可以让我们省去在所有的子元素中使用前缀的工作

  `<table xmlns="http://www.w3.org/TR/html4/">`

  

## XML CDATA

* XML 文档中的所有文本均会被解析器解析。只有 CDATA 区段中的文本会被解析器忽略。
* CDATA 部分由 `<![CDATA[` 开始，由 "**]]>**" 结束：

# 

# DTD

## 简介

DTD（文档类型定义）的作用是定义 XML 文档的合法构建模块。

DTD 可被成行地声明于 XML 文档中，也可作为一个外部引用。

## XML构建模块

* 所有的 XML 文档（以及 HTML 文档）均由以下简单的构建模块构成：
  * 元素
  * 属性
  * 实体：特殊字符的实体引用
  * PCDATA：parsed character data，**被解析器解析的文本**
  * CDATA：**不会被解析器解析的文本**

## DTD元素申明

声明一个元素

```
<!ELEMENT element-name category>
或
<!ELEMENT element-name (element-content)>
```

* 空元素：`<!ELEMENT br EMPTY>`
* PCDATA 的元素：`<!ELEMENT from (#PCDATA)>`
* 带有任何内容的元素:`<!ELEMENT note ANY>`
* 带有子元素（序列）的元素
  * 带有一个或多个子元素的元素通过圆括号中的子元素名进行声明：
  * `<!ELEMENT element-name (child1)>`
  * `<!ELEMENT element-name (child1,child2,...)>`
* 声明只出现一次的元素
  * `<!ELEMENT note (message)>`
* 声明最少出现一次的元素
  * `<!ELEMENT note (message+)>`
* 声明出现零次或多次的元素
  * `<!ELEMENT note (message*)>`
* 声明出现零次或一次的元素
  * `<!ELEMENT note (message?)>`

* 声明"非.../即..."类型的内容
  * `<!ELEMENT note (to,from,header,(message|body))>`
* 声明混合型的内容
  * `<!ELEMENT note (#PCDATA|to|from|header|message)*>`



## DTD属性申明

在 DTD 中，属性通过 ATTLIST 声明来进行声明。

* 语法：

  `<!ATTLIST element-name attribute-name attribute-type attribute-value>`

* 类型选项

  | 类型               | 描述                          |
  | :----------------- | :---------------------------- |
  | CDATA              | 值为字符数据 (character data) |
  | (*en1*\|*en2*\|..) | 此值是枚举列表中的一个值      |
  | ID                 | 值为唯一的 id                 |
  | IDREF              | 值为另外一个元素的 id         |
  | IDREFS             | 值为其他 id 的列表            |
  | NMTOKEN            | 值为合法的 XML 名称           |
  | NMTOKENS           | 值为合法的 XML 名称的列表     |
  | ENTITY             | 值是一个实体                  |
  | ENTITIES           | 值是一个实体列表              |
  | NOTATION           | 此值是符号的名称              |
  | xml:               | 值是一个预定义的 XML 值       |

* 默认**属性值**

  | 值           | 属性的默认值   |
  | ------------ | -------------- |
  |              | 属性值         |
  | #REQUIRED    | 属性值是必需的 |
  | #IMPLIED     | 属性不是必需的 |
  | #FIXED value | 属性值是固定的 |

## DTD实体

* 实体是用于定义引用普通文本或特殊字符的快捷方式的变量。

* 实体引用是对实体的引用
* 实体可在内部或外部进行声明。

* 一个内部实体声明

  * `<!ENTITY entity-name "entity-value">`

    ```
    <!ENTITY writer "Donald Duck.">
    <!ENTITY copyright "Copyright runoob.com">
    
    XML 实例：
    
    <author>&writer;&copyright;</author>
    ```

    

  * 一个实体由三部分构成: 一个和号 (&), 一个实体名称, 以及一个分号 (;)。

* 一个外部实体声明

  ```
  DTD 实例:
  
  <!ENTITY writer SYSTEM "http://www.runoob.com/entities.dtd">
  <!ENTITY copyright SYSTEM "http://www.runoob.com/entities.dtd">
  
  XML example:
  
  <author>&writer;&copyright;</author>
  ```

