#class A,B -> C

class A:
    def say_a(self):
        print("in A")
    def say_hi(self):
        print("hi A")

class B:
    def say_b(self):
        print("in B")
    def say_hi(self):
        print("hi B")

class C(B,A):
    pass

instance_c = C()
instance_c.say_a()
instance_c.say_b()
'''
if exist same instance name in multiple inheritance, 
a class that earier specified have priority 
'''
instance_c.say_hi()
