def show_length(list):
    print("length of the list is {0}".format(len(list)))

scores = [40,50]

print(scores[0])
print(scores[1])

#show the list length
show_length(scores)

#add element to tail of the list
scores.append(100)
print(scores)
show_length(scores)

#show the num of element
print("show the num of element")
for i,score in enumerate(scores):
    print("[{0}]:{1}".format(i,score))

