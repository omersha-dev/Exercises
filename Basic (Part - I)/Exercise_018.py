def calcThreeNums(a, b, c):
    sum = a + b + c
    if(a == b == c):
        return sum * 3
    else:
        return sum

print(calcThreeNums(1, 2, 3))
print(calcThreeNums(1, 1, 1))