#之所以乘以64，是因为这样m再大，加上h，也只能填充到h的后6个0，不影响h的1，其实只要是大于等于64，并且是2的n次幂的数都行，比如128
def readBinaryWatch(num):
    output = []
    for h in range(12):
        for m in range(60):
            if bin(h * 64 + m).count('1') == num:
                output.append('%d:%02d' % (h, m))
    return output
result = readBinaryWatch(1)
print(result)
