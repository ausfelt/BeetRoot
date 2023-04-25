import threading

class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for i in range(self.rounds):
            self.counter += 1
            print(self.counter)

# create two instances of the Counter thread and start them
t1 = Counter()
t2 = Counter()
t1.start()
t2.start()

# wait for the threads to finish
t1.join()
t2.join()

# print the final value of the counter
print(Counter.counter)


#I dont know why but i get 0 every time. Except if i change "counter" but then i just get the int i put there.

#When i put a print in the run function i get very mysterious results. But it works. But still not?