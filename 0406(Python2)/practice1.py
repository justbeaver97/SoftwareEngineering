print('2016112234 서예현')

msclist = ['math','science','computer']
print('Original List: ', msclist)

msclist.insert(1,'algorithm')
print('insert(1,"algorithm") : ', msclist)

msclist.append('algorithm2')
print('append("algorithm") : ', msclist)

msclist.remove('science')
print('remove("science") : ', msclist)

msclist.pop()
print('pop() : ', msclist)

del msclist[0]
print('del msclist[0] : ',msclist)

msclist.clear()
print('clear() : ',msclist)