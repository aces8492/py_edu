from package_test.iterator import get_infinite
#map

#This function tri-multiply num
def triple(n):
    return n*3

#use map(func,iter)
#cast for list (return of map is generator)
print(list(map(triple,[1,2,3])))

new_map = map(triple,[4,5,6])
print(new_map.__next__())

g = get_infinite()
print("maybe print 0,6,12,18...")
print(list(map(triple,get_infinite())))
