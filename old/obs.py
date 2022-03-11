from observer import Publisher, Subscriber
from observer import Publisher2, SubscriberOne, SubscriberTwo
from observer import Publisher3, Subscriber3

pub = Publisher()

bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

pub.register(bob)
pub.register(alice)
pub.register(john)

pub.dispatch("It's lunchtime!")

pub.unregister(john)

pub.dispatch("Time for dinner")
print(" ")

"""-----------------------------------"""

pub2 = Publisher2()
larry = SubscriberOne('Larry')
curly = SubscriberTwo('Curly')
moe = SubscriberOne('Moe')
print(" ")

print(f"Publisher2's register method called with 'who' object of 'larry' and callback value of larry.update")
pub2.register(larry, larry.update)
print(" ")
print(f"Publisher2's register method called with 'who' object of 'curly' and callback value of curly.receive")
pub2.register(curly, curly.receive)
print(" ")
print(f"Publisher2's register method called with 'who' object of 'moe' and no callback value")
pub2.register(moe)
print(" ")

print(f"Publisher2's dispatch method called with message 'It's lunchtime' as parameter")
pub2.dispatch("It's lunchtime!")
print(" ")
pub2.unregister(curly)
print(" ")
print(f"Publisher2's dispatch method called with message 'Time for dinner' as parameter")
pub2.dispatch("Time for dinner")
print(" ")

"""--------------------------------------"""
print("Publisher3 instantiated with 'lunch' and 'dinner' passed as list parameter")
pub3 = Publisher3(['lunch', 'dinner'])
print("Subscriber3 object 'bob' instantiated with 'Bob' as parameter")
bob = Subscriber3('Bob')
print("Subscriber3 object 'alice' instantiated with 'Alice' as parameter")
alice = Subscriber3('Alice')
print("Subscriber3 object 'john' instantiated with 'John' as parameter")
john = Subscriber3('John')
print(" ")

print("Publisher3's register method called with 'lunch' and bob as parameters")
pub3.register("lunch", bob)
print(" ")
print("Publisher3's register method called with 'dinner' and alice as parameters")
pub3.register("dinner", alice)
print(" ")
print("Publisher3's register method called with 'lunch' and john as parameters")
pub3.register("lunch", john)
print(" ")
print("Publisher3's register method called with 'dinner' and john as parameters")
pub3.register("dinner", john)
print(" ")

print("Publisher3's dispatch method called with 'lunch' and 'It's lunchtime' as parameters")
pub3.dispatch("lunch", "It's lunchtime!")
print("Publisher3's dispatch method called with 'dinner' and 'Dinner is served' as parameters")
pub3.dispatch("dinner", "Dinner is served")