class Subscriber:
    def __init__(self, name):
        self.name = name
        print(f"Subscriber init is passed with parameter '{self.name}'")

    def update(self, message):
        print("Subscribers' update method displays message, confirming it was received")
        print('{} got message "{}"'.format(self.name, message))


class Publisher:
    def __init__(self):
        self.subscribers_set = set()
        print(f"Publisher init declares a set for subscribers: {self.subscribers_set}")

    def register(self, who):
        print(f"Publisher's register method takes 'who' parameter {who.name} and adds to set")
        self.subscribers_set.add(who)
        print(f"subscriber set: {self.subscribers_set}")

    def unregister(self, who):
        print(f"Publisher's unregister method removes 'who' parameter {who.name} from set")
        self.subscribers_set.discard(who)
        print(f"subscriber set: {self.subscribers_set}")

    def dispatch(self, message):
        print(f"Publisher's dispatch method passes message '{message}' to subscribers")
        for subscriber in self.subscribers_set:
            print(f"for each subscriber object in subscribers_set, call update() | {subscriber.name}")
            subscriber.update(message)


class SubscriberOne:
    def __init__(self, name):
        self.name = name
        print(f"SubscriberOne's init holds parameter of 'name' {self.name}")

    def update(self, message):
        print(f"SubscriberOne's update() method called with message {message}")
        print('{} got message "{}"'.format(self.name, message))


class SubscriberTwo:
    def __init__(self, name):
        self.name = name
        print(f"SubscriberTwo's init holds parameter of 'name' {self.name}")

    def receive(self, message):
        print(f"SubscriberTwo's receive() method called with message {message}")
        print('{} got message "{}"'.format(self.name, message))


class Publisher2:
    def __init__(self):
        self.subscribers_dict = dict()
        print(f"Publisher2's init creates dictionary for subscribers {self.subscribers_dict}")

    def register(self, who, callback=None):
        print(f"Publisher2's register method passes 'who' object '{who.name}' and callback={callback}")
        if callback == None:
            print(f"if callback==None, Publisher2's register calls getattr() with 'who' and 'update' as parameters, stores as 'callback'")
            callback = getattr(who, 'update')
        print(f"regardless of callback's value (({callback})), save callback value in subscriber_dict[who]")
        self.subscribers_dict[who] = callback
        print(self.subscribers_dict)

    def unregister(self, who):
        print(f"Publisher2's unregister method removes 'who' from subscribers_dict")
        del self.subscribers_dict[who]

    def dispatch(self, message):
        for subscriber, callback in self.subscribers_dict.items():
            print(f"for each subscriber, callback in subscribers_dict: (({subscriber})), {callback}")
            print(f"send message: {message}")
            callback(message)


class Subscriber3:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Subscriber3 {self.name}'s update method receives message of {message}")
        print('{} got message "{}"'.format(self.name, message))


class Publisher3:
    def __init__(self, events):
        # maps event names to subscribers
        # str -> dict
        print(f"'events' list passed to Publisher3's init: {events}")
        self.events = {event: dict()
                       for event in events}
        print(f"Publisher3's init creates dictionary of events | {self.events}")

    def get_subscribers(self, event):
        print(f"Publisher3's get_subscribers method takes event as parameter: {event}, returns events[event]: {self.events[event]}")
        return self.events[event]

    def register(self, event, who, callback=None):
        print(f"Publisher3's register method called with event (({event})), who (({who.name})) and callback {callback} as parameters")
        if callback == None:
            print(f"if callback==None, Publisher3's register calls getattr() with 'who' and 'update' as parameters, stores as 'callback'")
            callback = getattr(who, 'update')
        print(f"callback: {callback}")
        self.get_subscribers(event)[who] = callback
        print(f"regardless of callback's value, save in self.get_subscribers(event)[who]")
        print(self.get_subscribers(event)[who])

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self, event, message):
        print(self.get_subscribers(event))
        for subscriber, callback in self.get_subscribers(event).items():
            print(f"for each subscriber (({subscriber})) and callback {callback} in subscribers(event)dict:")
            print(f"send message: {message}")
            callback(message)