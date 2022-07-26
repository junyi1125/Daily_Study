import random


def ChainRadixSort(Lst):
    for i in range(len(Lst)):  # 根据待排列表的长度来生成"桶"
        Basket = [[] for k in range(len(Lst))]  # 创建10个空列表
        for j in range(len(Lst)):  # 这一部分执行LSD基数排序
            '''
            针对第j个桶,从个位数开始开始存放到对应的桶中,然后随着i的递增,进行操作的位数逐渐递增,
            最开始是个位数,第二次i=1时,排的十位数
            如:当i=0时,第一次先对Lst[j]这个元素整除1,然后在除于10来求余数(因为是10的0次方)
            '''
            Basket[Lst[j]//(10**i) % 10].append(Lst[j])
            # 这里的append(Lst[j])是根据前面的元素的个位数来插入的，例如"456"的个位数是6，那就插入到第6位(第7个列表)
        Lst = [n for x in Basket for n in x]  # 把Basket里的元素逐个取出给到Lst中
        # 嵌套for循环，增加易读性
    return Lst


# 给这个新生成的列表，利用random函数，在[100,1000)之间生成10个不重复的整数
n = int(input('你想要多少个整数\n'))
Lst1 = [random.randint(100, 1000) for num in range(n)]


print(Lst1)
print(ChainRadixSort(Lst1))
