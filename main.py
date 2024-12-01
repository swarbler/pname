import random, time, math, sys
from colorama import Fore, Back, Style

#* declaring variables *#
with open('list.txt', 'r') as l:
    names = l.read().split()

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
                print(Fore.MAGENTA + names[i][:nLengthMax].upper() + Fore.BLUE, end='')

                chosenName = names[i] # sets chosen name to selected name
            else:
                print(Fore.GREEN + names[i][:nLengthMax].upper() + Fore.BLUE, end='')
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

    r2, r3, r4, r5 = random.randrange(0, len(names)), random.randrange(0, len(names)), random.randrange(0, len(names)), random.randrange(0, len(names))

    print(Fore.RED, end='')
    print('  _                                                                        ')
    print(' _\\`.                                                                      ')
    print(' \\_)-`""---""""--.                                                         ')
    print('/.--     _        `._                                                      ')
    print('`_.-\'.-. \\"-.   ,--. \\                                                     ')
    if last:
        print('`---"   `.;  `.\' -. `."-.               ' + Fore.MAGENTA + names[r1][:30] + Fore.RED)
    else:
        print('`---"   `.;  `.\' -. `."-.               ' + Fore.GREEN + names[r1][:30] + Fore.RED)
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

def name_birds(selectedNumber, last=False):
    """creates birds"""
    global chosenName

    print(Fore.CYAN, end='')
    print('   (                          \\\\')
    if last:
        print('  `-`-.               \\\\      (->')
        print('  \'( - >              (->     //\\      ' + Fore.MAGENTA + names[selectedNumber][:20] + Fore.CYAN)
    else:
        print('  `-`-.               \\\\      (o>')
        print('  \'( O >              (o>     //\\      ' + Fore.GREEN + names[selectedNumber][:20] + Fore.CYAN)
    print('   _) (           ____(()_____V_/_____')
    print('  /    )              ||      ||               ,_,')
    if last:
        print(' /_,\'  /                     ||               (.,.)')
    else:
        print(' /_,\'  /                     ||               (O,O)')
    print('   \\  /                                       (   )')
    print('===m""m=========================         ------"-"-------')

    if last:
        chosenName = names[selectedNumber]

def name_tv(selectedNumber, last=False):
    """creates tv"""
    global chosenName

    print(Fore.GREEN, end='')
    print(' _____________________     ')
    print('|,----------------.  |\\    ')
    print('||                 |=| |   ')
    if last:
        print('|| ' + Fore.MAGENTA + names[selectedNumber][:14] + ' ' * (14 - len(names[selectedNumber][:14])) + Fore.GREEN + ' || | |   ')
    else:
        print('|| ' + Fore.BLUE + names[selectedNumber][:14] + ' ' * (14 - len(names[selectedNumber][:14])) + Fore.GREEN + ' || | |   ')
    print('||             . _o| | | __')
    print('|`-----------------\' |/ /~/')
    print(' ~~~~~~~~~~~~~~~~~~~~~ / / ')
    print('                       ~~  ')

    if last:
        chosenName = names[selectedNumber]

