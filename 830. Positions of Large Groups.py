def largeGroupPositions(S):
    S = S + '0'
    new = []
    new1= []
    new2 = []
    for i in range(0, len(S) - 1):
        if S[i] == S[i+1]:
            new.append(i)
        else:
            new.append(i)
            if new[-1] - new[0] >= 2:
                new1.append(new[0])
                new1.append(new[-1])
                new2.append(new1)
                new1 = []
            new = []
            
    return new2
result = largeGroupPositions("abcdddeeeeaabbbcd")
print(result)