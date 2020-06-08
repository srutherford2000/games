'''
Project Name:Team Wobble Stick
File: project_skeleton.py
Project Team: Jason Jeong, Sarah Rutherford

This is our final project. 

This game starts at a home page where you can select one of two games to play by
clicking on a picture of a game. The games are Pong and Breakout. Pong is a
two player game where you compete for points and win once you get to get 11
points. Breakout is a single player game in which you try to break as many(or
all the bricks). It keeps track and allows you to input high scores in order
to help people stay motivated to play it. Both games are keyboard operated, using
arrow keys, w and s. The escape key is also active and can be used to return to
the home screen. The q key exits the program. 

The update and draw functions are broken down by game statuses, which allow
the program to only execute a set of code depending on the part of the game.
This is not only helpful for orginization but also for efficency of the code.
The game statuses are as shown below:
0 opening/home page pick between games
B0 breakout home page
B1 breakout playing
B2 breakout gameover
B3 breakout highscores
PauseB breakout paused
B4 breakout win
P0 pong home page
P1 pong playing
P2 pong gameover
PauseP pong paused

The edits made since our demo were to fix the random on the pong, and add the
pause phase for both breakout and pong. Additionally we chose to tell the program
to sleep before reseting the ball and coninuting play in pong as to prevent
it from simply killing one person over and over because they weren't ready.
This does cause a little of a lag look but we think this is better then losing
a point, not being prepared and immidiatly losing another point. 

No excessivly obscure libraries are needed for this program. We do import the
pgzrun library (in order to have the game functions), the math library (to use
the trig functions for the angle of the ball), the random library(to randomly
assign angles), and the time library (in order to keep track of time and delay
some steps in the program).
'''


import pgzrun ##for game stuff
import math   ##for trig stuff
import random ##for making randomized decisions
import time   ##for creating a game clock
 
WIDTH=650
LENGTH=650
 
do_get_initials=0
game_status=0
dict={}
box_list=[]
high_scores=[[0,'aaa'],[0,'aaa'],[0,'aaa'],[0,'aaa'],[0,'aaa']]

##possible statuses
#0 opening/home page pick between games
#B0 breakout home
#B1 breakout playing
#B2 breakout gameover
#B3 breakout highscores
#B4 breakout win
#P0 pong home
#P1 pong playing
#P2 pong gameover
 
 
##create the actors
#pong actors
pong_left_player=Actor('pong_player_image')
pong_right_player=Actor('pong_player_image')
#both actor
ball=Actor('ball')
#breakout actors
top_bound=Actor('horizontal_bound')
top_bound.pos=325,25
bottom_bound=Actor('horizontal_bound')
bottom_bound.pos=325,625
left_bound=Actor('vertical_bound')
left_bound.pos=25,325
right_bound=Actor('vertical_bound')
right_bound.pos=625,325
breakout_player=Actor('breakout_player_image')

#creates a list of blocks
for i in 'abcdefghijkl':
    for a in range(12):
        box=str(i)+str(a)
        box_list.append(box)
    
def board_setup():
    global box_list
    n=50
    for box in box_list[:12]:
        dict[box]=Actor('purple_square')
        dict[box].pos=n,37.5
        n+=50
    n=50
    for box in box_list[12:24]:
        dict[box]=Actor('purple_square')
        dict[box].pos=n,62.5
        n+=50
    n=50
    for box in box_list[24:36]:
        dict[box]=Actor('blue_square')
        dict[box].pos=n,87.5
        n+=50
    n=50
    for box in box_list[36:48]:
        dict[box]=Actor('blue_square')
        dict[box].pos=n,112.5
        n+=50
    n=50
    for box in box_list[48:60]:
        dict[box]=Actor('green_square')
        dict[box].pos=n,137.5
        n+=50
    n=50
    for box in box_list[60:72]:
        dict[box]=Actor('green_square')
        dict[box].pos=n,162.5
        n+=50
    n=50
    for box in box_list[72:84]:
        dict[box]=Actor('yellow_square')
        dict[box].pos=n,187.5
        n+=50
    n=50
    for box in box_list[84:96]:
        dict[box]=Actor('yellow_square')
        dict[box].pos=n,212.5
        n+=50
    n=50
    for box in box_list[96:108]:
        dict[box]=Actor('orange_square')
        dict[box].pos=n,237.5
        n+=50
    n=50
    for box in box_list[108:120]:
        dict[box]=Actor('orange_square')
        dict[box].pos=n,262.5
        n+=50
    n=50
    for box in box_list[120:132]:
        dict[box]=Actor('red_square')
        dict[box].pos=n,287.5
        n+=50
    n=50
    for box in box_list[132:144]:
        dict[box]=Actor('red_square')
        dict[box].pos=n,312.5
        n+=50

