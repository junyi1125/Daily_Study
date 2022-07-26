class SingleNode():  # 定义的数据域和指针域

    def __init__(self, item):  # 构造函数，在生成对象时调用
        self.item = item  # 实例化(这俩都是)
        self.next = None  # 指向下一个结点。还尚未与其他节点有联系;None是因为目前指针域不知道指到哪里去，但是它得实例化，所以先给他搞个None


'''--------------------------------------------------------------'''


class SingleLinkList():  # 定义一个'不带头节点的单链表'的类

    def __init__(self, node=None):  # 构造头结点
        self.__head = node  # 头指针

    def is_empty(self):  # 判断链表是否为空
        # 判断头指针的是否为空，并且返回bool值。原理:如果头指针为空，就说明与判断的None一样，可以成立，所以返回True，反之，不对就返回False
        return self.__head == None

    def length(self):  # 求链表的长度
        cur = self.__head  # cur游标,用来移动遍历节点
        count = 0  # count记录数量
        while cur != None:  # 如果这个位置存在元素
            count += 1  # count就+1
            cur = cur.next  # 然后重新定义cur，意思就是说当上述两句话运行结束之后，cur变成刚才cur的下一个
        return count

    def travel(self):  # 遍历整个链表
        cur = self.__head  # cur游标,用来移动遍历节点；刚开始的时候cur为头指针
        i = 0  # 计数作用
        while cur != None:  # 当头指针不为零的时候
            i += 1  # 原来的i+1后，再赋值给i
            print(cur.item, end=" ")  # 打印元素;后面这个end是为了关掉换行，让它在同一行输出
            cur = cur.next  # 与length()中的cur同样道理

    def add(self, item):  # 在链表头部添加元素，也就是"头插法"
        '''那个node是把SingleNode()打上了个标签，方便用'''
        node = SingleNode(item)  # 把数据元素构成一个链表的节点,也就是把item封装成列表所需要使用的节点
        node.next = self.__head  # 让item指向原来的头节点
        '''self.__head指向了None,下面的self.__head指向node'''
        self.__head = node  # 让原有的__head指向新的节点

    def append(self, item):  # 尾插法
        node = SingleNode(item)  # 把数据元素构成一个链表的节点,也就是把item封装成列表所需要使用的节点
        cur = self.__head
        if self.is_empty():  # 如果刚开始的时候链表为空
            self.__head = node  # 我们给它添加一个节点，否则next是无法成立的
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):  # 向任意位置增加节点
        node = SingleNode(item)  # 与add()中的作用一样
        pre = self.__head  # pre指向了第一个节点
        count_time = 0  # 它会随着pre走
        '''不可以加=号,pre就不在我们所要添加元素的那个位置了'''
        while count_time < (pos-1):  # 定义一个循环，往后移动
            pre = pre.next
            count_time += 1
            # 当循环结束后，pre指向pos—1的位置
        node.next = pre.next  # 改变node的next区域，让它去指向pre的next
        pre.next = node  # 让pre.next指向节点


'''--------------------------------------------------------------'''


s1 = SingleLinkList()  # 给SingleLinkList()定义一个标签，方便调用
print(s1.is_empty())  # 判断数据域是否为空，返回bool值

lst = [1, 2, 3, 4, 5, 7, 8, 9, 10]  # 待置入元素
for i in lst:  # 利用一个for的循环，将列表lst里的元素利用append()函数从尾部插入
    s1.append(i)  # 调用append()函数

print(s1.travel())  # 遍历链表
print(s1.length())  # 此时链表的长度

s1.insert(4, 6)  # 在第四个位置插入元素"6"
print(s1.travel())  # 再遍历一遍列表

print(s1.length())  # 此时链表的长度
