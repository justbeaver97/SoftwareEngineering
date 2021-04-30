def func(*args, **kwargs):
    for x in args:
        print(x,end='  ')
    print('My Name : ', kwargs['name'], ' & My Age : ', kwargs['age'])
func(1,2,3,4, name='YeHyun', age=25)
#1  2  3  4  My Name :  YeHyun  & My Age :  25

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result,end = ' ')
    else:   result = 0
    return result
tri_recursion(6)