def breakout_check_keys():
    if keyboard.left:
        breakout_player.x -=4
    if keyboard.right:
        breakout_player.x +=4

def breakout_player_movement():
    global box_list
    #user hits wall
    if breakout_player.colliderect(left_bound):
        breakout_player.x+=2
    elif breakout_player.colliderect(right_bound):
        breakout_player.x-=2
    else:
        breakout_check_keys()

current_angle=300

def breakout_ball_movement():
    global current_angle,score, ball_speed
    #if moving up with a right angle
    collide=0
    for i in box_list:
        if ball.colliderect(dict[i]):
            if dict[i].image=='red_square':
                score+=1
            elif dict[i].image=='orange_square':
                score+=2
            elif dict[i].image=='yellow_square':
                score+=3
            elif dict[i].image=='green_square':
                score+=4
            elif dict[i].image=='blue_square':
                score+=5
            elif dict[i].image=='purple_square':
                score+=6
            dict[i].pos=1000,1000
            collide=1
            break
    collide_user=0
    if ball.colliderect(breakout_player):
        collide_user=1               
    if 270<=current_angle<=360:
        if ball.colliderect(right_bound):
            current_angle=random.randint(180,270)
        if collide==1:    
            current_angle=random.randint(0,90)   
    #if moving up with a left angle
    elif 180<=current_angle<270:
        if ball.colliderect(left_bound):
            current_angle=random.randint(270,360)  
        if collide==1:    
            current_angle=random.randint(90,180) 
    #if moving down with a left angle
    elif  90<=current_angle<180:
        if ball.colliderect(left_bound):
            current_angle=random.randint(0,90)     
        if collide==1 or collide_user==1:    
            current_angle=random.randint(180,270)   
    #if moving down with a right angle
    elif  0<=current_angle<90:
        if ball.colliderect(right_bound):
            current_angle=random.randint(90,180)  
        if collide==1 or collide_user==1:    
            current_angle=random.randint(270,360)  
    ball.x+=(ball_speed*math.cos(math.radians(current_angle)))
    ball.y+=(ball_speed*math.sin(math.radians(current_angle)))

def breakout_check_lost():
    global game_status
    if ball.colliderect(bottom_bound):
        game_status='B2'
        

def breakout_check_win():
    global box_list, boxes_hit
    boxes_hit=0
    for i in box_list:
        if dict[i].pos== (1000,1000):
            boxes_hit+=1
    if boxes_hit ==144:
        game_status == 'B4'

def create_high_score(score):
    global high_scores
    high_scores.append([score,'NEW'])
    high_scores.sort()
    high_scores.reverse()
    high_scores=high_scores[:5]

def get_initials(score):
    '''
    allows a person to alter thier initials for thier high score
    using the up down key to switch the letter and the left right
    key to swith what letter is being changed
    '''
    global high_scores, char, what_to_adjust
    letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    initials=high_scores[what_to_adjust][1]
    current_letter=letters.find(initials[char])
    if keyboard.up:
        current_letter+=1
        if current_letter>51:
            current_letter-=51
        new_letter=letters[current_letter]
        initials=initials[:char]+new_letter+initials[char+1:]          
    if keyboard.down:
        current_letter-=1
        if current_letter<0:
            current_letter+=51
        new_letter=letters[current_letter]
        initials=initials[:char]+new_letter+initials[char+1:]
    if keyboard.left:
        char-=1
        if char==-1:
            char=2
    if keyboard.right:
        char+=1
        if char==3:
            char=0
    high_scores[what_to_adjust]=[score,initials]

