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

    def travel(self):
        key = []  # 存放序列坐标
        value = []  # 存放元素
        if self.isEmpty():
            return IndexError('队列是空的！')
        else:
            for index, i in enumerate(self.items):
                key.append(index)
                value.append(i)
            a_line = dict(zip(key, value))
            print(a_line)


q = Quene()
for i in range(9):
    q.enquene(i)

for i in range(5):
    q.dequene()

for i in range(10, 13):
    q.enquene(i)

print(q.travel())
