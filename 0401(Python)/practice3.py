print("2016112234 서예현")

x = "awesome"

def myfunc1():
    x = "cool"
    print("1, Computer is " + x)

def myfunc2():
    global y
    y  = "fantastic"
    print("2, Computer is " + x)

myfunc1()
myfunc2()
print("3, Computer is " + y)