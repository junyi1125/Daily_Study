'''
对一个空白的列表对其注入
'''
lst = []
for i in range(1,4):
    lst.append(input('请输入第%d个数字:' %(i)))
print(lst)#显示原始列表
lst.sort(key=len)#以元素长度为关键值
lst.reverse()#反转
print(lst)
lst.pop(0)#删掉第一个
print(lst)