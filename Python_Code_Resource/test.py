class CSNode(object):
    '''树孩子兄弟二叉链表节点类'''

    def __init__(self, data=None, firstchild=None, nextsibling=None):
        self.data = data
        self.firstchild = firstchild  # 最左孩子结点
        self.nextsibling = nextsibling  # 右兄弟结点


class CSTree(object):
    '''树的二叉链表类'''

    def __init__(self, root=None):
        self.root = root

    def OutPath(self):
        '''依据普通树的二叉树，输出树中所有从根到叶的路径'''
        '''（T为普通树对应的二叉树，T为栈）'''
#因实例方法中的递归部分在调用前需完成部分变量初始化，
# 故在实例方法中需设计一个仅包括递归代码的局部函数
        def outpath(T):
            while T:  # T为二叉树当前节点
                S.Push(T.data)  # 当前节点作为路径的一部分入栈
                if T.firstchild == None:  # 当前结点左孩子为空，树中对应节点为叶子结点
                    print('树的一条路径(调用实例方法):', S.stack)  # 输出从栈底到栈顶的一条路径
                else:
                    outpath(T.firstchild)  # 遍历左子树
                S.Pop()
         #将当前访问的结点从路径中退出，包含该节点的所有路径已遍历完成
        #执行Pop()操作的两种情况：
        # ①print(''树的一条路径).....后；②outpath（T.firstchild)后（左子树遍历完成）
                T = T.nextsibling  # 左子树遍历完成后，开始遍历右子树

        S = Stack()  # 递归调用钱初始化
        T = self.root  # 递归调用钱初始化
        outpath(T)

    def CreatTree(self):
        '''依据用户输入节点二元组建立树的二叉链表'''
#用户输入：自顶向下，自左向右这个输入双亲-孩子有序对
#二元组'#根节点'作为起始，二元组'##'作为结束
        if self.root != None:
            print('树非空，无法加入结点')
            return False

        S = Queue()
        ch = input('输入二元组：')
        one = ch[0]
        two = ch[1]  # 接受第一次输入

        while two != '#':
            p = CSNode(two)
            S.EnQueue(p)  # 新建结点入队

            if one == '#':  # 建立根结点
                self.root = p
            else:  # 非根节点
                head = S.GetHead()  # 获取队头元素
                while head.data != one:
                    #修正队头元素为当前二元组的父结点
                    S.DeQueue()
                    head = S.GetHead()
                if head.firstchild == None:
                    #父节点没有左子树
                    head.firstchild = p
                    temp = p
                    #暂存父节点的最左孩子结点地址
                    # 便于添加父节点的其他孩子结点
                else:
                    temp.nextsibling = p
                    temp = p
                    #暂存已入队的最右孩子结点
            ch = input('输入二元组：')
            one = ch[0]
            two = ch[1]


class Queue(object):
    '''队列'''

    def __init__(self):
        '''构建队列'''
        self.elem = []

    def EnQueue(self, value):
        '''元素入队'''
        self.elem.append(value)  # 列表尾插入

    def DeQueue(self):
        '''元素出队'''
        if len(self.elem) == 0:
            return False  # 空队报错退出
        return self.elem.pop(0)  # 列表头出队

    def GetHead(self):
        '''获取队头元素'''
        if len(self.elem) == 0:
            return False
        return self.elem[0]


class Stack(object):
    '''栈'''

    def __init__(self):
        self.stack = []

    def Push(self, data):
        self.stack.append(data)  # 在表尾入栈

    def Pop(self):
        if len(self.stack) == 0:
            return False
        return self.stack.pop()


'''函数定义'''


def AllPath(T, S):
    '''采用先序遍历输出二叉树从根到所有叶子结点的路径'''
    #T为一棵二叉树，S为栈
    if T:  # 指针不为空时
        S.Push(T.data)
        if T.Lchild == None and T.Rchild == None:
            S.PrintStack(S)  # 输出栈中所有元素（整条路径），但不出栈
        else:
            AllPath(T.Lchild, S)
            AllPath(T.Rchild, S)
        S.Pop(S)  # 找到叶子结点时，出栈栈顶元素（叶子结点）


def OutPath2(T, S):
    '''依据普通树的二叉树，输出树中所有从根到叶的路径'''
    '''（T为普通树对应的二叉树，T为栈）'''
    while T:  # T为二叉树当前节点
        S.Push(T.data)  # 当前节点作为路径的一部分入栈
        if T.firstchild == None:  # 当前结点左孩子为空，树中对应节点为叶子结点
            print('树的一条路径(调用函数):', S.stack)  # 输出从栈底到栈顶的一条路径
        else:
            OutPath2(T.firstchild, S)  # 遍历左子树
        S.Pop()
#执行Pop()操作的两种情况：
# ①执行print(''树的一条路径).....之后，出栈的是叶子结点；
# ②执行OutPath2（T.firstchild,S)之后，此时左子树遍历完成。在遍历右子树之前，
# 需从栈中退出左子树的根节点，因其为右子树根节点的兄长结点。
        T = T.nextsibling  # 左子树遍历完成后，开始遍历右子树


def TreeDepth(T):
    '''求森林深度，T为森林的二叉链表'''
    if T == None:
        return 0
    else:
        h1 = TreeDepth(T.firstchild)
        h2 = TreeDepth(T.nextsibling)
        if h1+1 > h2:
            return h1+1
        else:
            return h2


'''主程序'''
#嵌套实例化方式建立二叉树
tree1 = CSTree(CSNode('A', CSNode('B', None, CSNode('C',
                                                    CSNode('E', None, CSNode('F', CSNode('G'))), CSNode('D')))))

#实例化保存路径的栈
S = Stack()

#采用函数调用实现递归，主调程序略显复杂
OutPath2(tree1.root, S)

#采用实例方法实现递归，优点主调程序更简洁，实例方法实现略复杂
tree1.OutPath()

#输出以二叉链表存储的森林的深度
print('森林的深度为：', TreeDepth(tree1.root))

#用户输入方式建立树的二叉链表
tree2 = CSTree()  # 新建树的空二叉链表
tree2.CreatTree()
print()
