msctuple = ('math','science','computer')    #('math', 'science', 'computer')
print(type(msctuple))   #<class 'tuple'>
thistuple = ("math")
print(type(thistuple))  #<class 'str'>

tuple1 = ("abc", 34, True, 40, "def")

#tuple은 값 변경 불가능
x = ("math", "science", "computer")
y = list(x)             # tuple -> list
y[1] = "science2"       # change values of the second element.
x = tuple(y)            # 다시 list -> tuple
print(x)                #('math', 'science2', 'computer')

(m, s, c) = msctuple
print(m) # print ‘math’
print(s) # print ‘science’
print(c) # print ‘computer’

msctuple2 = ("math", "science", "computer" , "algorithm", "software")
(m, s, *c) = msctuple2
print(m) # print ‘math’
print(s) # print ‘science’
print(c) # print [“computer”, “algorithm”, “software” ] -> list로 할당

