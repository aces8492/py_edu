#global scope
msg = "Hello global!";

def say_hi():
    #local scope
    #msg = "Hello Local!";
    #print (msg);
    """
    normally, function can't rewrite global var 
    however, function can rewrite this using 'global' i
    """
    global msg;
    msg = "global 2 local";
    print(msg);

say_hi();
print(msg);
