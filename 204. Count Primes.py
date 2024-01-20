#方法一：虽然我的这个代码跑超时了，但是这个代码的思想非常重要，即a除以所有b的余数都不等于0的时候cnt+=1
'''
def countPrimes(n):
	cnt = 0
	a = 2
	flag = True
	while a < n:
		for b in range(2, a):
			if a % b == 0:
				flag = False
				break
			else:
				continue
		if flag == True:
			cnt += 1
		else:
			flag = True
		a += 1
	return cnt
result = countPrimes(10)
print(result)
'''
#方法二： 答案给的方法，这个也差点跑超时
'''
def countPrimes(n):
    if n <= 2:
        return 0
    res = [True] * n#原来列表还可以这么玩
    res[0] = res[1] = False
    for i in range(2, n):
        if res[i] == True:
            for j in range(2, (n-1)//i+1):#这个逻辑暂时先不看了，反正跑的时间这么长
                res[i*j] = False
    return sum(res)
result = countPrimes(10)
print(result)
'''
#答案给的另一种方法，这个跑的时间还挺快，不过这个方法得建立在一个不是很常见的数学公式上

def countPrimes(n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
            print(primes)
    return sum(primes)
result = countPrimes(20)
#print(result)
'''primes[2 * 2: 10:2] = [False] * len(primes[2 * 2: 10:2])

   primes[4, 6, 8]
   primes[3 * 3: 10:2] = [False] * len(primes[3 * 3: 10:3])
   primes[9]
'''