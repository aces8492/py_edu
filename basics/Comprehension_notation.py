#comprehension notation (C_N)
#range() is iterable
print([i for i in range(10)])

#generate range object
print(range(10))
#making list from iterable (range object)
print(list(range(10)))


#using C_N map like usage
print([i*3 for i in range(10)])
#same processing using map
print(list(map(lambda x:x*3,range(10))))

#using C_N filter like usage
print([i*3 for i in range(10) if i % 2 == 0])
#same processing using map
print(list(filter(lambda i:i%2==0,map(lambda x:x*3,range(10)))))

#to try one-liner (it isn't readable ...)
print([i if i % 2 == 0 else "skip 3" if i == 3 else "skip" for i in map(lambda x:x*3,range(10))])
print([i*3 if i % 2 == 0 else "skip 3" if i == 3 else "skip" for i in range(10)])

#C_N for list
print({i*3 for i in range(10) if i % 2 == 0})


print(i*3 for i in range(10) if i % 2 == 0) 

