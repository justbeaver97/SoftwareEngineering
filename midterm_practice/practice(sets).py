mscset = {"math", "science", "computer"}
print(mscset)   #{'computer', 'science', 'math'} -> 순서가 없음

set4 = {"abc", 34, True, 40, "def"} # mix variable types

mscset.add("algorithm")
print(mscset)

mscset.discard('algorithm')
print(mscset)

x = {"math", "science", "computer"}
y = {"computer", "algorithm", "software"}
z = x.intersection(y)               #{'computer'}
z2 = x.symmetric_difference(y)      #{'software', 'math', 'algorithm', 'science'}

