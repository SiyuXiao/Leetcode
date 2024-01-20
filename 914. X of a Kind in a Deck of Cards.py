#这个问题本质上是一个求最大公约数的问题
def hasGroupsSizeX(deck):
    deck.sort()
    deck1 = list(set(deck))
    cnt = []
    cd = []#cd means 'common divisor'
    for a in deck1:
        cnt.append(deck.count(a))
    gcd = min(cnt)#gcd means 'great common divisor'
    if gcd < 2:
        return False
    else:
        flag = True
        while gcd >= 2:
            for b in cnt:
                if b%gcd != 0:
                    flag = False
                    break
                else:
                    continue
            if flag == True:
                cd.append(gcd)
            else:
                flag = True
            gcd -= 1
    return cd != []
result = hasGroupsSizeX([1,1,1,2,2,2,3,3])
print(result)
