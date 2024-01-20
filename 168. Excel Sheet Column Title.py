def convertToTitle(n):
    r = ''
    while(n>0):
        n -= 1
        r = chr(n%26+65) + r
        n //= 26
    return r
result = convertToTitle(701)
print(result)