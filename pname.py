import random, time, math, sys, glob
from colorama import Fore, Back, Style
from art import *
from pathlib import Path


#* declaring variables *#
chosenListFile = 'list'
chosenName = ''

TRICKLE_TIME = 10
MINIMUM_PAIR_TIME = 0.2

OPTIONS = ['web', 'spiderman', 'birds', 'bird', 'tv', 'television', 'calc', 'calculator', 'golf', 'reaper', 'death', 'flowers', 'flower']
PAIR_OPTIONS = ['branches', 'branch', 'waterfall', 'caves', 'cave']
FOUR_OPTIONS = ['blocks', 'block']
SET_OPTIONS = ['set list file', 'set list', 'set file', 'list file', 'list', 'file']
RANDOM_SET_OPTIONS = ['random list file', 'random list', 'random file', 'random']

def setList():
    with open(chosenListFile + '.txt', 'r') as l:
        return l.read().split()

names = setList()


#* declaring functions *#

def call_error(param, errorType='none', minR=0, maxR=0):
    """error message"""

    print('\033c', end='') # clear terminal

    print(Fore.RED, end='')
    tprint('something went wrong', 'fire-font-s')
    # print('                           )    )                                           )                                   ')
    # print('             )      (   ( /( ( /( (          (  (    (  (      (         ( /(   (  (    (                (  (   ')
    # print(' (    (     (      ))\\  )\\()))\\()))\\   (     )\\))(   )\\))(    ))\\  (     )\\())  )\\))(   )(    (    (     )\\))(  ')
    # print(' )\\   )\\    )\\  \' /((_)(_))/((_)\\((_)  )\\ ) ((_))\\  ((_)()\\  /((_) )\\ ) (_))/  ((_)()\\ (()\\   )\\   )\\ ) ((_))\\  ')
    # print('((_) ((_) _((_)) (_))  | |_ | |(_)(_) _(_/(  (()(_) _(()((_)(_))  _(_/( | |_   _(()((_) ((_) ((_) _(_/(  (()(_) ')
    # print('(_-</ _ \\| \'  \\()/ -_) |  _|| \' \\ | || \' \\))/ _` |  \\ V  V // -_)| \' \\))|  _|  \\ V  V /| \'_|/ _ \\| \' \\))/ _` |  ')
    # print('/__/\\___/|_|_|_| \\___|  \\__||_||_||_||_||_| \\__, |   \\_/\\_/ \\___||_||_|  \\__|   \\_/\\_/ |_|  \\___/|_||_| \\__, |  ')
    # print('                                            |___/                                                       |___/   ')
    # print('')

    match errorType:
        case 'does_not_exist':
            print('"' + param + '" does not exist yet. Please try again later.')
        case 'invalid_file':
            print('"' + param + '.txt" is not a valid file. Please try again.')
        case _:
            print('"' + param + '" is not a valid input. Please try again.')
    input('~>')

    print('\033c', end='') # clear terminal

# selecting a single person
def name_web(selectedNumber, last=False):
    """creates name web"""
    global chosenName

    for i in range(len(names) - 1):
        # checks whether it is at the beginning of the line
        if i % 3 == 0: 
            start = random.randrange(5) + 1
            print(Fore.BLUE + '~' * start, end='')

        nLength = len(names[i])

        # UPPER CASE if selected, lower case if not
        if i == selectedNumber:
            if last:
                print(Fore.MAGENTA + names[i][:20].upper() + Fore.BLUE, end='')

                chosenName = names[i] # sets chosen name to selected name
            else:
                print(Fore.GREEN + names[i][:20].upper() + Fore.BLUE, end='')
        else:
            print(names[i][:20].lower(), end='')

        # buffer text
        print('~' * (20 - nLength), end='')
        print('~' * 5, end='')
        
        # checks whether it is at the end of the line
        if i % 3 == 2: 
            print('~' * (5 - start))

