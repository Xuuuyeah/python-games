import random
# function part
def movement_by_user():                                             # let user set the corresponding letter to a certain direction
    comms = list()                                                  # all the commands set by user
    global movements
    movements = {'left':1, 'down':2, 'right':3, 'up':4}
    for direction in movements.keys():
        while True:
            movements['%s' %direction] = input('enter a letter for %s:' %direction)
            if movements['%s' %direction].isalpha() == True:        # judge whether is a letter
                if len(set(movements.values())) == 4:               # judge whether they are the same
                    if len(movements['%s' %direction]) == 1:        # judge whether they are one letter 
                        comms.append(movements['%s' %direction])
                        break
            print('enter one letter for each direction')
    global left,down,up,right
    left,down,right,up = comms[0],comms[1],comms[2],comms[3]
              
def disorder():                                                     # disorder the goal matrix
    global random_true
    random_true = 1                      # to differentiate movement by disorder or by user
    time = 0                             # time of random disorder
    while True:
        random_disorder = random.choice([left , right, down, up])
        move(random_disorder)
        time += 1
        if time == (n**5) : return make_matrix()  # less numbers, less times of random

def make_matrix():                                                  # covert list to matrix
    for line in range(int(n)):
        for column in range(int(n)):
            if li[(n * line) + column] == 0:
                print('%-5s' % ' ', end='')
            else:
                print('%-5s' % li[(n * line) + column], end='')
        print()
        print()

def move(command):                                                  # switch each other in the list
    global pos,movements
    pos = li.index(0)                                               # the position of 0 in the list
    movements = [left+'-left',down+'-down',right+'-right',up+'-up'] # original movements
    protection = 0                       # prevent user inputting things other than 'wasd'
    out_of_index = 0                     # prevent all numbers can not move to certain direction

    for search_0 in range(1, n + 1):     # give user hint that the numbers can not move to a certain direction
        if pos == (search_0 * n) - 1: movements[0] = ''
        if pos == (search_0 * n): movements[2] = ''
        if pos == n ** 2 - n + search_0: movements[3] = ''
        if pos == search_0: movements[1] = ''

    if command == left:                  # move to left
        protection = 1                   # valid input when protection = 1
        for search in range(1, n + 1):
            if pos == (search * n) - 1: out_of_index = 1
        if out_of_index == 0:            # the space is not on the boundary
            li[pos], li[pos + 1] = li[pos + 1], li[pos]
        elif out_of_index == 1 and random_true == 0:
            print("can't move to left anymore")

    elif command == right:               # move to right
        protection = 1
        for search in range(n):
            if pos == (search * n): out_of_index = 1
        if out_of_index == 0:
            li[pos], li[pos - 1] = li[pos - 1], li[pos]
        elif out_of_index == 1 and random_true == 0:
            print("can't move to right anymore")

    elif command == up:                  # move up
        protection = 1
        for search in range(n):
            if pos == n ** 2 - n + search: out_of_index = 1
        if out_of_index == 0:
            li[pos], li[pos + n] = li[pos + n], li[pos]
        elif out_of_index == 1 and random_true == 0:
            print("can't move upward anymore")

    elif command == down:                # move down
        protection = 1
        for search in range(n):
            if pos == search: out_of_index = 1
        if out_of_index == 0:
            li[pos], li[pos - n] = li[pos - n], li[pos]
        elif out_of_index == 1 and random_true == 0:
            print("can't move downward anymore")
    if protection == 0 and random_true == 0: print("please enter "+ left,right,up,down +"to move the number")

# operating part
print('---------------------------------------------------------------------------------------------------------------------------------------------------------------')
print("welcome to the sliding number of evil version!!!")

while True:
    while True:
        try:                                                        # prevent numbers other than 3 to 10
            global n
            n = int(input('Enter the desired dimension of the puzzle:'))
            if int(n) == n and n in range(3, 11):
                print("let's rock!!!!!!")
                break
            else: print('please enter a integer from 3 to 10:')
        except: print('please enter a integer from 3 to 10:')

    li = []                                                         # operating list
    win_criterion = []                                              # comparing list
    for dig in range(1, n ** 2): li.append(dig), win_criterion.append(dig)
    li.append(0), win_criterion.append(0)

    movement_by_user()
    disorder()                                                      # produce random matrix

    random_true = 0                                                 # users' turn
    counter = 0                                                     # count steps
    while True:
        global command
        command = input("enter your move"+' '+' '.join(movements)+':')
        move(command)
        counter += 1
        make_matrix()
        if li == win_criterion:
            print('you win!!!')
            print('total steps:', counter)
            break
    while True:
        choice = input("Enter ‘n’ to start a new game or enter ‘q’ to end the game:")
        if choice == 'q' or choice == 'n': break
    if choice == 'q':
        print('thanks for playing!')
        break
