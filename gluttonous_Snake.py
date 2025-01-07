import turtle
import random
import time
import math
indicator = 1
grown = 0
food_number = 0
move_x = 0
move_y = 0

def get_status():
    status.pu()
    status.goto(-100, 250)
    status.write("Contact:          Time:          Motion:", font = ('Arial', 14, 'normal'))

def show_contact():
    turtle_contact.clear() 
    turtle_contact.write(contact, font = ('Arial', 14, 'normal'))

def time_running():
    if monster_pos[0] != snake[-1] and len(snake) != 51:
        clock.clear()
        global time
        time += 1
        clock.write(time, font=('Arial', 14, 'normal'))
        win.ontimer(time_running, 1000)

def game_area():
    start_up._tracer(False)
    start_up.pu()
    start_up.goto(-250, -290)
    start_up.pd()
    for step in range(2):
        start_up.fd(500)
        start_up.lt(90)
        start_up.fd(580)
        start_up.lt(90)
    start_up.goto(-250, 210)
    start_up.pensize(3)
    start_up.fd(500)
    start_up.pensize()
    start_up.pu()
    start_up.hideturtle()
    get_status()  

def show_welcome():
    welcome.pu()
    welcome.goto(-200, 50)
    text =""" 
    Welcome to my version of snake ...
    
    You are going to use the 4 arrow keys to move the snake 
    around the screen, trying to consume all the food items 
    before the monster catches you ...
    
    Click anywhere on the screen to start the game, havefun!!
    """
    welcome.write(text, font=('Arial', 12, 'normal'))

def snake_monster_body(x, y, paint, monster_or_snake):
    monster_or_snake.isvisible()
    monster_or_snake.up()
    monster_or_snake.goto(x, y)
    monster_or_snake.shape('square')
    monster_or_snake.color('black', paint)
    monster_or_snake.stamp()

def ini_monster():
    while True:
        poses_x = []
        poses_y = []
        for i in range(-12, 12):
            poses_x.append(20 * i)
            poses_y.append(20 * i - 40)
        global monster_pos
        monster_pos = []
        monster_x = random.choice(poses_x)
        monster_y = random.choice(poses_y)
        if (monster_x - snake[-1][0]) ** 2 + (monster_y - snake[-1][1]) ** 2 >= 6400 and [monster_x, monster_y] not in snake:
            monster_pos.append([monster_x, monster_y])
            break
    snake_monster_body(monster_x, monster_y, 'purple', moving_monoster)

def monster_out(x, y):
    if x == -260 or x == 260 or y == -300 or y == 220:
        return True
    return False

def monster_move():
    if monster_pos[0] in snake:
        global contact
        contact += 1
        show_contact()
    if monster_pos[0] == snake[-1] or len(snake) == 51:
        # hint.pu()
        # hint.color('red')
        # if monster_pos[0] == snake[-1]:
        #     hint.write('Your snake dies!\nPress \'r\' to restart the game.\nPress \'q\' to quit the game.', font=('Arial', 12, 'normal'))
        # elif len(snake) == 51:
        #     hint.write('You win!\nPress \'r\' to restart the game.\nPress \'q\' to quit the game.', font=('Arial', 12, 'normal'))
        # win.listen()
        # win.onkey(lambda: main(), 'r')
        # win.onkey(lambda: win.bye(), 'q')
        return
    else:
        moving_monoster.clear()
        first_quadr = [[20, 0], [0, 20]]
        second_quadr = [[-20, 0], [0, 20]]
        third_quadr = [[-20, 0], [0, -20]]
        forth_quadr = [[20, 0], [0, -20]]
        if snake[-1][0] - monster_pos[0][0] > 0 and snake[-1][1] - monster_pos[0][1] > 0:
            movement = random.choice(first_quadr)

        elif snake[-1][0] - monster_pos[0][0] < 0 and snake[-1][1] - monster_pos[0][1] > 0:
            movement = random.choice(second_quadr)
            
        elif snake[-1][0] - monster_pos[0][0] < 0 and snake[-1][1] - monster_pos[0][1] < 0:
            movement = random.choice(third_quadr)

        elif snake[-1][0] - monster_pos[0][0] > 0 and snake[-1][1] - monster_pos[0][1] < 0:
            movement = random.choice(forth_quadr)

        elif snake[-1][0] == monster_pos[0][0] and snake[-1][1] != monster_pos[0][1]:
            movement = [0, 20 * (snake[-1][1] - monster_pos[0][1]) / (abs(snake[-1][1] - monster_pos[0][1]))]

        elif snake[-1][1] == monster_pos[0][1] and snake[-1][0] != monster_pos[0][0]:
            movement = [20 * (snake[-1][0] - monster_pos[0][0]) / abs((snake[-1][0] - monster_pos[0][0])), 0]

        monster_pos[0][0] += movement[0]
        monster_pos[0][1] += movement[1]
        snake_monster_body(monster_pos[0][0], monster_pos[0][1], 'purple', moving_monoster)
        interval = random.choice([350, 450, 550])
        win.ontimer(monster_move, interval)
        win.update()
    
def draw_snake():
    for body in snake[: -1]:
        snake_monster_body(body[0], body[1], 'green', hungry_snake)
    snake_monster_body(snake[-1][0], snake[-1][1], 'red', hungry_snake)
    win.update()

def ini_snake():
    global snake
    snake = [[0, 0]]

def set_food():
    global growth
    growth = 5
    all_pos = []
    global food_pos
    food_pos = []
    global food_number
    food_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    global all_food
    all_food = []
    for i in range(-12, 12):
        for j in range(-12, 12):
            all_pos.append([20 * i, 20 * j - 50])
    for i in range(9):
        while True:
            random_food = random.choice(all_pos)
            if random_food not in snake and random_food not in monster_pos:
                food_pos.append(random_food)
                all_pos.remove(random_food)
                break

