scores = [40,50,70,90] 
# calling iterator
it = iter(scores)

print("use itr")
print(next(it))
print(next(it))
print("Hello itr")
print(next(it))
print(next(it))

print("use for")
for score in scores:
    print(score)

"make generator"
def get_infinite():
    i = 0
    while True:
        yield i*2
        i += 1

g = get_infinite()

for i in range(0,6):
    print(next(g))

