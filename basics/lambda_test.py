#normally lambda
#return n*2
myfunc = lambda x:x*2

print(myfunc(2))
print(myfunc(4))

#lambda with map
li = [1,2,3,4]
#lambda using in map and conv iter to map
li2 = list(map(lambda n:n*5,li))
#li2 = map(lambda n:n*5,li)
#for element in li2:
#    print(element)
print(li)
print(li2)

#one line
print(list(map(lambda n:n*n,[1,2,3])))
