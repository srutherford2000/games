1. Files: 
- multigame.py 
	main program that runs the games, will be discussed further in this documentation.
- README.txt
	text file you are currently reading that describes multigame python file.
2. Overview:
- Our game prompts the user to choose between the two Atari games: Breakout and Pong.
Breakout is a single player game with the aim being to score the highest point on the scoreboard
by breaking 'bricks'. You die by letting the ball past the user paddle and having the ball hit 
the bottom of the screen. Pong is a two plater game where whichever players scores 11 points wins
the game. Both games can be paused if one player was to want a break, and breakout takes high 
scores in order to keep things competitive. 
3. Commands:
- From the homepage, click the side of the screen for the user's choice of game.
- Hit "q" to exit/turnoff the game at anytime.
- Hit "esc" to return to the homepage at anytime.
- Hit "enter" to begin both Pong and Breakout once a game is selected (should prompt you on the screen).
- When in Pong and Breakout, press "p" to pause the game and "o" to resume after a pause.
- Pong will automatically restart after every round(once someone gets a point)
- When in Breakout, after the game completes, use Arrow Keys to input initials on the scoreboard.
	(left/right change position in the initials, up/down change letter)
	click "shift" and "enter" simaltaneously to start a new game of breakout after entering 
	the high score
4. Code Packages:
- imported pgzrun, math, random, and time
pgzrun is the only one a user would need to install prior to running this assuming they have 
python installed already. (math, random and time are all preinstalled with python)
5. Inputs:
- Takes keys pressed and mouse clicks as inputs(how these keys works are previously 
	discused in section 3).
6.Output Files:
- No output files are created by this program.

