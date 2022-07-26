#定义函数
def maopaopaixu(lst):#'lst'可以去掉，直接打上maopaopaixu()并且在括号内输入要针对的对象
    l = len(lst)#列表的长度
    for i in range(l):#
        for j in range(0, l-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(lst)

#循环十次的输入和列表的注入
lst = []
for times in range(1,11):
    x = int(input('请输入第%d个数:' %(times)))
    lst.append(x)

#打印原来的列表和利用冒泡法排序之后的列表
print(lst)
maopaopaixu(lst)#引用函数