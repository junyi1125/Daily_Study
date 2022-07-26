def BilnsertionSort(R):
    for i in range(2, len(R)):
        R[0] = R[i]  # 将R[i]暂存到R[0]
        '''在R[1...i-1]中折半查找插入位置的语句段'''
        low = 1
        high = i-1
        while low <= high:
            m = (low+high)//2  # 折半

            if R[0] < R[m]:
                high = m-1  # 插入点在低半区
            else:
                low = m+1  # 插入点在高半区

        if R[i] > R[m]:
            m += 1
        '''在R[1...i-1]中折半查找插入位置m'''
        for j in range(i-1, m-1, -1):  # 从下标i-1开始，逆序至下标m，逐个元素后移
            R[j+1] = R[j]  # 记录后移
        R[m] = R[0]  # 插入


a = [None, 23, 14, 34, 10, 80, 54, 76, 27, 67, 58,
     34, 61, 8]  # a[0]的None是为了设置一个空的位置，把R[i]暂存在那个地方
BilnsertionSort(a)
print(a)
