print("2016112234 서예현")

def func(*args, **kwargs):
    for x in args:
        print(x)
    print('My Name : ', kwargs['name'], ' & My Age : ', kwargs['age'])

func(1,2,3,4, name='YeHyun', age=25)