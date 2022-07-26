class SingleNode():  # 定义的数据域和指针域

    def __init__(self, item):  # 构造函数，在生成对象时调用
        self.item = item  # 实例化(这俩都是)
        self.next = None  # 指向下一个结点。还尚未与其他节点有联系;None是因为目前指针域不知道指到哪里去，但是它得实例化，所以先给他搞个None


class BinaryTree():  # 创建BinaryTree()类
    def __init__(self, rootObject, node=None):
        self.Key = rootObject
        self.LeftChild = None
        self.RightChild = None
        self.__head = node

    def insertLeft(self, newNode):  # 插入左子节点
        if self.LeftChild == None:
            self.LeftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.LeftChild
            self.LeftChild = t

    def insertRight(self, newNode):  # 插入右子节点
        if self.RightChild == None:
            self.RightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.RightChild
            self.RightChild = t

    '''
    二叉树的访问函数
    '''

    def getRightChild(self):  # 返回当前节点的右子节点所对应的二叉树
        return self.RightChild

    def getLeftChild(self):  # 返回当前节点的左子节点所对应的二叉树
        return self.LeftChild

    def setRootVal(self, obj):  # 在当前节点中存储参数val中的对象
        self.Key = obj

    def getRootVal(self):  # 返回当前节点存储的对象
        return self.key


r = BinaryTree('A')
r.insertLeft('B')
r.insertLeft('D')
r.insertLeft('G')
r.insertRight('H')
r.insertLeft('I')
r.insertRight('C')
r.insertRight('F')
r.insertLeft('E')
r.insertRight('J')
