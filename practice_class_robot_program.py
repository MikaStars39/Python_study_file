def robot_test():

    class Robot:

        population = 0

        def __init__(self, name):
            self.name = name
            print('Now we have a new robot called {}'.format(self.name))
            Robot.population += 1

        def die(self):
            # we kill robots here
            Robot.population -= 1
            if Robot.population == 0:
                print('{} is the last one'.format(self.name))
            else:
                print('{} has been killed'.format(self.name))
                print('there is still {:d} robots here'.format(self.population))

        def say_hi(self):
            print('Hi, my master call me {}'.format(self.name))

        @classmethod
        def how_many(cls):
            print('the number of the robots are {:d}'.format(cls.population))

    rbt01 = Robot('ET')
    rbt01.say_hi()
    rbt01.how_many()

    rbt02 = Robot('NM')
    rbt02.say_hi()
    rbt02.how_many()

    print('now we need to destroy all the robots')
    rbt01.die()
    rbt02.die()

    Robot.how_many()
