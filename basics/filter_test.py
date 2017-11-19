#extract even number using filter
def is_even(n):
    return n % 2 == 0
print(list(filter(is_even,range(20))))
