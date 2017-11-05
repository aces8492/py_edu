#list
items_list = [50,80,450]
#tuple
items_tuple = (50,"apple",32.5)

for item in items_tuple:
    print(item)

#it can't re-write value of tuple
#items[0] = 20

#convert list <-> tuple
print(list(items_tuple))
print(tuple(items_list))

tuple2list = list(items_tuple)
tuple2list[0] = "banana"
print(tuple2list)
