XML+XSD,SOAP和WSDL就是构成WebService平台的三大技术。

WebService采用HTTP协议传输数据，采用XML格式封装数据

XML解决了数据表示的问题，但它没有定义一套标准的数据类型

XML Schema(XSD)就是专门解决这个问题的一套标准，WebService平台就是用XSD来作为其数据类型系统的



SOAP协议 = HTTP协议 + XML+XSD

WSDL:基于xml的，用于描述web Service及其函数，参数返回值

WebService服务提供商可以通过两种方式来暴露它的WSDL文件地址

* 注册到UDDI服务器，以便被人查找
* 直接告诉给客户端调用者





