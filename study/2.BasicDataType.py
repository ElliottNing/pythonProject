'''
Python3 基本数据类型
'''

# 1、Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
# 等号（=）用来给变量赋值。
# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print('整型变量:', counter)
print('浮点型变量:', miles)
print('字符串:', name)

# 2、多个变量赋值
# Python允许你同时为多个变量赋值。例如：
a = b = c = 1
print(c)
# 以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。
# 您也可以为多个对象指定多个变量。两个对象 1 和 0.2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。例如：
a, b, c = 1, 0.2, "runoob"
print(a, b, c)

# 3、标准数据类型
# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
# Python3 的六个标准数据类型中：
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

# 3.1、Number（数字）
# Python3 支持 int、float、bool、complex（复数）。
# 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# 像大多数语言一样，数值类型的赋值和计算都是很直观的。
# 内置的 type() 函数可以用来查询变量所指的对象类型。
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))


# 3.2、isinstance 和 type 的区别在于：
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
class A:
    pass


class B(A):
    pass


isinstance(A(), A)
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)

# 3.3、注意：Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
# 在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
# print('==subclass(bool, int):', issubclass(bool, int))
print('True==1:', True == 1)
print('False==0:', False == 0)
print('True+1:', True + 1)
print('False+1:', False + 1)
print('1 is True:', 1 is True)
print('1 is False:', 1 is False)
print('0 is True:', 0 is True)
print('0 is False:', 0 is False)

# 您也可以使用del语句删除一些对象引用。
# del语句的语法是：del var1[,var2[,var3[....,varN]]]
# 您可以通过使用del语句删除单个或多个对象。例如：
del a
del b, c
# print('a删除后:', a)
# print('bc删除后:', b, c)
# NameError: name 'a' is not defined

# 3.4、数值运算
print('加法:', 5 + 4)
print('减法:', 4.3 - 2)
print('乘法:', 3 * 7)
print('除法，得到一个浮点数:', 2 / 4)
print('除法，得到一个整数:', 2 // 4)
print('取余:', 17 % 3)
print('乘方:', 2 ** 5)
# Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型

# 4、String（字符串）
# Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
# 字符串的截取的语法格式：变量[头下标:尾下标]
# 详见img/string截取图片.png
# 加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，与之结合的数字为复制的次数。实例如下：
str2 = 'Runoob'
print('输出字符串:', str2)  # 输出字符串
print('输出第一个到倒数第二个的所有字符:', str2[0:-1])  # 输出第一个到倒数第二个的所有字符
print('输出字符串第一个字符:', str2[0])  # 输出字符串第一个字符
print('输出从第三个开始到第五个的字符:', str2[2:5])  # 输出从第三个开始到第五个的字符
print('输出从第三个开始的后的所有字符:', str2[2:])  # 输出从第三个开始的后的所有字符
print('输出字符串两次，也可以写成 print (2 * str):', str2 * 2)
print('连接字符串:', str2 + "TEST")  # 连接字符串

# 4.1、Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
print('Ru\'oob')
print(r'Ru\'noob')
# 另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。
print(
    '''R
u
o
o
b''')
# 注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。
word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])
# 与 C语言字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。

# 5、List（列表）
# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
# 列表是有序的
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
# List可以使用+操作符进行拼接。
# List中的元素是可以改变的。
# 列表截取的语法格式如下：变量[头下标:尾下标]
# 如图：img/列表1.png

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
print('输出完整列表:', list)  # 输出完整列表
print('输出列表第一个元素:', list[0])  # 输出列表第一个元素
print('从第二个开始输出到第三个元素:', list[1:3])  # 从第二个开始输出到第三个元素
print('输出从第三个元素开始的所有元素:', list[2:])  # 输出从第三个元素开始的所有元素
print('输出两次列表:', tinylist * 2)  # 输出两次列表
print('连接列表:', list + tinylist)  # 连接列表

# 与Python字符串不一样的是，列表中的元素是可以改变的：
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []  # 将对应的元素值设置为 []
print(a)

# Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
# 如图：img/列表2.png
letters = ['r', 'u', 'n', 'o', 'o', 'b']
print(letters[1:4:2])


# 如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)
    return output


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)

# 6、Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。
# 元组写在小括号 () 里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同：
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')
print('输出完整元组:', tuple)  # 输出完整元组
print('输出元组的第一个元素:', tuple[0])  # 输出元组的第一个元素
print('输出从第二个元素开始到第三个元素:', tuple[1:3])  # 输出从第二个元素开始到第三个元素
print('输出从第三个元素开始的所有元素:', tuple[2:])  # 输出从第三个元素开始的所有元素
print('输出两次元组:', tinytuple * 2)  # 输出两次元组
print('连接元组:', tuple + tinytuple)  # 连接元组

# 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。
# 其实，可以把字符串看作一种特殊的元组。
tup = (1, 2, 3, 4, 5, 6)
print(tup[0])

print(tup[1:5])

# tup[0] = 11  # 修改元组元素的操作是非法的

# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()  # 空元组
tup2 = (20,)  # 只有一个元素，需要在元素后添加逗号

# 7、Set（集合）
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 创建格式：parame = {value01,value02,...} 或者 set(value)

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)  # 输出集合，重复的元素被自动去掉
print(set({2, 3}))
# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print('a 和 b 的差集:', a - b)  # a 和 b 的差集
print('a 和 b 的并集:', a | b)  # a 和 b 的并集
print('a 和 b 的交集:', a & b)  # a 和 b 的交集
print('a 和 b 中不同时存在的元素:', a ^ b)  # a 和 b 中不同时存在的元素

# 8、Dictionary（字典）
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取，相当于Java map。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}  # 这不就是json么

print('输出dict的值:', dict)  # 输出dict
print('输出键为 \'one\' 的值:', dict['one'])  # 输出键为 one 的值
print('输出键为 2 的值:', dict[2])  # 输出键为 2 的值
print('输出完整的字典:', tinydict)  # 输出完整的字典
print('输出所有键:', tinydict.keys())  # 输出所有键
print('输出所有值:', tinydict.values())  # 输出所有值

# print(int(x [,base])) # 将x转换为一个整数
# print(float(x)) # 将x转换到一个浮点数
# print(complex(real [,imag])) # 创建一个复数
# print(str(x)) # 将对象 x 转换为字符串
# print(repr(x)) # 将对象 x 转换为表达式字符串
# print(eval(str)) # 用来计算在字符串中的有效Python表达式,并返回一个对象
# print(tuple(s)) # 将序列 s 转换为一个元组
# print(list(s)) # 将序列 s 转换为一个列表
# print(set(s)) # 转换为可变集合
# print(dict(d)) # 创建一个字典。d 必须是一个 (key, value)元组序列。
# print(frozenset(s)) # 转换为不可变集合
# print(chr(x)) # 将一个整数转换为一个字符
# print(ord(x)) # 将一个字符转换为它的整数值
# print(hex(x)) # 将一个整数转换为一个十六进制字符串
# print(oct(x)) # 将一个整数转换为一个八进制字符串
