print('2016112234 서예현')

fruitlist = ['banana','orange','kiwi','cherry']

fruitlist.reverse()
print('reverse() -> ', fruitlist)

fruitlist.sort()
print('sort() -> ', fruitlist)

fruitlist.sort(key=str.lower)
print('reverse(key=str.lower) -> ', fruitlist)