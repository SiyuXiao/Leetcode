'''
def plusOne(digits):
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            else:
            	digits[~i] = 0
        return [1] + [0] * len(digits)
result = plusOne([1, 9, 9])
print(result)
'''
#那个else可以省略，比如下面这个

def plusOne(digits):
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)
result = plusOne([1, 9, 9])
print(result)
