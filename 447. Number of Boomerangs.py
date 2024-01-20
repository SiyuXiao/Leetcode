def numberOfBoomerangs(points):
    count = 0
    for i in points:
        a={}#这个a={}放的位置很巧妙，是这个题思想的关键
        for j in points:
            c = (i[0]-j[0])**2+(i[1]-j[1])**2
            if c not in a:
                a[c]=1
            else:
                count += a[c] 
                a[c]+=1 
    return count*2
result = numberOfBoomerangs([[0,0],[1,0],[2,0]])
print(result)