class negExcept(Exception):
    pass

def fibonacci(depth):
    try:
        if(depth < 0):
            raise negExcept("can't use negative value")

    except negExcept as e:
        print (e)

    else:
        depth = int(depth)
        if depth == 0 or depth == 1:
            return 1
        else:
            return fibonacci(depth-2) + fibonacci(depth-1)

start_num = int(input("Enter the start number : "))
end_num = int(input("Enter the end number : "))

print(list(map(fibonacci, range(start_num, end_num))))

