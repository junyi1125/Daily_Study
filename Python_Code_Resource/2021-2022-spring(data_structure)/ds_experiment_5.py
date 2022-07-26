class BinaryTree():  # 创建BinaryTree()类
    def __init__(self, rootObject):
        self.Key = rootObject
        self.LeftChild = None
        self.RightChild = None

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
        return self.Key


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
