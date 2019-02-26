

v = [0,3,5,1,6,8] # 每个物品的价值，第1个0不算上
w = [0,12,34,9,10,22]  #每个物品的质量，第1个0不算
n = 5 #物品个数
weight = 50  #背包容量
index = [0 for i in range(n+1)]
optp = [[0 for col in range(weight+1)] for row in range(n+1)]  #最优
def package(v,w,n,totalWeight):
    for i in range(1,n+1):
        for j in range(1,totalWeight+1):
            if w[i]<j:
                optp[i][j] = max(optp[i-1][j], v[i]+optp[i-1][j-w[i]])
            else:
                optp[i][j] = optp[i-1][j]


    # 递推装入背包的物体：
    j = totalWeight
    for i in range(n,0,-1):
        if optp[i][j]>optp[i-1][j]:
            index[i] = 1
            j = j- w[i]

    print('选中物品的标号：', index)


    # 矩阵的最后一个元素是背包放的总重量
    return optp[-1][-1]


res = package(v,w,n,weight)
print(res)
