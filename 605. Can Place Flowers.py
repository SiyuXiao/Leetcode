#这个for循环里i没法跳，可以用while循环，比较给i设定一个值，if满足这个条件的时候i+2, if不满足这个条件的时候i+1
'''
def canPlaceFlowers(flowerbed, n):
    count = 0
    flowerbed = [0] + flowerbed + [0]
    for i in range(0, len(flowerbed) - 2):
        if flowerbed[i] == flowerbed[i+1] ==flowerbed[i+2]:
            count += 1
            i += 2
    return n <= count
result = canPlaceFlowers([1,0,0,0,0,1], 2)
print(result)
'''
#符合答案要求的代码

def canPlaceFlowers(flowerbed, n):
    count = 0
    flowerbed = [0] + flowerbed + [0]
    for i in range(0, len(flowerbed) - 2):
        if flowerbed[i] == flowerbed[i+1] ==flowerbed[i+2]:
            count += 1
            flowerbed[i+1] = 1
    return n <= count
result = canPlaceFlowers([1, 0, 0, 0, 0, 1], 2)
print(result)
