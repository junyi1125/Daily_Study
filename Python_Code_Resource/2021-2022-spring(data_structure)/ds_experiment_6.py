# 节点之引用
class BinaryTree():  # 创建BinaryTree()类
    def __init__(self, rootObject):
        self.Key = rootObject
        self.LeftChild = None
        self.RightChild = None

    '''插入部分'''

    def insertLeft(self, newNode):  # 插入左子节点
        if self.LeftChild == None:
            self.LeftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.LeftChild = self.LeftChild
            self.LeftChild = t

    def insertRight(self, newNode):  # 插入右子节点
        if self.RightChild == None:
            self.RightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.RightChild = self.RightChild
            self.RightChild = t

    '''访问部分'''

    def getRightChild(self):  # 返回当前节点的右子节点所对应的二叉树
        return self.RightChild

    def getLeftChild(self):  # 返回当前节点的左子节点所对应的二叉树
        return self.LeftChild

    def getRootVal(self):  # 返回当前节点存储的对象
        return self.Key


'''先访问根结点，然后递归地前序遍历左子树，最后递归地前序遍历右子树'''


def Preorder(tree):  # 前序遍历
    if tree:
        print(tree.getRootVal())  # 先输出根结点
        Preorder(tree.getLeftChild())  # 左节点
        Preorder(tree.getRightChild())  # 右节点


'''先递归地中序遍历左子树，然后访问根节点，最后递归地中序遍历右子树'''


def Inorder(tree):  # 中序遍历
    if tree != None:
        Inorder(tree.getLeftChild())
        print(tree.getRootVal())
        Inorder(tree.getRightChild())


'''先递归地后序遍历左子树,然后递归地后序遍历右子树,最后访问根节点'''


def Postorder(tree):  # 后序遍历
    if tree != None:
        Postorder(tree.getLeftChild())
        Postorder(tree.getRightChild())
        print(tree.getRootVal())


def leave(tree):  # 节点数量
    if tree == None:
        return 0
    else:
        a = (1+leave(tree.getLeftChild())+leave(tree.getRightChild()))
    return a


'''根结点部分'''
r = BinaryTree('A')
'''左节点部分'''
for i in ['I','G','E','D','B']:
    r.insertLeft(i)
'''右节点部分'''
for l in ['J','H','F','C']:
    r.insertRight(l)

print('前序遍历')
Preorder(r)
print('--------')
print('中序遍历')
Inorder(r)
print('--------')
print('后序遍历')
Postorder(r)
print('--------')
print('节点数量为', leave(r))
