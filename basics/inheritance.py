#parent class
class User:
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print("[parent method] Hi! {0}".format(self.name))

#inheritance class
class AdminUser(User):
    def __init__(self,name,age):
        """
        inferitance class can re-use parent (init) method
        #this referred same place of parent self.name
        """
        super().__init__(name)
        self.age = age

        #before the override of parent property
        print("to called name using super() in childern class is {0}".format(self.name))

        #after the override of parent property
        self.name = "Endo"
        print("to called name using super() after the override is {0}".format(self.name))

    def say_hello(self):
        print("Hello!! {0} age:{1}".format(self.name,self.age))

    def say_hi(self):
        print("[method after the overwirte in children method] hi {0}".format(self.name))

print("before the inheritance")
bob = User("Bob")
bob.say_hi()

print("after the inheritance")
bob = AdminUser("bob",22)
bob.say_hi()

print(bob.name)
#instance method of sab class
bob.say_hello()
#it override parent method 
bob.say_hi()


