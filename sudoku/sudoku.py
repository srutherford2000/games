import pgzrun ##for game stuff
import math   ##for trig stuff
import random ##for making randomized decisions
import time

mistake = 0 

WIDTH=542
LENGTH=550

vert1 = Actor('vertical')
vert1.pos = 180,0
vert2 = Actor('vertical')
vert2.pos = 360,0
hor1 = Actor('horizontal')
hor1.pos = 0,180
hor2 = Actor('horizontal')
hor2.pos = 0,360
vert0 = Actor('vertical')
vert0.pos = 0,0
vert3 = Actor('vertical')
vert3.pos = 540,0
hor0 = Actor('horizontal')
hor0.pos = 0,0
hor3 = Actor('horizontal')
hor3.pos = 0,540 

sudoku = ["9","4","6"," "," "," ","8","3",' ',
          " "," ","8","9"," ",' ',' ','4','5',
          ' ','7','3',' ',' ','2','1','9','6',
          ' ',' '," ","2"," ",' '," "," ","1",
          " ",'9'," ","1",' ',' ','3','7','8',
          '8',' ',' ',' ',' ',' ','4',' ',' ',
          ' ',' ','1','7','2','6','9',' ',' ',
          '4','6',' ',' ','1',' ','2',' ',' ',
          '2','8',' ',' ','9',' ','6',' ','3']
solution = ['9','4','6','5','7','1','8','3','2',
            '1','2','8','9','6','3','7','4','5',
            '5','7','3','8','4','2','1','9','6',
            '7','3','4','2','8','9','5','6','1',
            '6','9','2','1','5','4','3','7','8',
            '8','1','5','6','3','7','4','2','9',
            '3','5','1','7','2','6','9','8','4',
            '4','6','9','3','1','8','2','5','7',
            '2','8','7','4','9','5','6','1','3']


box_list=[]
dict = {}
#creates a list of blocks
for a in range(81):
    box=str(a)
    box_list.append(box)

#mass produces 81 box actors
for i in range(9):
    n = 30
    for box in box_list[i*9:i*9+9]:
        dict[box]=Actor('square')
        dict[box].pos=n,30+(i*60)
        n+=60

chosen_block = ""
start = False

def check_square(num):
    global mistake
    if sudoku[int(chosen_block)] == " ":
        if num ==solution[int(chosen_block)]:
            sudoku[int(chosen_block)] = num
        else:
            mistake += 1
            print("that number was wrong!")
            print("you now have", mistake, "mistakes.")
    else:
        print("this was a given number! don't try to change it")


def check_numbers():
    global chosen_block, start, sudoku
    if keyboard.k_1 and start:
            check_square("1")
            start = False
    elif keyboard.k_2 and start:
        check_square("2")
        start = False
    elif keyboard.k_3 and start:
        check_square("3")
        start = False
    elif keyboard.k_4 and start:
        check_square("4")
        start = False
    elif keyboard.k_5 and start:
        check_square("5")
        start = False
    elif keyboard.k_6 and start:
        check_square("6")
        start = False
    elif keyboard.k_7 and start:
        check_square("7")
        start = False
    elif keyboard.k_8 and start:
        check_square("8")
        start = False
    elif keyboard.k_9 and start:
        check_square("9")
        start = False
    

def on_mouse_down(pos):
    global chosen_block, start
    for box in dict:
        if dict[box].collidepoint(pos):
            chosen_block = box
            start = True
def draw():
    global sudoku
    screen.fill("white")
    for box in dict:
            dict[box].draw()
    vert1.draw()
    vert2.draw()
    hor1.draw()
    hor2.draw()
    vert0.draw()
    vert3.draw()
    hor0.draw()
    hor3.draw()
    for i, num in enumerate(sudoku):
        screen.draw.text(num, (23+((i%9)*60),20+((i//9)*60)),color="black", fontsize=30)
        

def update():
    check_numbers()


pgzrun.go()
