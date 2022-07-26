class Stack:
    def __init__(self):
        self.stack = []

    def StackEmpty(self):
        return self.stack == []

    def StackLength(self):
        return len(self.stack)

    def GetTop(self):
        if self.StackEmpty() == True:
            return 0
        else:
            self.stack[-1]

    def ClearStack(self):
        self.stack = []

    def Push(self, value):
        self.stack.append(value)

    def Pop(self):
        if self.StackEmpty() == True:
            return 0
        else:
            self.stack.pop()

    def matching(exp):
        state = True
        i = 0
        ch = exp[i]
        S = Stack()

        while ch != '#' and state:
            if ch == '(' or ch == '[':
                S.Push(ch)
                i += 1
                ch = exp[i]
                continue

            if ch == ')':
                if not S.StackEmpty() and S.GetTop() == '(':
                    S.Pop()
                    i += 1
                    ch = exp[i]
                    continue
                else:
                    state = 0
                    break

            if ch == ']':
                if not S.StackEmpty() and S.GetTop() == '[':
                    S.Pop()
                    i += 1
                    ch = exp[i]
                    continue

                else:
                    state = 0
                    break

        if S.StackEmpty() and state:
            return True
        else:
            return False


exp = ('[', '}', ']', ')', '{', '#')
Stack.matching(exp)
print(exp)
