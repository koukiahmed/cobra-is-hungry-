import random
import curses

s = curses.initscr() #initialize the screen
curses.curs_set(0)
sh, sw = s.getmaxyx() #hight and width of the screen
w = curses.newwin(sh, sw, 0, 0) #window for the game inside the screen 
w.keypad(1)
w.timeout(100)

snk_x = sw//4 #postion of the snake 
snk_y = sh//2
snake = [
    [snk_y, snk_x], #body of the snake
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh//2, sw//2] #postion of the food 
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT #keybord path

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key #new keybord path

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1: ]: #snake touch the screen or snake body itself
        curses.endwin()
        quit()
      

    new_head = [snake[0][0], snake[0][1]] #snake position

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    snake.insert(0, new_head) #moving the snake with body grow 

    if snake[0] == food: #snake head touch food position in screen 
        food = None
        while food is None: #insert new food in different position 
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI) #add food if new food position is not the same position of snake body
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD) #show the snake body in screen 