def name_calc(selectedNumber, last=False):
    """creates calculator"""
    global chosenName

    print(Fore.GREEN, end='')
    print(' __________ ')
    print('| ________ |')
    if last:
        print('||' + Fore.MAGENTA + names[selectedNumber][:8] + ' ' * (8 - len(names[selectedNumber][:8])) + Fore.GREEN + '||')
    else:
        print('||' + Fore.BLUE + names[selectedNumber][:8] + ' ' * (8 - len(names[selectedNumber][:8])) + Fore.GREEN + '||')
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

    r2, r3, r4 = random.randrange(0, len(names)), random.randrange(0, len(names)), random.randrange(0, len(names))

    rselect = random.randrange(0, 4)

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
    global chosenName

    r2, r3, r4, r5, r6, r7, r8 = random.randrange(0, len(names)), random.randrange(0, len(names)), random.randrange(0, len(names)), random.randrange(0, len(names)), random.randrange(0, len(names)), random.randrange(0, len(names)), random.randrange(0, len(names))

    rselect = random.randrange(0, 8)

    print(Fore.RED, end='')

    print('                       ,____')
    print('                   |---.\\   ')
    print('           ___     |    `   ')
    print('          / .-\\  ./=)       ')
    if last:
        if rselect == 0:
            print('         |  |*|_/\\/|        ' + Fore.MAGENTA + names[r1][:30] + Fore.RED)
        else:
            match rselect:
                case 1: print('         |  |*|_/\\/|        ' + Fore.BLUE + names[r2][:30] + Fore.RED)
                case 2: print('         |  |*|_/\\/|        ' + Fore.BLUE + names[r3][:30] + Fore.RED)
                case 3: print('         |  |*|_/\\/|        ' + Fore.BLUE + names[r4][:30] + Fore.RED)
                case 4: print('         |  |*|_/\\/|        ' + Fore.BLUE + names[r5][:30] + Fore.RED)
                case 5: print('         |  |*|_/\\/|        ' + Fore.BLUE + names[r6][:30] + Fore.RED)
                case 6: print('         |  |*|_/\\/|        ' + Fore.BLUE + names[r7][:30] + Fore.RED)
                case 7: print('         |  |*|_/\\/|        ' + Fore.BLUE + names[r8][:30] + Fore.RED)
    else:
        print('         |  |"|_/\\/|        ' + Fore.BLUE + names[r1][:30] + Fore.RED)
    if last and rselect == 1:
        print('         ;  |-;| /_|        ' + Fore.MAGENTA + names[r1][:30] + Fore.RED)
    else:
        print('         ;  |-;| /_|        ' + Fore.BLUE + names[r2][:30] + Fore.RED)
    if last and rselect == 2:
        print('        / \\_| |/ \\ |        ' + Fore.MAGENTA + names[r1][:30] + Fore.RED)
    else:
        print('        / \\_| |/ \\ |        ' + Fore.BLUE + names[r3][:30] + Fore.RED)
    if last and rselect == 3:
        print('       /      \\/\\( |        ' + Fore.MAGENTA + names[r1][:30] + Fore.RED)
    else:
        print('       /      \\/\\( |        ' + Fore.BLUE + names[r4][:30] + Fore.RED)
    if last and rselect == 4:
        print('       |   /  |` ) |        ' + Fore.MAGENTA + names[r1][:30] + Fore.RED)
    else:
        print('       |   /  |` ) |        ' + Fore.BLUE + names[r5][:30] + Fore.RED)
    if last and rselect == 5:
        print('       /   \\ _/    |        ' + Fore.MAGENTA + names[r1][:30] + Fore.RED)
    else:
        print('       /   \\ _/    |        ' + Fore.BLUE + names[r6][:30] + Fore.RED)
    if last and rselect == 6:
        print('      /--._/  \\    |        ' + Fore.MAGENTA + names[r1][:30] + Fore.RED)
    else:
        print('      /--._/  \\    |        ' + Fore.BLUE + names[r7][:30] + Fore.RED)
    if last and rselect == 7:
        print('      `/|)    |    /        ' + Fore.MAGENTA + names[r1][:30] + Fore.RED)
    else:
        print('      `/|)    |    /        ' + Fore.BLUE + names[r8][:30] + Fore.RED)
    print('        /     |   |         ')
    print('      .\'      |   |         ')
    print('jgs  /         \\  |         ')
    print('    (_.-.__.__./  /         ')

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
    print('~ birds')
    print('~ television')
    print('~ calculator')
    print('~ golf')
    print('~ reaper')
    print('~ quit')
    print('')
    userAction = input('~~> ').lower() # sets answer as lowercase to avoid miscasing
    
    match userAction:
        case 'web' | 'spiderman' | 'birds' | 'bird' | 'tv' | 'television' | 'calc' | 'calculator' | 'golf' | 'reaper' | 'death':
            delay = 0
            random.shuffle(names)

            for i in range(trickleTime):
                r = random.randrange(0, len(names))
                
                match userAction:
                    case 'web':
                        name_web(r)
                    case 'spiderman':
                        name_spiderman(r)
                    case 'birds' | 'bird':
                        name_birds(r)
                    case 'tv' | 'television':
                        name_tv(r)
                    case 'calc' | 'calculator':
                        name_calc(r)
                    case 'golf':
                        name_golf(r, i)
                    case 'reaper' | 'death':
                        name_reaper(r)

                time.sleep(delay)
                delay = delay + 0.1 # delay increases every time

                print('\033c', end='') # clear terminal
            
            r = random.randrange(0, len(names))    

            match userAction:
                case 'web':
                    name_web(r, True)
                case 'spiderman':
                    name_spiderman(r, True)
                case 'birds' | 'bird':
                    name_birds(r, True)
                case 'tv' | 'television':
                    name_tv(r, True)
                case 'calc' | 'calculator':
                    name_calc(r, True)
                case 'golf':
                    name_golf(r, -1, True)
                case 'reaper' | 'death':
                    name_reaper(r, True)

            time.sleep(0.8)

            print('\033c', end='') # clear terminal

            print(Fore.YELLOW, end='')
            print('|~' + ('~' * len(chosenName)) + '~|')
            print('| ' + Fore.MAGENTA + chosenName + Fore.YELLOW + ' |')
            print('|~' + ('~' * len(chosenName)) + '~|')
            print('')
            input('~~> ')

            print('\033c', end='') # clear terminal
        case 'quit' | 'q':
            sys.exit(0)
        case _:
            call_error(userAction)