def name_spiderman(r1, last=False):
    """creates spiderman"""
    global chosenName

    r2, r3, r4, r5 = random.randrange(len(names)), random.randrange(len(names)), random.randrange(len(names)), random.randrange(len(names))

    # sets spacing
    s2 = 16 - len(names[r2][:16])
    s4 = 16 - len(names[r4][:16])
    s5 = 24 - len(names[r5][:24])

    print(Fore.RED, end='')
    print('  _                                                                        ')
    print(' _\\`.                                                                      ')
    print(' \\_)-`""---""""--.                                                         ')
    print('/.--     _        `._                                                      ')
    print('`_.-\'.-. \\"-.   ,--. \\                                                     ')
    if last:
        print(f'`---"   `.;  `.\' -. `."-.               {Fore.MAGENTA}{names[r1][:30]}{Fore.RED}')
    else:
        print(f'`---"   `.;  `.\' -. `."-.               {Fore.GREEN}{names[r1][:30]}{Fore.RED}')
    print('               `---\\  `. "-.  ____                                         ')
    print('\\                   \\   "-._`"    `.                                       ')
    print('``.-,                `.     `._     \\                      _.-.            ')
    print('   "-:                 "-.    \\`.    "-._               .-"    `.          ')
    print(f'     :\\ {Fore.CYAN}{names[r2][:16]}{' ' * s2}{Fore.RED} +  +   "-.__\\ \\   ;   "-.          .\'     _   \\         ')
    print('      \\;                    j. :`-:_.\'      \'.---..--\'.   .-";`.  \\_ /; _  ')
    print('       :)                  :  `;  :        .\'     \\    ` ; .\'`-.;  \\7 L\'/  ')
    print('       ;                   ;   ;  ; `-.__,/ :\\     ;    /-"     `.   \'-+__ ')
    print('      /;                   ;   :  ;      : /  ;    ; _.\'         : :------\'')
    print('   _.\'"                    ;    \\:       ; \\  ; .-/-"             `.\\      ')
    print('  (/              __       :     :. : /  ;  "" (.\'                  "      ')
    print('  :)   _;      .-\'  \\       \\    ;  _\\\\o_\'    .:                           ')
    print('   \\  :/      :    `."-.     ;   ; /,\' :-\'\'=-\'/                            ')
    print(f'    `-\'       ;      ;  "-._ ;_ :   :_.\') .\'+-"    {Fore.CYAN}{names[r3][:30]}{Fore.RED}')
    print('              :      :      `; "\'      \'/ /"""--.._                        ')
    print('               \\      `+.     `,       :.\'         "-.                     ')
    print('                ;      : \\      \\_..--""              "-.                  ')
    print(f'                :`-..-"   \\   {Fore.CYAN}{names[r4][:16]}{' ' * s4}{Fore.RED}         ""-._               ')
    print('                 \\         ;     .----._                  ,\'l              ')
    print('                  `.       : _.-"       ""--..____..__    ; :              ')
    print('                    "-.     `._    bug                )     ;              ')
    print('                       "-.     ""--.._               :`.___.:              ')
    print('                          "-.-\'       `.             ;      :              ')
    print('                             "-._   .\'  )            :      ;              ')
    print('                                 "-._.-"              \\    :               ')
    print('                                                       ;   ;               ')
    print(f'  {Fore.CYAN}{names[r5][:24]}{' ' * s5}{Fore.RED}                             |  :                ')
    print('                                                      _:  :                ')
    print('                                                     l     `.              ')
    print('                                                     \'-._    `.            ')
    print('                                                         `.    \\           ')
    print('                                                           \\    ;          ')
    print('                                                            "-._:')

    if last:
        chosenName = names[r1]

def name_birds(selectedNumber, last=False):
    """creates birds"""
    global chosenName

    print(Fore.CYAN, end='')

    # bird heads
    print('   (                          \\\\')
    if last:
        print('  `-`-.               \\\\      (->')
        print(f'  \'( - >              (->     //\\      {Fore.MAGENTA}{names[selectedNumber][:20]}{Fore.CYAN}')
    else:
        print('  `-`-.               \\\\      (o>')
        print(f'  \'( O >              (o>     //\\      {Fore.GREEN}{names[selectedNumber][:20]}{Fore.CYAN}')
    
    # bird feet
    print('   _) (           ____(()_____V_/_____')
    print('  /    )              ||      ||               ,_,')
    
    # owl head
    if last:
        print(' /_,\'  /                     ||               (.,.)')
    else:
        print(' /_,\'  /                     ||               (O,O)')
    print('   \\  /                                       (   )')
    
    # bird and owl feet
    print('===m""m=========================         ------"-"-------')

    if last:
        chosenName = names[selectedNumber]

