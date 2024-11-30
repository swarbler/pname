import random, time, math, sys
from colorama import Fore, Back, Style

#* declaring variables *#
with open('list.txt', 'r') as l:
    names = l.read().split('\n')

chosenName = ''
spacingMax = 5
nLengthMax = 20
trickleTime = 10


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

    for i in range(len(names) - 1):
        # checks whether it is at the beginning of the line
        if i % 3 == 0: 
            start = random.randint(1, spacingMax)
            print(Fore.BLUE + '~' * start, end='')

        nLength = len(names[i])

        # UPPER CASE if selected, lower case if not
        if i == selectedNumber:
            if last:
                print(Fore.GREEN + names[i][:nLengthMax].upper() + Fore.BLUE, end='')

                chosenName = names[i] # sets chosen name to selected name
            else:
                print(Fore.RED + names[i][:nLengthMax].upper() + Fore.BLUE, end='')
        else:
            print(names[i][:nLengthMax].lower(), end='')

        # buffer text
        print('~' * (nLengthMax - nLength), end='')
        print('~' * 5, end='')
        
        # checks whether it is at the end of the line
        if i % 3 == 2: 
            print('~' * (spacingMax - start))

def name_spiderman(r1, last=False):
    """creates spiderman"""
    global chosenName

    r2, r3, r4, r5 = random.randint(0, len(names) - 1), random.randint(0, len(names) - 1), random.randint(0, len(names) - 1), random.randint(0, len(names)- 1)

    print(Fore.RED, end='')
    print('  _                                                                        ')
    print(' _\\`.                                                                      ')
    print(' \\_)-`""---""""--.                                                         ')
    print('/.--     _        `._                                                      ')
    print('`_.-\'.-. \\"-.   ,--. \\                                                     ')
    if last:
        print('`---"   `.;  `.\' -. `."-.               ' + Fore.MAGENTA + names[r1][:30] + Fore.RED)
    else:
        print('`---"   `.;  `.\' -. `."-.               ' + Fore.CYAN + names[r1][:30] + Fore.RED)
    print('               `---\\  `. "-.  ____                                         ')
    print('\\                   \\   "-._`"    `.                                       ')
    print('``.-,                `.     `._     \\                      _.-.            ')
    print('   "-:                 "-.    \\`.    "-._               .-"    `.          ')
    print('     :\\ '  + Fore.CYAN + names[r2][:16] + ' ' * (16 - len(names[r2][:16])) + Fore.RED + ' +  +   "-.__\\ \\   ;   "-.          .\'     _   \\         ')
    print('      \\;                    j. :`-:_.\'      \'.---..--\'.   .-";`.  \\_ /; _  ')
    print('       :)                  :  `;  :        .\'     \\    ` ; .\'`-.;  \\7 L\'/  ')
    print('       ;                   ;   ;  ; `-.__,/ :\\     ;    /-"     `.   \'-+__ ')
    print('      /;                   ;   :  ;      : /  ;    ; _.\'         : :------\'')
    print('   _.\'"                    ;    \\:       ; \\  ; .-/-"             `.\\      ')
    print('  (/              __       :     :. : /  ;  "" (.\'                  "      ')
    print('  :)   _;      .-\'  \\       \\    ;  _\\\\o_\'    .:                           ')
    print('   \\  :/      :    `."-.     ;   ; /,\' :-\'\'=-\'/                            ')
    print('    `-\'       ;      ;  "-._ ;_ :   :_.\') .\'+-"    '  + Fore.CYAN + names[r3][:24] + ' ' * (24 - len(names[r3][:24])) + Fore.RED)
    print('              :      :      `; "\'      \'/ /"""--.._                        ')
    print('               \\      `+.     `,       :.\'         "-.                     ')
    print('                ;      : \\      \\_..--""              "-.                  ')
    print('                :`-..-"   \\   '  + Fore.CYAN + names[r4][:16] + ' ' * (16 - len(names[r4][:16])) + Fore.RED + '         ""-._               ')
    print('                 \\         ;     .----._                  ,\'l              ')
    print('                  `.       : _.-"       ""--..____..__    ; :              ')
    print('                    "-.     `._    bug                )     ;              ')
    print('                       "-.     ""--.._               :`.___.:              ')
    print('                          "-.-\'       `.             ;      :              ')
    print('                             "-._   .\'  )            :      ;              ')
    print('                                 "-._.-"              \\    :               ')
    print('                                                       ;   ;               ')
    print('  '  + Fore.CYAN + names[r5][:24] + ' ' * (24 - len(names[r5][:24])) + Fore.RED + '                             |  :                ')
    print('                                                      _:  :                ')
    print('                                                     l     `.              ')
    print('                                                     \'-._    `.            ')
    print('                                                         `.    \\           ')
    print('                                                           \\    ;          ')
    print('                                                            "-._:')

    if last:
        chosenName = names[r1]

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
    print('~ web')
    print('~ spiderman')
    print('~ quit')
    print('')
    userAction = input('~~> ').lower() # sets answer as lowercase to avoid miscasing
    
    match userAction:
        case 'web' | 'spiderman':
            delay = 0
            random.shuffle(names)

            for i in range(trickleTime):
                r = random.randint(0, len(names) - 1)
                
                match userAction:
                    case 'web':
                        name_web(r)
                    case 'spiderman':
                        name_spiderman(r)

                time.sleep(delay)
                delay = delay + 0.1 # delay increases every time

                print('\033c', end='') # clear terminal
            
            r = random.randint(0, len(names) - 1)    

            match userAction:
                case 'web':
                    name_web(r, True)
                case 'spiderman':
                    name_spiderman(r, True)

            time.sleep(0.8)

            print('\033c', end='') # clear terminal

            print(Fore.YELLOW, end='')
            print('|~' + ('~' * len(chosenName)) + '~|')
            match userAction:
                case 'web':
                    print('| ' + Fore.GREEN + chosenName + Fore.YELLOW + ' |')
                case 'spiderman':
                    print('| ' + Fore.MAGENTA + chosenName + Fore.YELLOW + ' |')
            print('|~' + ('~' * len(chosenName)) + '~|')
            print('')
            input('~~> ')

            print('\033c', end='') # clear terminal
        case 'quit' | 'q':
            sys.exit(0)
        case _:
            call_error(userAction)
