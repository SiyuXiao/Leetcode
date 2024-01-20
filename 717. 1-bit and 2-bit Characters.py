#从倒数第二个数开始往前数“1”的个数，直到遇到第一个'0'
#这时候如果'1'的个数是偶数，那么结果是True，否则是False
def isOneBitCharacter(bits):
    count=0
    for i in range(len(bits)-2,-1,-1):
        if bits[i]==1: count+=1
        else: break
    if count%2==1: return False
    else: return True
print(isOneBitCharacter([0, 1, 1, 0]))
#[1, 1, 1, 0]
#[1, 0, 0]
#[0, 1, 1, 0]