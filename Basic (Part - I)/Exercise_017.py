def checkThousandRange(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

print(checkThousandRange(1000))
print(checkThousandRange(900))
print(checkThousandRange(800))
print(checkThousandRange(2200))