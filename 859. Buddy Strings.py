#这题出的有毛病,当A='abab', B='abab'时，应该输出false,但是样例里给的true
def buddyStrings(A, B):
    lst = []
    if len(A) != len(B):
        return False
    else:
        for index, elem in enumerate(zip(A, B)):
            if len(set(elem)) > 1:
                lst.append(index)
        if len(lst) == 0:
            return len(set(A)) != len(A) and len(A) == len(B) == 2
        elif len(lst) == 2:
            return A[lst[0]] == B[lst[1]] and B[lst[0]] == A[lst[1]]
        else:
            return False
result = buddyStrings('abab', 'abab')
print(result)
#是我理解错了，确实应该是A只交换一次，这一次里只交换两个字母就能得到B