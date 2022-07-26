#计算从1到n的立方和
def lifang(num):#定义了一个处理立方的函数
    he = 0
    for i in range(1,num+1):
        he += i**3
    return he
num = int(input('请输入数字:'))
print(lifang(num))
print('-----------')
#2-100的孪生素数
print('孪生素数')
def sushu():
    lst = []
    for n in range(2,101):
        for x in range(2,n-1):
            if n % x == 0:
                break
        else:
            lst.append(n)
    tpl = tuple(lst)
    for y in range(2,len(lst)):
        if int(tpl[y] - tpl[y-1]) == 2:
            print('(',tpl[y-1],',',tpl[y],')')
sushu()
print('-----------')
#1-9阶乘
print('1-9阶乘')
def jiecheng():
    for num in range(1,10):
        a = 1
        for i in range(1,num+1):
            a = a * i
        print('%d! = %d' %(num,a))
jiecheng()
print('-----------')