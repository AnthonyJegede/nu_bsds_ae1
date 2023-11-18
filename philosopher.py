#Import libraries sesction
import threading
import time

#Create constant variables that are needed and set maximum values
#for objects and behaviours. These preset values can be used to 
#observe the behaviour of the program under different parameters.
THNK_SECS = 3
TOTAL_PHILS = 4
EAT_SECS = 4

#Create the Philosopher class which inherits from threading.Thread, 
# and with a constructor that runs by default
#whenever the class in instantiated with no custom values.
class Philosopher(threading.Thread):
    def __init__(self, index, fork1, fork2):
        threading.Thread.__init__(self)
        self.index = index
        self.fork1 = fork1
        self.fork2 = fork2

#Define other methods for this class to simulate the behaviour of
#the object, as shown on the UML class diagram.
    def run(self):
        while True:
            self.think()
            self.eat()

    def think(self):
        print(f"Philosopher {self.index} : Can't eat now, I'm thinking")
        time.sleep(THNK_SECS)
        
#The eat function first prints to indicate that a philosopher 
#is starving before starting to eat. This helps to understand the
#thread operation better while the application is doing while running
    def eat(self):
        print(f"Philosopher {self.index} : I'm starving")
        with self.fork1:
            with self.fork2:
                print(f"Philosopher {self.index} : Can't think now, I'm eating")
                time.sleep(EAT_SECS)
        print(f"Philosopher {self.index} : I'm done eating")

#The main function that runs to kick off the program.
#create the number of philosophers specified by TOTAL_PHILS
#Start the threads, then call the join method on the 
# philosopher instances,to make the thread wait until the 
# current thread is completed

def main():
    forks = [threading.Lock() for _ in range(TOTAL_PHILS)]
    philosophers = [Philosopher(i, forks[i], forks[(i + 1) % TOTAL_PHILS]) for i in range(TOTAL_PHILS)]

    for philosopher in philosophers:
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()

if __name__ == "__main__":
    main()
