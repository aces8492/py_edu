#function
def say_hi(name="default",age="-1"):
    print("{0} age({1})".format(name,age));
    return "complete";

#function call
say_hi();
say_hi(age=22);
msg = say_hi("tom",23);
print(msg);
