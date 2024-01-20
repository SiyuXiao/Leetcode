def addBinary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]
result = addBinary("11", "1")
print(result)