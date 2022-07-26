def BinaryTree(r):  # 列表函数BinaryTree,那个r就是根节点的值
    return [r, [], [], ]  # 仅有一个根节点和两个作为子节点的空列表


def insertLeft(root, newBranch):  # 插入左子树
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    print(root)


def insertRight(root, newBranch):  # 插入右子树
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    print(root)


'''
树的访问函数
'''


def getRootVal(root):  # 返回当前节点存储的对象
    return root[0]


def setRootVal(root, newVal):  # 在当前节点中存储参数val中的对象
    root[0] = newVal


def getLeftChild(root):  # 返回当前节点的右子节点所对应的二叉树
    return root[1]


def getRightChild(root):  # 返回当前节点的左子节点所对应的二叉树
    return root[2]


r = BinaryTree(3)
print(r)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)
l = getLeftChild(r)
print(l)
setRootVal(l, 9)
print(r)
insertLeft(l, 11)
print(r)
x = getRightChild(getRightChild(r))
print(x)
