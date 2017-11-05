score_lists = [40,50,60,70,100]
score_tuple = (40,50,60,70,100)

print("Value and this num")
for i,score in enumerate(score_lists):
    print("{0}:{1}".format(i,score))

print("specify start and end point of value 1 to 4")
print("list : {0}".format(score_lists[1:4]))
print("tuple : {0}\n".format(score_tuple[1:4]))

print("only specify end point")
print("{0}\n".format(score_lists[:2]))

print("only specify start point")
print("{0}\n".format(score_lists[3:]))

print("show 3 elements from tail of lists")
print("{0}\n".format(score_lists[-3:]))

#this can use string
s = "Hello"
print(s[2:4])


