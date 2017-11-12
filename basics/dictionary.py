#dictionary 
sales = {"taguch":200, "fkoji":400}
print (sales["taguch"])

# change value
sales["taguch"] = 400
print (sales["taguch"])

# add value
sales["dot"] = 400
print(sales)

# del value
del(sales["fkoji"])
print(sales)

# search key and value using items()
for key,value in sales.items():
    print("{0}:{1}".format(key,value))
