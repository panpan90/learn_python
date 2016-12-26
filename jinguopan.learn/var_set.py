#coding=utf-8

###################
# python中变量和集合
#
###################
## python中 有5种数据类型 1：数字 2：字符串 3：列表(即list) 4: 元组 5：字典 6：set

# 1：数字 python 中定义变量时不需要显示指定变量类型，以下为python中变量使用的典型语法
######### 变量定义和赋值
# a =100
# b =100.0
# c ="123"
# print(a);print(b);print(c)
#
# # 多重赋值
# a = b =c =9;print(a);print(b);print(c)
a,b,c = 123,789,1011;print(a);print(b);print(c)
# 字符串的使用
'''
str="jinguopan123"
print("打印整个字符 "+str)
print("打印第一个字符 "+str[0])
print("打印第一个到第五个字符 "+str[0:4])
print("打印第一个到第五个字符 "+str[:4]) # 默认从0开始
print("打印第3个字符到最后 "+str[3:]) #默认到最后一个字符
print("字符串拼接使用+号 "+ (str[0:3]+"pinjin"))
str=str*2
print("字符串重复两次 "+str)

###列表的使用  注意定义list是用 [] 而不是{} 列表的长度和值都能改变
list=["333",999] #定义了一个list
list2=[123,"21"] # 也可以直接定义
list[0]="333"
list[1]=789
print("打印整个列表 ",list) # +是连接两个字符的，不能用+ 连接列表
print("打印整个列表",list[0:])
print("打印列表第0个元素",list[0])
print("打印两倍的列表 ",list*2)
print("两个列表进行连接 ",(list+list2))

## 元组的使用，即数组，元组()，里面的值不能被更新

tuple=("123",678,"我的")
tuple1=("连接 tuple",)
print("打印第二到第三个元素 元组 ",tuple[0:2])
print("打印整个元祖 ",tuple)
tuple3=tuple+tuple1
print("tuple3 ",tuple3)
print("两个tuple 进行连接 ", tuple+tuple1)
'''
list9 = list()
list9.append("1236666666666666666")
list9.append("899")
print(list9)
for i in list9:
    print(i)
cusDict= dict()
cusDict.setdefault("123","789")
for key in cusDict:
    print(key)
    print(cusDict.get(key))


