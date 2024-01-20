#这个程序我写了好多遍才写出来，最开始用的字典，后来改用一个列表，最后又用了两个列表
#[0,0,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0]，这个测试样例使我抛弃了用字典的想法
#[0,1,1,1,0,0,1,0,0]，这个测试样例促使我又多用了一个列表
'''
def maxDistToClosest(seats):
    A = []
    B = []
    cnt = 0
    seats = seats + [1]
    for i in range(len(seats)):
        if seats[i] == 0:
            cnt += 1
        else:
            A.append(cnt)
            cnt = 0
    else:
        if max(A) % 2 == 1:
            B.append((max(A) // 2) + 1)
        else:
            B.append((max(A) // 2))
    B.append(A[0])
    B.append(A[-1])
    return max(B)
print(maxDistToClosest([0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1]))
'''


#Discuss里的方法，我觉得这个方法很巧妙
def maxDistToClosest(seats):
    left, count, _max_distance = -1, 0, 1
    for i, x in enumerate(seats):
        if x == 0:
            count += 1
        else:
            if left < 0:
                distance = count
            else:
                distance = count // 2 + count % 2
            left, count = i, 0
            _max_distance = max(_max_distance, distance)
    return max(_max_distance, count)
print(maxDistToClosest([1,0,0,0]))