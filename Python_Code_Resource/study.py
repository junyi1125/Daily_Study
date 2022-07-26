class BiThrNode(object):
    '''线索二叉树结点类'''
    def __init__(self,data=None,lchild=None, rchild=None,\
        pred=None,succ=None):
        self.data   = data
        self.lchild  = lchild
        self.rchild = rchild;
        self.pred  = pred           #前驱线索
        self.succ  =  succ           #后继线索

class BiThrTree(object):
    '''线索二叉树类'''
    def __init__(self,root=None):
        self.root =root #线索二叉树带有头结点，头指针指向头结点

    def InOrder(self):
        p = self.root.succ
        while p != self.root:
            print (p.data)    #访问节点
            p = p.succ  

class BiTNode(object):
    '''二叉链表结点类'''
    def __init__(self , data=None, lchild=None, rchild=None) :
        self.data = data                            #结点数据域
        self.lchild =  lchild                        #左孩子指针
        self.rchild = rchild                        #右孩子指针

class BiTree(object):
    '''二叉链表类'''
    def __init__(self , root=None) :
        self.root = root                         #根节点地址，默认值为空

    def ListCreatBiTree(self,Tlist) :
        '''将顺序存储的二叉树（列表）转换为二叉链表'''
        '''该方法调用前，主调程序需先实例化一个空树对象'''
        def CreatNode(i):                                   #i为列表起始下标
            if i >= len(Tlist) or  Tlist[i] == None:
                return None
        
            root = BiTNode( Tlist[i] )                    #创建父节点
            root.lchild = CreatNode(2 * i +1)      #创建左孩子结点
            root.rchild = CreatNode(2 * i +2)     #创建右孩子结点
            return root       
            #此处root为方法内的局部变量，和self.root不是同一个变量
        self.root=CreatNode(0)                #将建立的二叉链表保存到二叉树对象中

    def visit(self,point):
        '''访问节点的虚拟函数'''
        print(point.data, end=' ')                           #遍历时可以直接输出
        return point.data

    def preorder(self,cur):       
        '''递归实现先序遍历,cur为待遍历的二叉树根结点'''
        if cur:
            self.visit(cur)                             #访问结点
            self.preorder(cur.lchild)           #遍历左子树
            self.preorder(cur.rchild)          #遍历右子树

    def inorder(self,cur):
        '''递归实现中序遍历,cur为待遍历二叉树根节点'''
        if cur:
            self.inorder(cur.lchild)             #遍历左子树
            self.visit(cur)                           #访问结点
            self.inorder(cur.rchild)           #遍历右子树
         
    def postorder(self, cur):
        '''递归实现后序遍历,cur为待遍历二叉树根节点'''
        if cur: 
            self.postorder(cur.lchild)     #遍历左子树
            self.postorder(cur.rchild)     #遍历右子树
            self.visit(cur)                        #访问结点

    def CountLeaf(self):
        '''遍历统计二叉链表叶子结点的个数
        (使用可变数据类型用于多级递归之间参数的传递'''
 #将程序的递归调用部分作为实例方法内部的一个函数来设计。
#优点：①可以在实例方法内完成递归函数调用前的参数初始化，
#避免直接对实例方法递归调用；②方便各级递归函数之间参数传递 ；
# ③提高程序易读性。
        def Leaf(cur,count):        #递归调用函数 
            if cur:                #递归结束条件
                if  cur.lchild == None  and  cur.rchild == None:
                    count[0]+=1
                else:
                    Leaf(cur.lchild,count)
                    Leaf(cur.rchild,count)
        #递归调用前初始化
        count = [0]     #定义为可变数据类型，初值为零
        Leaf(self.root,count)   #递归调用
        return(count[0])          

    def Depth(self):
        '''后序遍历获得二叉树的深度（采用递归方式）'''

        def recur(cur):
            if cur == None:
                depthval = 0    #递归结束条件
            else:
                depthLeft    = recur(cur.lchild)
                depthRight = recur(cur.rchild)
                if depthLeft > depthRight:
                    depthval = depthLeft+1
                else:
                    depthval = depthRight+1
            return depthval

        cur = self.root         #递归程序调用前参数初始化
        return recur(cur)


    def CopyTree(self,Mtree):
        '''通过后序遍历复制二叉树，cur为母树'''
        '''结点的建立顺序：从左右叶子结点开始逐级回退到根节点。
        结点的处理和新建顺序是左、右、根，故采用的是后序遍历'''

        def GetTreeNode(data,lptr,rptr):
            '''生成二叉树的一个结点'''
            T = BiTNode()
            T.data = data
            T.lchild = lptr
            T.rchild = rptr
            return T

        def recur(cur):
            if  cur == None:                    #递归结束条件
                return None 
        #后序遍历过程中，保存父节点地址，用于后续建立父
            if cur.lchild:
                newlptr = recur(cur.lchild) #f复制左子树
            else:
                newlptr = None
            if cur.rchild:
                newrptr = recur(cur.rchild) #复制右子树
            else:
                newrptr =None
            #通过后序遍历建立左右子树
            newT = GetTreeNode(cur.data,newlptr,newrptr)  
            #生成父节点
            return newT

        self.root  = recur(Mtree.root)

#建立二叉树方法一：通过实例化嵌套方式，将二叉树中结点逐个添加到二叉树中
'''①枚举出全部结点，通过实例化嵌套方式建立二叉链表，实例化实参求值顺序：从左往右，从内向外
  ②结点建立顺序：C、B、F、E、D、A
  ③实参内结点的书写顺序，遵循二叉树的先根遍历顺序：A->B->C->D->E->F'''

Tree0 = BiTree( BiTNode( 'A', BiTNode( 'B', BiTNode('C')), BiTNode( 'D', BiTNode('E', BiTNode('F')))))   

#建立二叉树方法二：顺序存储转为二叉链表存储
'''因为是主调程序新建一棵二叉树，故应该由主调程序完成空二叉树对象实例化，
再调用空树对象的实例方法来创建结点，这样也方便编程。'''
Tree1 = BiTree()       #在一个空树中添加结点，故应首先实例化一颗空二叉树
Tree1.ListCreatBiTree( [3,9,20,None,None,15,7] )   #将列表元