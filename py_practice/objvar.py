class Robot :
    population = 0
    
    def __init__(self, name):
        self.name = name
        print("(Initialising {0})".format(self.name))
        Robot.population += 1

    def die(self):
        print("{0} is being destroyed".format(self.name))
        Robot.population -= 1
        
        if Robot.population == 0:
            print("{0} was the last one.".format(self.name))
        else:
            print("There are still {0:d} robots working".format(Robot.population))

    def sayHi(self):
        print("Greetings, my master call me {0}".format(self.name))

    @classmethod
    def howMany(cls):
        print("We have {0:d} robots".format(cls.population))
        
droid1 = Robot("R2-D2")
droid1.sayHi()
droid1.howMany()

droid2 = Robot("C-3PO")
droid2.sayHi()
droid2.howMany()

print("\n Robots can do some work here")
print("\nRobots have done their work lets destroy them.\n")

droid1.die()
droid2.die()

Robot.howMany()