def print_food():
    welcome.clear()
    if not monster_pos[0] == snake[-1]:
        for i in range(9):
            food = turtle.Turtle()
            food.hideturtle()
            food.pu()
            if food_number[i] != 'empty':
                food.goto(food_pos[i][0], food_pos[i][1])
                food.write(food_number[i], align="center", font=('Arial', 12, 'normal'))
                all_food.append(food)
            else:
                pass

def judge_eating(n):
    if food_pos[n][0] == snake[-1][0] and food_pos[n][1] - snake[-1][1] == -10:
        if food_number[n] != 'empty':
            global growth
            growth += (n + 1)
            food_number[n] = 'empty'
            all_food[n].clear()
            win.update()

def turn(direction):
    global indicator
    indicator = 1
    global move_x, move_y
    if direction == 'Left':
        move_x = -20
        move_y = 0
    elif direction == 'Right':
        move_x = 20
        move_y = 0
    elif direction == 'Up':
        move_x = 0
        move_y = 20
    elif direction == 'Down':
        move_x = 0
        move_y = -20 

def pause():
    global indicator
    indicator *= -1
    motion.clear()
    motion.write('Pause', font=('Arial', 14, 'normal'))

def snake_move():
    delay = 0
    if monster_pos[0] == snake[-1] or len(snake) == 51:
        hint.pu()
        hint.color('red')
        if monster_pos[0] == snake[-1]:
            hint.write('Your snake dies!\nPress \'r\' to restart the game.\nPress \'q\' to quit the game.', font=('Arial', 12, 'normal'))
        elif len(snake) == 51:
            hint.write('You win!\nPress \'r\' to restart the game.\nPress \'q\' to quit the game.', font=('Arial', 12, 'normal'))
        win.listen()
        win.onkey(lambda: main(), 'r')
        win.onkey(lambda: win.bye(), 'q')
        return
    else:
        global indicator
        if indicator == -1:
            win.ontimer(snake_move, 300)
            return
        else:
            if (move_x, move_y) == (20, 0):
                motion.clear()
                motion.write('Right', font=('Arial', 14, 'normal'))
            elif (move_x, move_y) == (-20, 0):
                motion.clear()
                motion.write('Left', font=('Arial', 14, 'normal'))
            elif (move_x, move_y) == (0, 20):
                motion.clear()
                motion.write('Up', font=('Arial', 14, 'normal'))
            elif (move_x, move_y) == (0, -20):
                motion.clear()
                motion.write('Down', font=('Arial', 14, 'normal'))
            for i in range(9):
                judge_eating(i)
            if snake[-1][0] + move_x == 260 or snake[-1][0] + move_x == -260 or snake[-1][1] + move_y == 220 or snake[-1][
                1] + move_y == -300:
                None
            else:
                snake.append([snake[-1][0] + move_x, snake[-1][1] + move_y])
                global grown
                if grown < growth:
                    grown += 1
                    if 'empty' in food_number:
                        delay = 200
                else:
                    snake.remove(snake[0])
                hungry_snake.clear()
                draw_snake()
                snake_monster_body(monster_pos[0][0], monster_pos[0][1], 'purple', moving_monoster)
        win.ontimer(snake_move, 300 + delay)
        win.update()
                    
            



    
    # motion.write(direction, font = 12) 

def ready():
    win.clear()
    global status
    status = turtle.Turtle()
    status.hideturtle()
    global contact
    contact = 0
    global turtle_contact
    turtle_contact = turtle.Turtle()
    turtle_contact.hideturtle()
    turtle_contact.pu()
    turtle_contact.goto(-41, 250)
    turtle_contact.write(contact, font=('Arial', 14, 'normal'))
    global time
    time = -1
    global clock
    clock = turtle.Turtle()
    clock.hideturtle()
    clock.pu()
    clock.goto(30, 250)
    clock.write('0', font=('Arial', 14, 'normal'))
    global motion
    motion = turtle.Turtle()
    motion.hideturtle()
    motion.pu()
    motion.goto(120, 250)
    motion.write('Pause', font = ('Arial', 14, 'normal'))
    global welcome
    welcome = turtle.Turtle()
    welcome.hideturtle()
    global hungry_snake
    hungry_snake = turtle.Turtle()
    hungry_snake.hideturtle()
    global start_up
    start_up = turtle.Turtle()
    start_up.hideturtle()
    global moving_monoster
    moving_monoster = turtle.Turtle()
    moving_monoster.hideturtle()
    global hint
    hint = turtle.Turtle()
    hint.hideturtle()

    game_area()
    show_welcome()
    ini_snake()
    draw_snake()
    ini_monster()
    set_food()

def start_game(x, y):
    win.onscreenclick(None)
    time_running()
    print_food()
    monster_move()
    win.onkeypress(lambda: pause(), 'space')
    win.onkey(lambda: turn('Left'), 'Left')
    win.onkey(lambda: turn('Right'), 'Right')
    win.onkey(lambda: turn('Up'), 'Up')
    win.onkey(lambda: turn('Down'), 'Down') 
    snake_move()   

def main():
    global win
    win = turtle.Screen()
    win.setup(660, 740)
    win.listen()
    global indicator
    indicator = 1
    global grown
    grown = 0
    global food_number
    food_number = 0
    global move_x, move_y
    move_x = 0
    move_y = 0
    ready()
    win.onscreenclick(start_game)
    win.mainloop()

main()
