startVariable = 0
while True:
    startVariable += 1
    if startVariable > 10:
        break

testList = [1,5,5,7]
for element in testList:
    if element == 5:
        continue
    print(element)
