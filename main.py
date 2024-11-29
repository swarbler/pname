import random, time, math, sys
from colorama import Fore, Back, Style

#* declaring variables *#
with open('list.txt', 'r') as l:
    names = l.read().split('\n')

chosenName = ""
spacingMax = 5
nLengthMax = 20


#* declaring functions *#

def call_error(param, errorType='none', minR=0, maxR=0):
    """error message"""

    print('\033c', end='') # clear terminal

    # something went wrong (Fire Font-k)
    print(Fore.RED, end='')
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
        # checks whether it is at the beginning of the line
        if i % 3 == 0: 
            start = random.randint(1, spacingMax)
            print(Fore.YELLOW + '~' * start, end='')

        nLength = len(names[i])

        # UPPER CASE if selected, lower case if not
        if i == selectedNumber:
            print(Fore.RED + names[i][:nLengthMax].upper() + Fore.YELLOW, end='')

            if last:
                chosenName = names[i] # sets chosen name to selected name
        else:
            print(names[i][:nLengthMax].lower(), end='')

        # buffer text
        print('~' * (nLengthMax - nLength), end='')
        print('~' * 5, end='')
        
        # checks whether it is at the end of the line
        if i % 3 == 2: 
            print('~' * (spacingMax - start))

#* program *#
while True:
    # PNAME Stick Letters
    print(Fore.BLUE, end='')
    print(' __                  ___ ')
    print('|__) |\\ |  /\\  |\\/| |__  ')
    print('|    | \\| /~~\\ |  | |___ ')             
    print(Fore.GREEN)
    print('|| made by sbird ||')

    print(Fore.YELLOW)
    print('What would you like to do?')
    print('')
    print('~ run')
    print('~ quit')
    print('')
    userAction = input('~~> ').lower() # sets answer as lowercase to avoid miscasing
    
    match userAction:
        case 'run':
            delay = 0
            random.shuffle(names)

            for i in range(10):
                # random number
                r = random.randint(0, len(names))
                
                name_web(r)

                # delay
                time.sleep(delay)
                delay = delay + 0.1

                print('\033c', end='') # clear terminal
            
            # random number
            r = random.randint(0, len(names))            
            name_web(r, True)

            time.sleep(0.8)

            print('\033c', end='') # clear terminal

            print(Fore.YELLOW, end='')
            print('|~' + ('~' * len(chosenName)) + '~|')
            print('| ' + Fore.RED + chosenName + Fore.YELLOW + ' |')
            print('|~' + ('~' * len(chosenName)) + '~|')
            print('')
            input('~~> ')

            print('\033c', end='') # clear terminal
        case 'quit' | 'q':
            sys.exit(0)
        case _:
            call_error(userAction)
