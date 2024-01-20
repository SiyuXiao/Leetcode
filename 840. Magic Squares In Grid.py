#这破题，我遇到了[[5,5,5],[5,5,5],[5,5,5]]这个测试样例就不好使了，看Discuss才发现输入得是distinct numbers
#还有这9个数得在1到9之间
def numMagicSquaresInside(grid):
	count = 0
	for i in range(len(grid)-2):
		for j in range(len(grid[0])-2):
			if sum(grid[i][j:j+3]) == sum(grid[i+1][j:j+3]) == sum(grid[i+2][j:j+3]) \
			== sum([grid[i][j], grid[i+1][j], grid[i+2][j]]) == \
			sum([grid[i][j+1], grid[i+1][j+1], grid[i+2][j+1]]) == \
			sum([grid[i][j+2], grid[i+1][j+2], grid[i+2][j+2]]) \
			==sum([grid[i][j], grid[i+1][j+1], grid[i+2][j+2]]) == sum([grid[i][j+2], grid[i+1][j+1], grid[i+2][j]]):
				count += 1
	return count
result = numMagicSquaresInside([[4,3,8,4], [9,5,1,9], [2,7,6,2]])
print(result)

#这个写法很好理解
'''
def numMagicSquaresInside(grid):
    res = 0
    for i in range(len(grid)-2):
        for j in range(len(grid)-2):
            if sum(grid[i][j:j+3]) == sum(grid[i+1][j:j+3]) == sum(grid[i+2][j:j+3]) \
            == sum(grid[k][j] for k in range(i,i+3)) == sum(grid[k][j+1] for k in range(i, i+3)) \
            == sum(grid[k][j + 2] for k in range(i, i + 3)) \
            == (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]) \
            == (grid[i+2][j]+ grid[i + 1][j + 1] + grid[i][j + 2]) and \
            set(grid[i][j: j + 3] + grid[i + 1][j: j +3] + grid[i + 2][j:j + 3]) \
            == {1,2,3,4,5,6,7,8,9}: res += 1
    return res
result = numMagicSquaresInside([[4,3,8,4], [9,5,1,9], [2,7,6,2]])
print(result)
'''