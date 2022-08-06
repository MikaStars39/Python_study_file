def object_test():

    class Person:
        # init gives the Person access to edit or value it directly
        def __init__(self, name1):
            self.name = name1

        def say_hi(self):
            print('Hello, how are you? my name is', self.name)

    name = input()
    p = Person(name)
    # if we do not use init, we can only write as:
    # p = person()
    # p.name() = name
    p.say_hi()
