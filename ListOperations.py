listVariable = [1,2,3]
secondList = ["Hello", True]

jointList = listVariable + secondList + ["End"]
print(jointList)


print(jointList[0:3])


jointList[2] = 50
print(jointList)

jointList.append(10)
print(jointList)
