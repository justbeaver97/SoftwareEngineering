arr = ['math','science','computer']
print(type(arr))    #<class 'list'>

arr2 = ['abc' ,35 ,True ,40, 'def']     #['abc', 35, True, 40, 'def']

if True in arr2:
    print("True")   #True

arr[1:2] = ['korean', 'english']  #['math', 'korean', 'english', 'computer']

arr2.extend(arr)    #['abc', 35, True, 40, 'def', 'math', 'korean', 'english', 'computer']
arr2.pop(3)         #['abc', 35, True, 'def', 'math', 'korean', 'english', 'computer']
del arr2[0]         #[35, True, 'def', 'math', 'korean', 'english', 'computer']
del arr2            #arr2 삭제
arr.clear()         #[]

fruitlist = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruitlist.sort()
print(fruitlist)    #['banana', 'kiwi', 'mango', 'orange', 'pineapple']
fruitlist.reverse()
print(fruitlist)

def myfunc(n):
    return abs(n - 50)
numlist = [100, 50, 65, 82, 23]
numlist.sort(key = myfunc)
print(numlist)      #[50, 65, 23, 82, 100]