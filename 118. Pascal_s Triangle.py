#Discuss解法1，这个解法比较好理解
def generate(numRows):
    n,b,res=0,[1],[]
    while n<numRows:
        res.append(b)
        b=[1]+[b[i]+b[i+1] for i in range(len(b)-1)]+[1]
        n+=1
    return res
result = generate(5)
print(result)

#Discuss解法2，这个解法执行的时间击败了100%的submissions
def generate(numRows):
    pascal = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal
result = generate(5)
print(result)
