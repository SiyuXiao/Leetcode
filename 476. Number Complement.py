#我自己写的方法
'''
def findComplement(num):
    num1 = ''
    for a in bin(num)[2:]:
        if a == '0':
            num1 += '1'
        else:
            num1 += '0'
    return int(num1, 2)
result = findComplement(5)
print(result)
'''
#答案给的方法: 题目里给的数变成二进制最高位一定为1，
#所以i一定变成比这个二进制数多一位的二进制数，而且最高位是1，后面全是0
#i-1以后变成和这个二进制位数一样，但全是1的数
#这时候异或，就变成了二进制位相反的数
def findComplement(num):
    i = 1
    while i <= num:
        i = i << 1
    return (i - 1) ^ num
result = findComplement(5)
print(result)