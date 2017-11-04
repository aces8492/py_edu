#create exception handle
class negExcpept(Exception):
    pass

#exception handle
def div(a,b):
    try:
        if(b < 0):
            raise negExcpept("can't use negative value")

        #0 division
        #print (a/b)
    except ZeroDivisionError:
        print("can't zero division")

    except negExcpept as e:
        print (e)

    else:
        print("no exception")
    finally:
        print("-- process end --")

print("10/-3")
div(10,-3)
print("10/0")
div(10,0)

