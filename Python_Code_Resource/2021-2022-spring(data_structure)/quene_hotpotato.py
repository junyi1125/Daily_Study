class Quene():
    def __init__(self):  # 声明该类的属性
        self.items = []

    def isEmpty(self):  # 判断该队列是否为空，返回bool(True of False)
        return self.items == []

    def enquene(self, item):  # 往队列中添加东西，并且只会添加在尾部(即第0位)
        self.items.insert(0, item)

    def dequene(self):  # 把队列的头部元素踢出去
        return self.items.pop()

    def size(self):  # 队列的长度，返回bool(True of False)
        return len(self.items)


'''
几个小朋友围成一个圆圈，开始一个小朋友手里有土豆
依次传递土豆num次后,手里有土豆的小朋友退出游戏
其余小朋友继续，直到队列中只剩下一个小朋友，返回该小朋友的名字
'''

# 传土豆函数，接受两个参数


def hotPotato(namelist, num):
    simqueue = Quene()
    # 将小朋友名字放入队列中
    for name in namelist:
        simqueue.enquene(name)

    # 传递土豆直到剩下最后一个人
    while simqueue.size() > 1:
        for i in range(num):
            # 循环传递土豆，头部元素出队再回到队里（圆）
            simqueue.enquene(simqueue.dequene())
        # 此时手里有土豆的小朋友(即此时在头部的小朋友)退出游戏
        simqueue.dequene()
    # 返回剩余的最后一个小朋友的名字
    return simqueue.dequene()


print(hotPotato(['bill', 'david', 'susan', 'jane', 'kent', 'brad'], 7))
