phonedict = {
  "brand": "Apple",
  "model": "iphone 12",
  "year": 2020
}
x = phonedict.get("model")      #iphone 12
x = phonedict.keys()            #dict_keys(['brand', 'model', 'year'])
phonedict["color"] = "white"    #dict_keys(['brand', 'model', 'year', 'color'])
y = phonedict.values()          #dict_values(['Apple', 'iphone 12', 2020, 'white'])
phonedict["year"] = 2021        #dict_values(['Apple', 'iphone 12', 2021, 'white'])
z = phonedict.items()           #dict_items([('brand', 'Apple'), ('model', 'iphone 12'), ('year', 2021), ('color', 'white')])
phonedict.update({"year":2022}) #dict_items([('brand', 'Apple'), ('model', 'iphone 12'), ('year', 2022), ('color', 'white')])
phonedict.pop("model")          #dict_items([('brand', 'Apple'), ('year', 2022), ('color', 'white')])
phonedict.popitem()             #dict_items([('brand', 'Apple'), ('year', 2022)])
del phonedict["year"]           #dict_items([('brand', 'Apple')])
phonedict.clear()               #dict_items([])
del phonedict                   #dictionary 삭제

phonedict = {
  "brand": "Apple",
  "model": "iphone 12",
  "year": 2020
}
mydict = phonedict.copy()       #dictionary 복제
mydict2 = dict(phonedict)       #dictionary 복제

phone1 = {"model":"iphone 11","year":2019}
phone2 = {"model":"iphone 12","year":2020}
phone3 = {"model":"galaxy s21","year":2021}
myphone = {
  "phone1" : phone1,
  "phone2" : phone2,
  "phone3" : phone3
}