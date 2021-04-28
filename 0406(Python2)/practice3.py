print('2016112234 서예현')

phonedict={
    'brand':'apple',
    'model':'iphone 12',
    'year':2020
}

print('phone dictionary : ',phonedict)

phonedict['color']='red'
print('add new element -> ', phonedict)

x = phonedict.get('model')
print('get("model") -> ',x)

x = phonedict.keys()
print('keys method -> ',x)

x = phonedict.values()
print('values method -> ',x)

x = phonedict.items()
print('items method -> ',x)