def name_tv(selectedNumber, last=False):
    """creates tv"""
    global chosenName

    # sets spacing
    s = 14 - len(names[selectedNumber][:14])

    print(Fore.GREEN, end='')
    print(' _____________________     ')
    print('|,----------------.  |\\    ')
    print('||                 |=| |   ')
    if last:
        print(f'||{Fore.MAGENTA}{names[selectedNumber][:14]}{' ' * s}{Fore.GREEN}|| | |   ')
    else:
        print(f'||{Fore.BLUE}{names[selectedNumber][:14]}{' ' * s}{Fore.GREEN}|| | |   ')
    print('||             . _o| | | __')
    print('|`-----------------\' |/ /~/')
    print(' ~~~~~~~~~~~~~~~~~~~~~ / / ')
    print('                       ~~  ')

    if last:
        chosenName = names[selectedNumber]

def name_calc(selectedNumber, last=False):
    """creates calculator"""
    global chosenName

    # sets spacing
    s = 8 - len(names[selectedNumber][:8])

    print(Fore.GREEN, end='')
    print(' __________ ')
    print('| ________ |')
    if last:
        print(f'||{Fore.MAGENTA}{names[selectedNumber][:8]}{' ' * s}{Fore.GREEN}||')
    else:
        print(f'||{Fore.BLUE}{names[selectedNumber][:8]}{' ' * s}{Fore.GREEN}||')
    print('|""""""""""|')
    print('|[M|#|C][-]|')
    print('|[7|8|9][+]|')
    print('|[4|5|6][x]|')
    print('|[1|2|3][%]|')
    print('|[.|O|:][=]|')
    print('"----------"  hjw')

    if last:
        chosenName = names[selectedNumber]

