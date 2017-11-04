#import module 'module_test.py' in package 'package_test' 
import package_test.module_test as MT
from package_test.module_test import AdminUser

tom = MT.User("tom")
bob = AdminUser("bob",23)

tom.say_hi()
print(bob.name)
bob.say_hi()
bob.say_hello()


