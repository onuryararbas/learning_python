#general format

#def name(parameters):
    #code, auto indentation
    #more code...

#when stop, we leave the function. no longer in name function

globalX = 5
def addOne(x):
    global globalX
    y = globalX + 1
    return y

start = 1
nextNumber = addOne(start)
print(start)
print(nextNumber)
