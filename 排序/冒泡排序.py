# 每进行一轮比较会把一个最大（或最小）的冒泡到最后一个位置
# 那么，下一轮比较的个数会减小1个
# 时间复杂度：O(n^2)
# range(6,0,-1):[6,5,4,3,2,1];
def Bubble(a):
    lens = len(a)
    for i in range(lens-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

# 测试
a = [1,4,8,2,5,3,7]
print(Bubble(a))