def breakout_change_ball_speed(boxes):
    global ball_speed
    if boxes%5==0:
        speed_increase=boxes//5
        ball_speed= 5+ (speed_increase*.2)

def reset_breakout():
    global game_status, current_angle, score, ball_speed
    game_status = 'B1'
    score=0
    ball_speed=5
    board_setup()
    ball.pos=325,582.5
    breakout_player.pos=325,600
    current_angle=300
 
 
def pong_player_movement():
    '''
    check the up/down keys to see if the right_pong_player moved, if key clicked, 
    add/subtract 4 to the position. 
    check the w/s keys to see if the left_pong_player moved, if key clicked, 
    add/subtract 4 to the position.
    restrict player from moving off the screen
    '''
    if keyboard.up:
        pong_right_player.y-=8
    elif keyboard.down:
        pong_right_player.y+=8
    if keyboard.w:
        pong_left_player.y-=8
    elif keyboard.s:
        pong_left_player.y+=8
    if pong_left_player.y<50:
        pong_left_player.y+=8
    elif pong_left_player.y>550:
        pong_left_player.y-=8
    if pong_right_player.y<50:
        pong_right_player.y+=8
    elif pong_right_player.y>550:
        pong_right_player.y-=8 
 
def pong_ball_movement():
    global current_angle
    '''
    Based on current angle of the ball, move th ball to its next position.
    '''
    ball.x+=8*math.cos(math.radians(current_angle))
    ball.y+=8*math.sin(math.radians(current_angle))
    
 
def pong_collision():
    global current_angle,left_score, right_score
    '''
    When the ball hits either of the players, it bounces toward the opposite side. 
    When the ball hits the top or the bottom wall, it also bounces toward the 
    other side. When the ball hits the left or right wall, the player at the 
    opposite side of the wall gains a point.
    '''
    #check crash into top/bottom wall (bounce off)
    if ball.y<0:
        if 180<=current_angle<270:
            current_angle= random.randint(90,180)
        elif 270<=current_angle<360:
            current_angle= random.randint(0,90)
    elif ball.y>600:
        if 0<=current_angle<90:
            current_angle= random.randint(270,360)
        elif 90<=current_angle<180:
            current_angle= random.randint(180,270)
    #check crash into plater (bounce off)
    if pong_left_player.colliderect(ball):
        if 180<=current_angle<270:
            current_angle= 360-(current_angle-180)
        elif 90<=current_angle<180:
            current_angle=180-current_angle
    elif pong_right_player.colliderect(ball):
        if 270<=current_angle<360:
            current_angle=180+(360-current_angle)
        elif 0<=current_angle<90:
            current_angle=90+(90-current_angle)
    #check crash into left/right wall(award point, reset ball)
    if ball.x>650 or ball.x<0:
        if ball.x>650:
            left_score+=1
        else:
            right_score+=1
        reset_pong()
    
    
def reset_pong():
    global game_status, current_angle
    current_angle=random.randint(0,360)
    ball.pos=325,325
    pong_left_player.pos=40,300
    pong_right_player.pos=610,300
    game_status='P1'
    time.sleep(.8)
 
def pong_check_game_over():
    global left_score, right_score, game_status
    if left_score>10 or right_score>10:
        game_status='P2'
    
 
def on_mouse_down(pos):
    global game_status
    if game_status==0:
        if pos[0]>300:
            game_status='P0'
        elif pos[0]<300:
            game_status='B0'
 
