# class Subscriber:
#     def __init__(self, name):
#         self.name = name
#         # print(f"SubscriberOne's init holds parameter of 'name' {self.name}")
#
#     def update(self, message):
#         print(f"SubscriberOne's update() method called with message {message} | : {self}")
#         print('{} got message "{}"'.format(self.name, message))
#
# class Publisher:
#     def __init__(self):
#         self.subscribers_dict = dict()
#         # print(f"Publisher2's init creates dictionary for subscribers {self.subscribers_dict}")
#
#     def register(self, who, callback=None):
#         # print(f"Publisher2's register method passes 'who' object '{who.name}' and callback={callback}")
#         if callback == None:
#             # print(f"if callback==None, Publisher2's register calls getattr() with 'who' and 'update' as parameters, stores as 'callback'")
#             callback = getattr(who, 'update')
#         # print(f"regardless of callback's value (({callback})), save callback value in subscriber_dict[who]")
#         self.subscribers_dict[who] = callback
#         # print(self.subscribers_dict)
#
#     def unregister(self, who):
#         # print(f"Publisher2's unregister method removes 'who' from subscribers_dict")
#         del self.subscribers_dict[who]
#
#     def dispatch(self, message):
#         for subscriber, callback in self.subscribers_dict.items():
#             print(f"for each subscriber, callback in subscribers_dict: (({subscriber})), {callback}")
#             print(f"send message: {message}")
#             callback(message)
#
#
# # if __name__ == "__main__":
#     # pub2 = Publisher()
#     # larry = Subscriber('Larry')
#     # # curly = SubscriberTwo('Curly')
#     # moe = Subscriber('Moe')
#     # print(" ")
#     #
#     # print(f"Publisher2's register method called with 'who' object of 'larry' and callback value of larry.update")
#     # pub2.register(larry, larry.update)
#     # print(" ")
#     # # print(f"Publisher2's register method called with 'who' object of 'curly' and callback value of curly.receive")
#     # # pub2.register(curly, curly.receive)
#     # # print(" ")
#     # print(f"Publisher2's register method called with 'who' object of 'moe' and no callback value")
#     # pub2.register(moe)
#     # print(" ")
#     #
#     # print(f"Publisher2's dispatch method called with message 'It's lunchtime' as parameter")
#     # pub2.dispatch("It's lunchtime!")
#     # print(" ")
#     # # pub2.unregister(curly)
#     # # print(" ")
#     # print(f"Publisher2's dispatch method called with message 'Time for dinner' as parameter")
#     # pub2.dispatch("Time for dinner")
#     # print(" ")