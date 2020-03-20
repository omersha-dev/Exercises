def countFours(list):
    counter = 0
    for element in list:
        if (element == 4):
            counter += 1
    return counter

someList = [4, 1, 2, 4, 4, 5, 4, 4, 5, 6, 3, 4]
print("The number 4 has been found %d times in the given list" % countFours(someList))