def draw():
    global left_score, right_score,game_status
    if game_status==0: #choose between the two games
        screen.blit('homepage', (0,0)) # Homepage_image contains a photo of each 
                                           # game where upon the user’s click on the 
                                           # photo initiates that game. 
        screen.draw.text("Click ESC at anytime to return to here", (185, 0),color="white", fontsize=24)        
        screen.draw.text("Click q at anytime to exit program", (195, 20),color="white", fontsize=24)
    elif game_status=='B0':
        screen.clear()
        screen.fill('black')
        screen.draw.text("Click Enter to Start", (175, 300),color="white", fontsize=48)
    elif game_status=='B1':
        screen.clear()
        screen.fill('black')
        top_bound.draw()
        bottom_bound.draw()
        left_bound.draw()
        right_bound.draw()
        breakout_player.draw()
        ball.draw()
        for box in dict:
            dict[box].draw()
        screen.draw.text("Score: "+str(score), (25, 10),color="white", fontsize=24)
    elif game_status=='B2':
        screen.draw.text("GAME OVER", (220, 330),color="white", fontsize=48)
        screen.draw.text("Click Enter", (230, 370),color="white", fontsize=48)
    elif game_status =='B3':
        screen.clear()
        screen.draw.text('HIGH SCORES',(220, 50),color="white", fontsize=48)
        for i in range(5):
            screen.draw.text(str(i+1)+'.'+str(high_scores[i][1])+'   '+str(high_scores[i][0]), (100, 100+40*i),color="white", fontsize=32)
        screen.draw.text('If you made a new high score, input it using arrow keys',(100,550),color="white", fontsize=24)
        screen.draw.text('Click shift and enter simaltaneously to play again',(100, 570),color="white", fontsize=24)
    elif game_status=='B4':
        screen.draw.text("YOU WIN!!!", (220, 330),color="white", fontsize=48)
        screen.draw.text("Click Enter to Start", (175, 370),color="white", fontsize=48)
    elif game_status=='P0': #pong home
        screen.clear()
        screen.fill('black')
        screen.draw.text("CLICK ENTER TO START", (135, 290),color="white", fontsize=48)
    elif game_status=='P1': #pong playing
        screen.clear()
        screen.blit('background',(0,0))
        pong_left_player.draw()
        pong_right_player.draw()
        ball.draw()
        screen.draw.text(str(left_score), (175, 20),color="white", fontsize=48)
        screen.draw.text(str(right_score), (475, 20),color="white", fontsize=48)
    elif game_status=='P2': #pong gameover
        if left_score>right_score:
            screen.draw.text('Left Player Wins!', (210, 300),color="red", fontsize=48)
        elif left_score<right_score:
            screen.draw.text('Right Player Wins!', (210, 300),color="red", fontsize=48)
        screen.draw.text('Click enter to restart', (235, 340),color="red", fontsize=32)
    elif game_status=="PauseP" or game_status=='PauseB':
        screen.draw.text("PAUSE",(240,305),color="red",owidth=1.5, ocolor='black',fontsize=80)

def update():
    global game_status, current_angle, ball_speed, boxes_hit, score,do_get_initials, what_to_adjust,char, left_score, right_score
    if game_status == 'B0': ##game off, before started once
        if keyboard.RETURN:
            reset_breakout()
    elif game_status=='B1': ##game on
        breakout_player_movement()
        breakout_ball_movement()
        breakout_check_win()
        breakout_check_lost()
        breakout_change_ball_speed(boxes_hit)
        if keyboard.p:
            game_status="PauseB"
    elif game_status == 'B2' or game_status=='B4': ##game off, after loss
        if keyboard.RETURN:
            game_status = 'B3' #shows high scores
            create_high_score(score)
            if [score,'NEW'] in high_scores:
                what_to_adjust=high_scores.index([score,'NEW'])
                char=0
                do_get_initials=1   
            else:
                do_get_initials=0
    elif game_status=='B3': ##show high score page
        if do_get_initials==1:
            get_initials(score)
        time.sleep(.1)
        if keyboard.RETURN and keyboard.rshift:
            reset_breakout()
    elif game_status=="PauseB": #pause
        if keyboard.o:
            game_status="B1"
    elif game_status=='P0': #pong home
        if keyboard.RETURN:            
            left_score,right_score=0,0
            reset_pong()
    elif game_status=='P1': #pong playing
        pong_player_movement()
        pong_ball_movement()
        pong_collision()
        pong_check_game_over()
        if keyboard.p:
            game_status="PauseP"
    elif game_status=='P2': #pong gameover
        if keyboard.RETURN:
            left_score,right_score=0,0
            reset_pong()
    elif game_status=="PauseP": #pause
        if keyboard.o:
            game_status="P1"
    if keyboard.ESCAPE:
        game_status=0
    if keyboard.q:
        exit()
    
  
pgzrun.go()


