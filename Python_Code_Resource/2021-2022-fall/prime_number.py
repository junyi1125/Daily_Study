#找到素数，多少范围的都行
def prime_number():
    num_lst = []
    for i in range(1,100):#这里的range设置范围
        for x in range(2,i-1):
            if i % x == 0:
                break
        else:
            num_lst.append(i)
    print(num_lst)
prime_number()