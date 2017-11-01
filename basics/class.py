#class
#empty class
"""
class User:
    pass
"""

#Constructor
class User:
    #class variable
    count = 0
    #initializer
    def __init__(self,name):
        User.count += 1
        #instance varialbe
        self.name = name
        self.__private = name*3

    #instance method can use instance variables (self)
    def say_hi(self):
        print("hi! {0}".format(self.__private))

    #It can use class method without instanciation
    @classmethod #decorator
    def show_info(cls):
        print("{0}:instances".format(cls.count))

#It can call class variable without instanciation
print("Initial count is {0}".format(User.count))

tom = User("Tom Jyon")
tom.score = 20
#Instances can call class variable because it is class property
print("Count of Tom is {0}".format(tom.count))

bob = User("bob")
bob.level = 10

tom.say_hi()
print(tom.name)
print(tom.score)
#It can't show private varialbe
#print(tom.__private)

bob.say_hi()
print(bob.name)
print(bob.level)

print("Final count is {0}".format(User.count))
print("\n{0}".format(User.show_info()))
