import pgzrun ##for game stuff
import random ##for making randomized decisions
import time


WIDTH=540
LENGTH=500


box_list=[]
game_status = 'menu'

dict = {}
#creates a list of blocks
for a in range(126):
    box=str(a)
    box_list.append(box)

#mass produces 120 box actors
for i in range(6):
    n = 27
    for box in box_list[i*10:i*10+10]:
        dict[box]=Actor('circle')
        dict[box].pos=n,25+(i*100)
        n+=54

for i in range(6):
    n = 0
    for box in box_list[(60+(i*11)):60 +(i*11)+11]:
        dict[box]=Actor('circle')
        dict[box].pos=n,75+(i*100)
        n+=54
not_popped = box_list[:]
popped = []


def remove_and_add_list(thing,remover,adder):
    ind = remover.index(thing)
    remover.pop(ind)
    adder.append(thing)

def reset():
    for box in dict:
        dict[box].image = 'circle'

def reset2():
    for box in dict:
        dict[box].image = 'circle2'

def spawn_more_bubbles(last_time):
    global timer, popped, not_popped
    passed = int(time.monotonic())-timer
    if last_time != passed:
        #print(last_time, passed)
        num_to_spawn = (passed // 5)+1
        try:
            for i in range(num_to_spawn):
                    rand = random.choice(not_popped)
                    dict[rand].image = 'circle'
                    remove_and_add_list(rand,not_popped,popped)
        except IndexError:
            pass        
    return passed
            
    
    
    

def on_mouse_down(pos):
    if game_status == "unlimited_pop" or game_status == 'how_fast':
        for box in not_popped:
            if dict[box].collidepoint(pos):
                sounds.pop2.play()
                dict[box].image = 'circle2'
                remove_and_add_list(box,not_popped,popped)
    elif game_status == "rush_mode":
        for box in popped:
            if dict[box].collidepoint(pos):
                sounds.pop2.play()
                dict[box].image = 'circle2'
                remove_and_add_list(box,popped,not_popped)

   
def draw():
    global game_status
    screen.fill("blue")
    if game_status == 'menu':
        screen.draw.text("Welcome to Bubble Wrap!",(20,20),color="black", fontsize=45)
        screen.draw.text("There are 3 different modes:",(20,200),color="black", fontsize=28)
        screen.draw.text("1.Click p for Unlimited Stress Free Popping",(20,225),color="black", fontsize=28)
        screen.draw.text("2.Click q for Rush Mode, see how long you can prevent \nthe screen from being filled by popping bubbles",(20,250),color="black", fontsize=28)
        screen.draw.text("3.Click m for Speed Mode, \nsee how quick you can pop the entire screen",(20,295),color="black", fontsize=28)

        screen.draw.text("Click z at any point to exit the game",(20,540),color="black", fontsize=28)
        screen.draw.text("Click ESC at any point to return from to the menu",(20,565),color="black", fontsize=28)
    elif game_status == "unlimited_pop" or game_status == 'how_fast':
        for box in dict:
                dict[box].draw()
    elif game_status == "rush_mode":
        for box in dict:
                dict[box].draw()

a=0

def update():
    global not_popped,popped, game_status, timer, a
    if keyboard.ESCAPE:
        game_status = "menu"
    if keyboard.z:
        exit()
    if game_status == "menu":
        if keyboard.p:
            reset()
            game_status = 'unlimited_pop'
        if keyboard.q:
            game_status = "rush_mode"
            reset2()
            timer = int(time.monotonic())
            for i in range(10):
                rand = random.choice(not_popped)
                dict[rand].image = 'circle'
                remove_and_add_list(rand,not_popped,popped)
        if keyboard.m:
            reset()
            timer = int(time.monotonic())
            game_status = 'how_fast'
                
    elif game_status == 'unlimited_pop':
        if len(popped) == 126:
            reset()
            not_popped = box_list[:]
            popped = []
    elif game_status == "rush_mode":
        if len(popped) == 126:
            print('game over you lose')
            print('Your time was', int(time.monotonic())-timer)
            time.sleep(4)
            game_status = "menu"
        elif len(not_popped) == 126:
            print('yay, you win')
        else:
            a = spawn_more_bubbles(a)
    elif game_status == 'how_fast':
        if len(popped) == 126:
            print('Your time was', int(time.monotonic())-timer)
            time.sleep(4)
            game_status = "menu"
        
        
    


pgzrun.go()
