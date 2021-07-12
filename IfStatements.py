#if booleanExpression:

testVariable = 10

if testVariable < 10:
    print("value is less than 10")
    print("Still in if")

print("no longer in if")

test2 = 20

if test2 < 20:
    print("Value is less than 20")

elif test2 == 20:
    print("Value is 20")
else:
    print("Value is greater than 20")
