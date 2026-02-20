

'''
#Dictionary
map = {1:['One',(1,2,3,4)], 2:'Two', 3:'Three'}

print(map)

#Accessing map
print(map.get(1))
print(map[1])

#length
print(len(map))

#keys
print(map.keys())

#values
print(map.values())

#items
print(map.items())

#insert
map[4] = 'Four'
print(map)  

#remove
map.pop(2)
print(map)
'''

map = {5: {'p': {5: "P"}, 6: "Q"},
      7:"R",
     'Q':"S", 
      "S":'T'}

print(map[map[map[5][6]]])