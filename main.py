import random
import time
import math

names = [
    "Bob",
    "Clark",
    "qwertyuiopasdfghjklzxcvbnm",
    "Joe",
    "Emily",
    "Sarah",
    "Jim",
    "Poseidon",
    "Nicole"
]

def decelerate_repeat():
    delay = 0

    for i in range(10):
        # random number
        index = random.randint(0, 8)
        
        name_web(index)

        # delay
        time.sleep(delay)
        delay = delay + 0.1

        print('\033c', end='') # clear terminal
    
    # random number
    index = random.randint(0, 8)
    
    name_web(index)

def name_web(selectedNumber):
    for i in range(len(names)):
        if i % 3 == 0: 
            start = random.randint(1, 5)
            print('~' * start, end='')

        nLength = len(names[i])
        if i == selectedNumber:
            print(names[i][:20].upper(), end='')
        else:
            print(names[i][:20].lower(), end='')

        print('~' * (20 - nLength), end='')
        
        if i % 3 == 2: 
            print('~' * (5 - start))


decelerate_repeat()
