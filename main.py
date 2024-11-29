import random
import time
import math
import sys

#* declaring variables *#
names = [
    "Bob",
    "Clark",
    "qwertyuiopasdfghjklzxcvbnm",
    "Joe",
    "Emily",
    "Sarah",
    "Jim",
    "Poseidon",
    "Nicole",
    "Henry",
    "Jeremy",
    "Pig",
    "Bard",
    "Kevin",
    "Seargent",
    "Stuart",
    "Gobble",
    "Zeus"
]
chosenName = ""


#* declaring functions *#

def call_error(param, errorType='none', minR=0, maxR=0):
    """error message"""

    print('\033c', end='') # clear terminal

    # something went wrong (Fire Font-k)
    print('')                                                                                                             
    print('                           )    )                                           )                                   ')
    print('             )      (   ( /( ( /( (          (  (    (  (      (         ( /(   (  (    (                (  (   ')
    print(' (    (     (      ))\\  )\\()))\\()))\\   (     )\\))(   )\\))(    ))\\  (     )\\())  )\\))(   )(    (    (     )\\))(  ')
    print(' )\\   )\\    )\\  \' /((_)(_))/((_)\\((_)  )\\ ) ((_))\\  ((_)()\\  /((_) )\\ ) (_))/  ((_)()\\ (()\\   )\\   )\\ ) ((_))\\  ')
    print('((_) ((_) _((_)) (_))  | |_ | |(_)(_) _(_/(  (()(_) _(()((_)(_))  _(_/( | |_   _(()((_) ((_) ((_) _(_/(  (()(_) ')
    print('(_-</ _ \\| \'  \\()/ -_) |  _|| \' \\ | || \' \\))/ _` |  \\ V  V // -_)| \' \\))|  _|  \\ V  V /| \'_|/ _ \\| \' \\))/ _` |  ')
    print('/__/\\___/|_|_|_| \\___|  \\__||_||_||_||_||_| \\__, |   \\_/\\_/ \\___||_||_|  \\__|   \\_/\\_/ |_|  \\___/|_||_| \\__, |  ')
    print('                                            |___/                                                       |___/   ')
    print('')

    match errorType:
        case 'does_not_exist':
            print('"' + param + '" does not exist yet. Please try again later.')
        case _:
            print('"' + param + '" is not a valid input. Please try again.')
    print('')
    input('~~> ')

    print('\033c', end='') # clear terminal

def name_web(selectedNumber, last=False):
    """creates name web"""
    global chosenName

    for i in range(len(names)):
        if i % 3 == 0: 
            start = random.randint(1, 5)
            print('~' * start, end='')

        nLength = len(names[i])
        if i == selectedNumber:
            print(names[i][:20].upper(), end='')
            if last:
                chosenName = names[i]
        else:
            print(names[i][:20].lower(), end='')

        print('~' * (20 - nLength), end='')
        
        if i % 3 == 2: 
            print('~' * (5 - start))
    print('')

#* program *#
while True:
    print('')
    print('|| made by sbird ||')
    print('')
                                                                                                                                                                                                                                                                                         
    # choose subject to study
    print('What would you like to do?')
    print('')
    print('~ run')
    print('~ quit')
    print('')
    userAction = input('~~> ').lower() # sets answer as lowercase to avoid miscasing
    
    match userAction:
        case 'run':
            delay = 0

            for i in range(10):
                # random number
                index = random.randint(0, len(names))
                
                name_web(index)

                # delay
                time.sleep(delay)
                delay = delay + 0.1

                print('\033c', end='') # clear terminal
            
            # random number
            index = random.randint(0, 8)            
            name_web(index, True)

            time.sleep(0.8)

            print('\033c', end='') # clear terminal

            print('|~' + ('~' * len(chosenName)) + '~|')
            print('| ' + chosenName + ' |')
            print('|~' + ('~' * len(chosenName)) + '~|')
            print('')
            input('~~> ')

            print('\033c', end='') # clear terminal
        case 'quit' | 'q':
            sys.exit(0)
        case _:
            call_error(userAction)
