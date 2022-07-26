'''
创建两个空列表，一个空字典
'''
lst1 = []
lst2 = []
sum = {}
'''
循环十次输入字符
'''
for count in range(1,11):#做一个循环，范围是[1,11)
    x = str(input('请输入字符\n'))
    lst1.append(x)
    while count == 10:#用while判断一下此时i是第几次了，如果i此时为10，就终止
        break
print(lst1)#这是带有重复元素的列表
lst3 = []
'''
set()本身是一个集合，而集合内的元素不能有重复，在set()的外面讨一个list()是将set()是为了处理成无重复元素的列表
'''
lst2 = set(lst1)
'''
用for循环来分别查找列表中的重复项
'''
for i in lst2:
    lst3.append(lst1.count(i))#append里的意思是对i分别计数，看看有几项
print(lst3)
print(lst2)
sum = zip(lst2,lst3)#zip()是将两个列表压缩
print(dict(sum))