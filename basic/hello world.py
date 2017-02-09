#!/usr/bin/python
#raw_input("\n\nPress the enter key to exit.")

####################Python 基础语法####################P

#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys; x = 'runoob'; sys.stdout.write(x + '\n');


print("Hello, World!");


"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
item_one=1;   # 这是一个注释
item_two=2;
item_three=3;

#Python语句中一般以新行作为为语句的结束符。
#但是我们可以使用斜杠（ \）将一行的语句分为多行显示，
total = item_one + \
        item_two + \
        item_three;
print("total总数")
print(total);

# 语句中包含[], {} 或 () 括号就不需要使用多行连接符
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']


word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
print(word);

#  打印多个语句
print(paragraph);
if True:
    print("true");
else:
    print("false");



####################Python 变量类型####################P
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

# print counter
# print miles
# print name

#-------------------------多个变量赋值
#Python允许你同时为多个变量赋值。例如：
a = b = c = 1
#以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。
#您也可以为多个对象指定多个变量。例如：
a, b, c = 1, 2, "john"
#-------------------------多个变量赋值


#-------------------------Python字符串
'''
python的字串列表有2种取值顺序:
从左到右索引默认0开始的，最大范围是字符串长度少1
从右到左索引默认-1开始的，最大范围是字符串开头
如果你的实要取得一段子串的话，可以用到变量[头下标:尾下标]
'''
s = 'ilovepython'
print(s[1:5])  #结果是love
print(s[1:-6])  #结果是love


str = 'Hello World!'
print (str) # 输出完整字符串
print (str[0]) # 输出字符串中的第一个字符
print (str[2:5]) # 输出字符串中第三个至第五个之间的字符串
print (str[2:]) # 输出从第三个字符开始的字符串


#加号（+）是字符串连接运算符，星号（*）是重复操作。如下实例：
print (str * 2) # 输出字符串两次
print (str + "TEST") # 输出连接的字符串

#-------------------------Python字符串

#-------------------------Python列表

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list) # 输出完整列表
print (list[0]) # 输出列表的第一个元素
print (list[1:3]) # 输出第二个至第三个的元素
print (list[2:]) # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2) # 输出列表两次
print (list + tinylist) # 打印组合的列表
#-------------------------Python列表

#-------------------------Python元组
#元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print (tuple) # 输出完整元组
print (tuple[0] )# 输出元组的第一个元素
print (tuple[1:3]) # 输出第二个至第三个的元素
print (tuple[2:]) # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2) # 输出元组两次
print (tuple + tinytuple) # 打印组合的元组
#-------------------------Python元组

#-------------------------Python元字典
'''
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成

'''
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734,'dept': 'sales'}
print (dict['one']);# 输出键为'one' 的值
print (dict[2]) ;# 输出键为 2 的值
print (tinydict) ;# 输出完整的字典
print (tinydict.keys()) ;# 输出所有键
print (tinydict.values()) ;# 输出所有值

#-------------------------Python 元字典

#--------------------------Python数据类型转换
'''

有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
函数	描述
int(x [,base])
将x转换为一个整数
long(x [,base] )
将x转换为一个长整数
float(x)
将x转换到一个浮点数
complex(real [,imag])
创建一个复数
str(x)
将对象 x 转换为字符串
repr(x)
将对象 x 转换为表达式字符串
eval(str)
用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)
将序列 s 转换为一个元组
list(s)
将序列 s 转换为一个列表
set(s)
转换为可变集合
dict(d)
创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)
转换为不可变集合
chr(x)
将一个整数转换为一个字符
unichr(x)
将一个整数转换为Unicode字符
ord(x)
将一个字符转换为它的整数值
hex(x)
将一个整数转换为一个十六进制字符串
oct(x)
将一个整数转换为一个八进制字符串
'''