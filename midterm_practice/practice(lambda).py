def myfunc(n):
    return lambda a: a*n
mydoubler = myfunc(2)
print(mydoubler(5))     #10
mytripler = myfunc(3)
print(mytripler(5))     #15

input_list = [[2, 6], [1, 2], [3, 4], [5, 3], [4, 1]]
print(sorted(input_list, key=lambda x : -x[1]))     #[[2, 6], [3, 4], [5, 3], [1, 2], [4, 1]]
print(sorted(input_list, key=lambda x : x[0]))      #[[1, 2], [2, 6], [3, 4], [4, 1], [5, 3]]