def name_golf(r1, stage=0, last=False):
    """golf animation"""
    global chosenName

    r2, r3, r4 = random.randrange(len(names)), random.randrange(len(names)), random.randrange(len(names))

    rselect = random.randrange(4)

    print(Fore.GREEN, end='')
    
    # first name
    if stage == 5 or stage == 6:
        # golf ball on sixth and seventh turn
        print('     \'\\                   o  .     ' + Fore.BLUE + names[r1][:16] + ' ' * (16 - len(names[r1][:16])) + Fore.GREEN + '   |>18>>  ')
    elif stage == 7:
        # golf ball on eight turn
        print('     \'\\                   .  o     ' + Fore.BLUE + names[r1][:16] + ' ' * (16 - len(names[r1][:16])) + Fore.GREEN + '   |>18>>  ')
    elif last: # last turn
        if rselect == 0: # if first name is selected
            print('     \'\\                   .  .     ' + Fore.MAGENTA + names[r1][:16] + ' ' * (16 - len(names[r1][:16])) + Fore.GREEN + '   |>18>>  ')
        else:
            # do not display selected name if rselect is not 0
            match rselect:
                case 1: print('     \'\\                   .  .     ' + Fore.BLUE + names[r2][:16] + ' ' * (16 - len(names[r2][:16])) + Fore.GREEN + '   |>18>>  ')
                case 2: print('     \'\\                   .  .     ' + Fore.BLUE + names[r3][:16] + ' ' * (16 - len(names[r3][:16])) + Fore.GREEN + '   |>18>>  ')
                case 3: print('     \'\\                   .  .     ' + Fore.BLUE + names[r4][:16] + ' ' * (16 - len(names[r4][:16])) + Fore.GREEN + '   |>18>>  ')
    else:
        print('     \'\\                   .  .     ' + Fore.BLUE + names[r1][:16] + ' ' * (16 - len(names[r1][:16])) + Fore.GREEN + '   |>18>>  ')
    
    # second name
    if stage == 3 or stage == 4:
        # golf ball on fourth and fifth turn
        print('       \\              o         \' .   ' + Fore.BLUE + ' ' * (12 - len(names[r2][:12])) + names[r2][:12] + Fore.GREEN + '    |       ')
    elif stage == 8:
        # golf ball on third last turn
        print('       \\              .         \' o   ' + Fore.BLUE + ' ' * (12 - len(names[r2][:12])) + names[r2][:12] + Fore.GREEN + '    |       ')
    else:
        if last and rselect == 1: # if second name is selected on last turn
            # displays selected name if rselect is 1
            print('       \\              .         \' .   ' + Fore.MAGENTA + ' ' * (12 - len(names[r1][:12])) + names[r1][:12] + Fore.GREEN + '    |       ')
        else:
            # displays non-selected name if rselect is not 1
            print('       \\              .         \' .   ' + Fore.BLUE + ' ' * (12 - len(names[r2][:12])) + names[r2][:12] + Fore.GREEN + '    |       ')
    
    if stage == -1:
        # golfball becomes magenta on last turn
        print('      O>>         .                 \'' + Fore.MAGENTA + 'o' + Fore.GREEN + '                |       ')
    elif stage == 9:
        # golfball on second last turn
        print('      O>>         .                 \'o                |       ')
    elif stage == 2:
        # golfball on third turn
        print('      O>>         o                 \'.                |       ')
    else:
        print('      O>>         .                 \'.                |       ')
    
    # third name
    if stage == 1:
        # golfball on the second turn
        print('       \\       o     ' + Fore.BLUE + names[r3][:30] + ' ' * (30 - len(names[r3][:30])) + Fore.GREEN + '   |       ')
    else:
        if last and rselect == 2: # if third name is selected on last turn
            # displays selected name if rselect is 2
            print('       \\       .     ' + Fore.MAGENTA + names[r1][:30] + ' ' * (30 - len(names[r1][:30])) + Fore.GREEN + '   |       ')
        else:
            # displays non-selected name if rselect is not 2
            print('       \\       .     ' + Fore.BLUE + names[r3][:30] + ' ' * (30 - len(names[r3][:30])) + Fore.GREEN + '   |       ')
    
    if stage == 0:
        # on the first turn, golfball is at the lowest point
        print('       /\\    o                                        |       ')
    else:
        print('       /\\    .                                        |       ')
    
    # fourth name name
    if last and rselect == 3: # if fourth name is selected on last turn
        # displays selected name if rselect is 3
        print('      / /  .\'               ' + Fore.MAGENTA + names[r1][:24] + ' ' * (24 - len(names[r1][:24])) + Fore.GREEN + '  |       ')
    else:
        # displays non-selected name if rselect not is 3
        print('      / /  .\'               ' + Fore.BLUE + names[r4][:24] + ' ' * (24 - len(names[r4][:24])) + Fore.GREEN + '  |       ')
    
    print('jgs^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

    if last:
        chosenName = names[r1]

def name_reaper(r1, last=False):
    """creates reaper"""
    global chosenName

    r2, r3, r4, r5, r6, r7, r8 = random.randrange(len(names)), random.randrange(len(names)), random.randrange(len(names)), random.randrange(len(names)), random.randrange(len(names)), random.randrange(len(names)), random.randrange(len(names))

    rselect = random.randrange(8)

    print(Fore.RED, end='')

    print('                       ,____')
    print('                   |---.\\   ')
    print('           ___     |    `   ')
    print('          / .-\\  ./=)       ')
    if last:
        if rselect == 0:
            print(f'         |  |*|_/\\/|        {Fore.MAGENTA}{names[r1][:30]}{Fore.RED}')
        else:
            match rselect:
                case 1: print(f'         |  |*|_/\\/|        {Fore.BLUE}{names[r2][:30]}{Fore.RED}')
                case 2: print(f'         |  |*|_/\\/|        {Fore.BLUE}{names[r3][:30]}{Fore.RED}')
                case 3: print(f'         |  |*|_/\\/|        {Fore.BLUE}{names[r4][:30]}{Fore.RED}')
                case 4: print(f'         |  |*|_/\\/|        {Fore.BLUE}{names[r5][:30]}{Fore.RED}')
                case 5: print(f'         |  |*|_/\\/|        {Fore.BLUE}{names[r6][:30]}{Fore.RED}')
                case 6: print(f'         |  |*|_/\\/|        {Fore.BLUE}{names[r7][:30]}{Fore.RED}')
                case 7: print(f'         |  |*|_/\\/|        {Fore.BLUE}{names[r8][:30]}{Fore.RED}')
    else:
        print(f'         |  |"|_/\\/|        {Fore.BLUE}{names[r1][:30]}{Fore.RED}')
    if last and rselect == 1:
        print(f'         ;  |-;| /_|        {Fore.MAGENTA}{names[r1][:30]}{Fore.RED}')
    else:
        print(f'         ;  |-;| /_|        {Fore.BLUE}{names[r2][:30]}{Fore.RED}')
    if last and rselect == 2:
        print(f'        / \\_| |/ \\ |        {Fore.MAGENTA}{names[r1][:30]}{Fore.RED}')
    else:
        print(f'        / \\_| |/ \\ |        {Fore.BLUE}{names[r3][:30]}{Fore.RED}')
    if last and rselect == 3:
        print(f'       /      \\/\\( |        {Fore.MAGENTA}{names[r1][:30]}{Fore.RED}')
    else:
        print(f'       /      \\/\\( |        {Fore.BLUE}{names[r4][:30]}{Fore.RED}')
    if last and rselect == 4:
        print(f'       |   /  |` ) |        {Fore.MAGENTA}{names[r1][:30]}{Fore.RED}')
    else:
        print(f'       |   /  |` ) |        {Fore.BLUE}{names[r5][:30]}{Fore.RED}')
    if last and rselect == 5:
        print(f'       /   \\ _/    |        {Fore.MAGENTA}{names[r1][:30]}{Fore.RED}')
    else:
        print(f'       /   \\ _/    |        {Fore.BLUE}{names[r6][:30]}{Fore.RED}')
    if last and rselect == 6:
        print(f'      /--._/  \\    |        {Fore.MAGENTA}{names[r1][:30]}{Fore.RED}')
    else:
        print(f'      /--._/  \\    |        {Fore.BLUE}{names[r7][:30]}{Fore.RED}')
    if last and rselect == 7:
        print(f'      `/|)    |    /        {Fore.MAGENTA}{names[r1][:30]}{Fore.RED}')
    else:
        print(f'      `/|)    |    /        {Fore.BLUE}{names[r8][:30]}{Fore.RED}')
    print('        /     |   |         ')
    print('      .\'      |   |         ')
    print('jgs  /         \\  |         ')
    print('    (_.-.__.__./  /         ')

    if last:
        chosenName = names[r1]

def name_flowers(r1, last=False):
    """creates flowers"""
    global chosenName

    r2, r3, r4, r5 = random.randrange(len(names)), random.randrange(len(names)), random.randrange(len(names)), random.randrange(len(names))

    rselect = random.randrange(5)

    s1, s2, s3 = random.randrange(5, 10), random.randrange(5, 10), random.randrange(5, 10)

    print(Fore.CYAN)
    # line 1
    if rselect == 0: # if first name is selected
        if last:
            print((s1 * ' ') + Fore.MAGENTA + names[r1] + Fore.CYAN + ((s1 * 2) * ' ') + names[r2])
        else:
            print((s1 * ' ') + Fore.GREEN + names[r1] + Fore.CYAN + ((s1 * 2) * ' ') + names[r2])
    elif rselect == 1: # if second name is selected
        if last:
            print((s1 * ' ') + names[r2] + ((s1 * 2) * ' ') + Fore.MAGENTA + names[r1] + Fore.CYAN)
        else:
            print((s1 * ' ') + names[r2] + ((s1 * 2) * ' ') + Fore.GREEN + names[r1] + Fore.CYAN)
    else:
        if last:
            match rselect: # don't show selected number if first name is not selected
                case 2: print((s1 * ' ') + names[r3] + ((s1 * 2) * ' ') + names[r2])
                case 3: print((s1 * ' ') + names[r4] + ((s1 * 2) * ' ') + names[r2])
                case 4: print((s1 * ' ') + names[r5] + ((s1 * 2) * ' ') + names[r2])
        else:
            print((s1 * ' ') + names[r1] + ((s1 * 2) * ' ') + names[r2])
    
    # line 2
    if rselect == 2: # if third name is selected
        if last:
            print((s2 * ' ') + Fore.MAGENTA + names[r1] + Fore.CYAN + ((s1 * 2) * ' ') + names[r4])    
        else:
            print((s2 * ' ') + Fore.GREEN + names[r3] + Fore.CYAN + ((s1 * 2) * ' ') + names[r4])
    elif rselect == 3: # if fourth name is selected
        if last:
            print((s2 * ' ') + names[r1] + ((s2 * 2) * ' ') + Fore.MAGENTA + names[r4] + Fore.CYAN)
        else:
            print((s2 * ' ') + names[r3] + ((s2 * 2) * ' ') + Fore.GREEN + names[r4] + Fore.CYAN)
    else:
        print((s2 * ' ') + names[r3] + ((s2 * 2) * ' ') + names[r4])
    
    # line 3
    if rselect == 4: # if last name is selected
        if last:
            print(((s3 * 3) * ' ') + Fore.MAGENTA + names[r1] + Fore.CYAN)
        else:
            print(((s3 * 3) * ' ') + Fore.GREEN + names[r5] + Fore.CYAN)
    else:
        print(((s3 * 3) * ' ') + names[r5])
    
    print('')
    print(f'            {Fore.YELLOW}wWWWw{Fore.GREEN}               {Fore.CYAN}wWWWw{Fore.GREEN}            ')
    print(f'      {Fore.RED}vVVVv{Fore.GREEN} (___) {Fore.BLUE}wWWWw{Fore.GREEN}         (___)  {Fore.BLUE}vVVVv{Fore.GREEN}     ')
    print(f'      (___)  ~Y~  (___)  {Fore.MAGENTA}vVVVv{Fore.GREEN}   ~Y~   (___)     ')
    print('       ~Y~   \\|    ~Y~   (___)    |/    ~Y~      ')
    print('       \\|   \\ |/   \\| /  \\~Y~/   \\|    \\ |/      ')
    print('      \\\\|// \\\\|// \\\\|/// \\\\|//  \\\\|// \\\\\\|///    ')
    print('jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    
    if last:
        chosenName = names[r1]

# selecting pairs
def pair_branch():
    """creates tree branch"""
    print(Fore.GREEN, end='')

    for i in range(1, len(names), 2): # iterates over names, stepping by 2
        # prints names beside branch
        print(f'      %@@@@%::;           ;@%%%%%%;\'   {names[i - 1][:50]}') 
        print(f'      %@@@@%::;%@@@o%::%@@%;   and {names[i][:50]}')

        # continues trunk
        print('  `.. %@@@o%::;         ')
        print('     `)@@@o%::;         ')
        for i in range(random.randrange(1, 4)): # random amount of trunk spacing
            print('      ;@@@o%::;         ')

        time.sleep(random.random() + MINIMUM_PAIR_TIME) # random amount of delay
    
    # base of tree
    print('      %@@%%%::;')
    if len(names) % 2 == 1: # if amount of names is an odd number, print odd one out
        print(f'      %@@@%(o);  . \'   {names[-1][:50]}')
    else:
        print('      %@@@%(o);  . \'        ') 
    
    # print the rest of the tree
    print('      %@@@o%;:(.,\'        ') 
    print('  `.. %@@@o%::;         ')
    print('     `)@@@o%::;         ')
    print('     .%@@@@%::;          ')
    print('     ;%@@@@%::;.              ')
    print('    ;%@@@@%%:;;;.             ')
    print('...;%@@@@@%%:;;;;,..    Gilo97')

def pair_waterfall():
    """creates waterfall"""
    print(Fore.BLUE, end='')

    # top of waterfall
    print('                  _.._                                             ')
    print('   _________....-~    ~-.______                                    ')
    print('~~~                            ~~~~-----...___________..--------   ')
    
    for i in range(1, len(names), 2): # iterates over names, stepping by 2
        # sets spacing
        spacing1 = 36 - len(names[i-1][:36])
        spacing2 = 40 - len(names[i][:40])
        
        # prints names beside waterfall
        print(f' {' ' * spacing1}{names[i - 1][:36]} and  |   |     |             ')
        print(f' {' ' * spacing2}{names[i][:40]}  | |   |  ||             ')
        
        # continues waterfall
        print('                                           |  |  |   |             ')

        time.sleep(random.random() + MINIMUM_PAIR_TIME) # random amount of delay
    
    # base of waterfall
    print('                                           |\'. .\' .`.|             ')
    print('___________________________________________|0oOO0oO0o|____________ ')
    print(' -          -         -       -      -    / \'  \'. ` ` \\    -    -  ')
    if len(names) % 2 == 1: # if amount of names is an odd number, print odd one out
        # sets spacing
        lastSpacing = 25 - len(names[-1][:25])
        
        print(f'{' ' * lastSpacing}{names[-1][:25]} --   /    \'  . `   ` \\    --    ')
    else:
        print('      --                  --       --   /    \'  . `   ` \\    --    ')
    print('---     AMC    ---          ---       /  \'                \\ ---    ')

def pair_caves():
    """creates caves"""
    print(Fore.MAGENTA, end='')

    # cave top
    for i in range(random.randrange(1, 4)): # random amount of cave spacing
        cLeft = random.randrange(1, 80) # random amount of cave walls
        cRight = 80 - cLeft # amount depends on rLeft

        print(cLeft * '%' + cRight * 'X')

    for i in range(1, len(names), 2): # iterates over names, stepping by 2
        rLeft = random.randrange(1, 40) # random amount of cave walls
        rRight = 40 - rLeft # amount depends on rLeft

        textLength = len((names[i - 1] + ' and ' + names[i])[:40]) # find length of both names combined

        # makes sure width of cave is 40
        # splits spacing equally between left and right
        spacingLeft = math.floor((40 - textLength) / 2)
        spacingRight = math.ceil((40 - textLength) / 2)

        # prints line with cave walls, spacing, and names
        print(f'{rLeft * '%'}{spacingLeft * ' '}{names[i - 1]} and {names[i][:40]}{spacingRight * ' '}{rRight * 'X'}')

        # continues cave
        for i in range(random.randrange(1, 4)): # random amount of cave spacing
            cLeft = random.randrange(1, 80) # random amount of cave walls
            cRight = 80 - cLeft # amount depends on rLeft

            print(cLeft * '%' + cRight * 'X')

        time.sleep(random.random() + MINIMUM_PAIR_TIME) # random amount of delay

    if len(names) % 2 == 1: # if amount of names is an odd number, print odd one out
        rLeft = random.randrange(1, 40) # random amount of cave walls
        rRight = 40 - rLeft # amount depends on rLeft

        textLength = len(names[-1][:40])

        # makes sure width of cave is 40
        # splits spacing equally between left and right
        spacingLeft = math.floor((40 - textLength) / 2)
        spacingRight = math.ceil((40 - textLength) / 2)

        # prints line with cave walls, spacing, and names
        print(f'{rLeft * '%'}{spacingLeft * ' '}{names[-1][:40]}{spacingRight * ' '}{rRight * 'X'}')

        # continues cave
        for i in range(random.randrange(1, 4)): # random amount of cave spacing
            cLeft = random.randrange(1, 80) # random amount of cave walls
            cRight = 80 - cLeft # amount depends on rLeft

            print(cLeft * '%' + cRight * 'X')
    
    # cave base
    for i in range(random.randrange(1, 4)): # random amount of cave spacing
        cLeft = random.randrange(1, 80) # random amount of cave walls
        cRight = 80 - cLeft # amount depends on rLeft

        print(cLeft * '%' + cRight * 'X')

# selecting groups of 4
def four_blocks():
    """creates blocks"""
    counter = 0

    B_COLOURS = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.CYAN]

    for i in range(3, len(names), 4): # iterates over names, stepping by 4
        # colours iterate through B_COLOURS
        # e.g. first is red, second is green, third is blue...
        print(B_COLOURS[counter])
        
        # sets spacing for each name
        spacing1 = 25 - len(names[i-3][:25])
        spacing2 = 25 - len(names[i-2][:25])
        spacing3 = 25 - len(names[i-1][:25])
        spacing4 = 25 - len(names[i][:25])
        
        # creates block
        print(f'|{'~' * 55}|')
        print(f'| {' ' * spacing1}{names[i-3][:25]} | {names[i-2][:25]}{' ' * spacing2} |')
        print(f'|{'~' * 55}|')
        print(f'| {' ' * spacing3}{names[i-1][:25]} | {names[i][:25]}{' ' * spacing4} |')
        print(f'|{'~' * 55}|')
        
        # counter goes from 0 to 4
        if counter == 4:
            counter = 0
        else:
            counter += 1
        
        time.sleep(random.random() + MINIMUM_PAIR_TIME) # random amount of delay


    # display remainder names
    match len(names) % 4:
        case 3:
            print(Fore.MAGENTA)
            print(f'remainder: {names[-3]}, {names[-2]}, and {names[-1]}')
        case 2:
            print(Fore.MAGENTA)
            print(f'remainder: {names[-2]} and {names[-1]}')
        case 1:
            print(Fore.MAGENTA)
            print(f'remainder: {names[-1]}')


#* program *#
while True:
    print(Fore.BLUE, end='')
    tprint('pname', 'nancyj')
    # print(' __                  ___ ')
    # print('|__) |\\ |  /\\  |\\/| |__  ')
    # print('|    | \\| /~~\\ |  | |___ ')           
    print(Fore.GREEN + '|| made by sbird ||')

    print(Fore.MAGENTA)
    print('currently selected list file: ' + chosenListFile + '.txt')

    print(Fore.YELLOW)
    print('What would you like to do?')

    print(Fore.YELLOW)
    print('select a single person:')
    print(Fore.BLUE + '~ web')
    print(Fore.RED + '~ spiderman')
    print(Fore.GREEN + '~ birds')
    print(Fore.BLUE + '~ television')
    print(Fore.RED + '~ reaper')
    print(Fore.MAGENTA + '~ calculator')
    print(Fore.GREEN + '~ golf')
    print(Fore.BLUE + '~ flowers')

    print(Fore.YELLOW)
    print('select pairs:')
    print(Fore.RED + '~ branch')
    print(Fore.BLUE + '~ waterfall')
    print(Fore.MAGENTA + '~ caves')

    print(Fore.YELLOW)
    print('select groups of 4:')
    print(Fore.GREEN + '~ blocks')

    print(Fore.YELLOW)
    print('adjustments:')
    print(Fore.BLUE + '> set list file (default: list)')
    print(Fore.MAGENTA + '> random list file')

    print(Fore.RED)
    print('~ quit')

    print(Fore.YELLOW)
    userAction = input('~~> ').lower() # sets answer as lowercase to avoid miscasing
    
    if userAction in OPTIONS:
        delay = 0
        random.shuffle(names)

        print('\033c', end='') # clear terminal

        for i in range(TRICKLE_TIME):
            r = random.randrange(len(names))
            
            match userAction:
                case 'web': name_web(r)
                case 'spiderman': name_spiderman(r)
                case 'birds' | 'bird': name_birds(r)
                case 'tv' | 'television': name_tv(r)
                case 'calc' | 'calculator': name_calc(r)
                case 'golf': name_golf(r, i)
                case 'reaper' | 'death': name_reaper(r)
                case 'flowers' | 'flower': name_flowers(r)

            time.sleep(delay)
            delay = delay + 0.1 # delay increases every time

            print('\033c', end='') # clear terminal
        
        r = random.randrange(len(names))    

        match userAction:
            case 'web': name_web(r, True)
            case 'spiderman': name_spiderman(r, True)
            case 'birds' | 'bird': name_birds(r, True)
            case 'tv' | 'television': name_tv(r, True)
            case 'calc' | 'calculator': name_calc(r, True)
            case 'golf': name_golf(r, -1, True)
            case 'reaper' | 'death': name_reaper(r, True)
            case 'flowers' | 'flower': name_flowers(r, True)

        time.sleep(1.5)

        print('\033c', end='') # clear terminal

        print(Fore.YELLOW, end='')
        print('|~' + ('~' * len(chosenName)) + '~|')
        print('| ' + Fore.MAGENTA + chosenName + Fore.YELLOW + ' |')
        print('|~' + ('~' * len(chosenName)) + '~|')
        print('')
        input('~~> ')

        print('\033c', end='') # clear terminal
    elif userAction in PAIR_OPTIONS:
        delay = 0
        random.shuffle(names)

        print('\033c', end='') # clear terminal

        match userAction:
            case 'branches' | 'branch': pair_branch()
            case 'waterfall': pair_waterfall()
            case 'caves' | 'cave': pair_caves()
        
        print(Fore.YELLOW)
        input('~~> ')

        print('\033c', end='') # clear terminal
    elif userAction in FOUR_OPTIONS:
        delay = 0
        random.shuffle(names)

        print('\033c', end='') # clear terminal

        match userAction:
            case 'blocks' | 'block': four_blocks()
        
        print(Fore.YELLOW)
        input('~~> ')

        print('\033c', end='') # clear terminal
    elif userAction in SET_OPTIONS:
        print(Fore.MAGENTA)
        print('enter your desired list file (must be a text file)')
        print(Fore.RED + ' ! note: do NOT include file extension. also, make sure list file is in the same directory as pyname !')
        
        # lists all .txt files
        print(Fore.BLUE)
        for i in glob.glob('*.txt'):
            print(f'-> {i}')
        
        print(Fore.YELLOW)
        userFile = input('~~> ')

        try:
            chosenListFile = userFile
            names = setList()

            print(Fore.BLUE)
            print(f'new list file -> {userFile}.txt')

            input('~>')

            print('\033c', end='') # clear terminal
        except:
            call_error(userFile, 'invalid_file')
    elif userAction in RANDOM_SET_OPTIONS:
        fileList = glob.glob('*.txt')

        print(Fore.BLUE)

        if fileList == ['list.txt']:
            print(Fore.BLUE)
            print('new list file -> list.txt')

            chosenListFile = 'list'
        else:
            r = random.randrange(1, len(fileList))
            print(f'new list file -> {fileList[r]}')

            chosenListFile = Path(fileList[r]).stem

        input('~>')

        print('\033c', end='') # clear terminal
    elif userAction ==  'quit' or userAction == 'q':
        sys.exit(0)
    else:
        call_error(userAction)
