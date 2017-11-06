a1 = {1,3,5,8}
b1 = {3,5,4,9}

for i,a in enumerate(a1):
    print("a{0}:{1}".format(i,a))

for i,b in enumerate(b1):
    print("b{0}:{1}".format(i,b))

print("(|):Union set")
print(a1|b1)
print("(&):Intersection set")
print(a1&b1)
print("(-):Difference set")
print(a1-b1)

