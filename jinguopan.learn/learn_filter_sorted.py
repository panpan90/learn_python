#coding=utf-8
import  math
###########################
# filter用于过滤序列，它接受一个
###########################


##判断n是否为素数
def  isPrime(n):
    flag = True
    if n < 2:
        flag=False
    else:
        for i in range(2,int(math.sqrt(n)),1):
            if n%i==0:
                flag=False;
    return flag;
# python中的函数没有返回值类型
def deletedPrime(n):
    flag=isPrime(n);
    if flag == True:
        flag=False
    else:
        flag=True
    return flag;

if __name__ == '__main__':
    list=filter(deletedPrime,range(1,200,1));
    print(list)