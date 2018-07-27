# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    elif len(L) == 1:
        return (L[0],L[0])
    else:
        Max = Min = L[0]
        for x in L:
            print(x,Max,Min)
            if x >= Max:
                Max = x

            elif x <= Min :
                Min = x

        return (Min, Max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')