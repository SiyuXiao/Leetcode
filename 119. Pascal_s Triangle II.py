#下面这两个程序时间复杂度都是n2
'''
def getRow(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        row = [x + y for x, y in zip([0]+row, row+[0])]
        print(row)
    return row
result = getRow(3)
#print(result)
'''

'''
def getRow(rowIndex):
    row = [1]
    for i in range(1, rowIndex + 1):
        row = [1] + [ row[x] + row[x - 1] for x in range(1, i)] + [1]
        print(row)
    return row
result = getRow(3)
#print(result)
'''