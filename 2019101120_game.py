import pygame
from config import *

pygame.init()
#Initialize the screen size and caption
display = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('River-Crossing Game')
#Stopping Condition set to False so game can continue
stop = False
#Clock to synchronize working of the different elements of the game
c = pygame.time.Clock()

#Start game in round 1, with player 1
player = 1
rounds = 1
#Create a list to store the scores in each round
scores = [0]
#Initialize the start time of each round
ticks = pygame.time.get_ticks()
#Create Player, Moving Obstacle, and Fixed Obstacle classes to detect collisions
#Give all of them parameters of image and position to place them in display
class Player (pygame.sprite.Sprite):
	def __init__(self, pos, *group):
		super().__init__(*group)
		self.image = pygame.image.load('rabbit.png')
		self.rect = self.image.get_rect(center = pos)
#Rabbit is the player 1

class Mobstacle (pygame.sprite.Sprite):
	def __init__(self, pos, *group):
		super().__init__(*group)
		self.image = pygame.image.load('animal.png')
		self.rect = self.image.get_rect(center = pos)
#Crocodile is the moving obstacle

class Fobstacle (pygame.sprite.Sprite):
	def __init__(self, pos, *group):
		super().__init__(*group)
		self.image = pygame.image.load('wall.png')
		self.rect = self.image.get_rect(center = pos)
#Brick wall is the fixed obstacle

#Set initial x, y, speed for player 1 in round 1
x = 500
y = 968
speed = 1

#Create group called all sprites to make updating positions easier
#Creating one group allows us to mainpulate every sprite at once including players and obstacles
all_sprites = pygame.sprite.Group()
#Maintain an xlist to store x coordinates of moving obstacles
xlist = [32, 500, 300, 700, 300, 400]
#Maintain a ylist to store coordinates of moving obstacles
#These lists will help with moving the obstacles and points calculation
ylist = [96, 186, 386, 720, 880, 588]
#Maintain a list of y coordinates of fixed obstacles for points calculation
y2list = [32, 32, 282, 482, 482, 652, 812, 968, 968]
#Create groups for fixed and moving obstacles to add to all_sprites
#Creating different groups allows us to manipulate fixed and moving obstacles differenetly
fobs = pygame.sprite.Group(Fobstacle((300, 32)), Fobstacle((750, 32)), Fobstacle((500, 282)), Fobstacle((850, 482)), Fobstacle((420, 482)), Fobstacle((200, 652)), Fobstacle((700, 812)), Fobstacle((300, 968)), Fobstacle((650, 968)))
mobs = pygame.sprite.Group() 

mlist = []
for i in range(6):
	mlist.append(Mobstacle((xlist[i], ylist[i]), mobs))
#In lines 60-64 we add instances of fixed and moving obstacles to the groups of fobs and mobs, which belong to all_sprites
all_sprites.add(fobs)
all_sprites.add(mobs)


#Instantiate the Player 1 variable with position and the group it belongs to which is all_sprites
player1 = Player((x, y), all_sprites)


#Create a timer function in order to monitor the time that has passed
#This is done by using the ticks variable that stores the time at the start and subtracting it from the current time
#Display the difference as the total time elapsed
#Return the time in order to calculate the final score
def timer() :
	global ticks
	seconds = (pygame.time.get_ticks() - ticks)//1000
	text = smallFont.render("Time: " + str(seconds), True, black)
	display.blit(text, (900, 980))
	return seconds
	


#Whenever a round is finished, either by victory or defeat, update the screen with the environment for the next round
#Most things remain constant except for the speeds and the poistions of the players
def refresh (s, player, rounds) :
	#declare global variables to ensure changes are implemented outside of the function in the main game
	global x, y, speed, all_sprites, x_list, y_list, fobs, mobs, mlist, player1, display, ticks
	ticks = pygame.time.get_ticks()
	display.fill(blue)
	#Update player position depending on the player who is playing
	x = 500
	if (player == 1):
		y = 968
	else :
		y = 32
	#Adjust the speeds according to the round
	#For level 1, the speed of moving obstacles is 2
	if rounds <= 2:
		speed = 2
	#For level 2, the speed of moving obstacles is 5
	elif rounds <= 4:
		speed = 5
	#For level 3 the speed of moving obstacles in 10
	else :
		speed = 10

	all_sprites = pygame.sprite.Group()
	xlist = [32, 500, 300, 700, 300, 400, 968]
	ylist = [96, 186, 386, 720, 880, 588, 650]
	y2list = [32, 32, 282, 482, 482, 652, 812, 968]

	fobs = pygame.sprite.Group(Fobstacle((300, 32)), Fobstacle((750, 32)), Fobstacle((500, 282)), Fobstacle((850, 482)), Fobstacle((420, 482)), Fobstacle((200, 652)), Fobstacle((700, 812)), Fobstacle((300, 968)), Fobstacle((650, 968)))
	mobs = pygame.sprite.Group() 

	mlist = []
	for i in range(6):
		mlist.append(Mobstacle((xlist[i], ylist[i]), mobs))
		all_sprites.add(fobs)
	all_sprites.add(mobs)

	player1 = Player((x, y), all_sprites)

	player1.rect.center = (x, y)
	pygame.draw.rect(display, path, [0, 0, 1000, 64])
	pygame.draw.rect(display, path, [0, 250, 1000, 64])
	pygame.draw.rect(display, path, [0, 450, 1000, 64])
	pygame.draw.rect(display, path, [0, 620, 1000, 64])
	pygame.draw.rect(display, path, [0, 780, 1000, 64])
	pygame.draw.rect(display, path, [0, 936, 1000, 64])
	all_sprites.update()
	all_sprites.draw(display)
	pygame.display.update()



#Create a Scoreboard function to monitor and update the score when it is called. The details for this are in lijne 214-236
def scoreboard (score) :
	ts = smallFont.render('Score: ' + str(score), False, black)
	display.blit(ts, (900, 20))


#When the game has ended, display the final scores for both players and the winner
def show():
	ts = smallFont.render('Player 1 scored ' + str(scores[1]) + ", " + str(scores[3]) + ", " + str(scores[5]), False, black)
	ts2 = smallFont.render('Player 2 scored ' + str(scores[2]) + ", " + str(scores[4]) + ", " + str(scores[6]), False, black)
	p1 = scores[1] + scores[3] + scores[5]
	p2 = scores[2] + scores[4] + scores[6]
	if (p1 > p2):
		ts3 = smallFont.render('Player 1 wins!', False, black)
	elif (p2 > p1):
		ts3 = smallFont.render('Player 2 wins!', False, black)
	else :
		ts3 = smallFont.render("It's a draw!", False, black)
	display.fill(white)
	display.blit(ts, (350, 100))
	display.blit(ts2, (350, 200))
	display.blit(ts3, (400, 500))
	pygame.display.update()


#This is the main loop for the game which continues until the stop variable is set to False
while not stop:
	#Check if the window is being closed to quit the game
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			stop = True
			pygame.quit()
			quit()

		#Check if there are keys being pressed to track movement using arrows and W, A, S, D. When those keys are presed, move in the respective direction by 20 units
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_LEFT or e.key == pygame.K_a:
				if x <= 32:
					x = x + 0
				else:
					x = x - 20
			if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
				if x >= 968:
					x = x + 0
				else:
					x = x + 20
			if e.key == pygame.K_UP or e.key == pygame.K_w:
				if y <= 32:
					y = y + 0
				else:
					y = y - 20
			if e.key == pygame.K_DOWN or e.key == pygame.K_s:
				if y >= 968:
					y = y + 0
				else:
					y = y + 20
	#Create blue background for river
	display.fill((100, 150, 255))
	#For moving obstacles, check if they are exiting the screen, and bring them back to starting position so they appear continuously
	for i in range(6):
		if xlist[i] >= 1000:
			xlist[i] = 0
		else:
			#Manipulate the speed using the speed variable that changes in successive rounds
			xlist[i] = xlist[i] + speed

		#Add the changed positions of the moving obstacles to make it look like they are moving
		mlist[i].rect.center = (xlist[i], ylist[i])
	#Add the updated position of player 1
	player1.rect.center = (x, y)

	#Create the safety bridges and add their colors and positions
	pygame.draw.rect(display, path, [0, 0, 1000, 64])
	pygame.draw.rect(display, path, [0, 250, 1000, 64])
	pygame.draw.rect(display, path, [0, 450, 1000, 64])
	pygame.draw.rect(display, path, [0, 620, 1000, 64])
	pygame.draw.rect(display, path, [0, 780, 1000, 64])
	pygame.draw.rect(display, path, [0, 936, 1000, 64])
	#Many of the sprites have new positions, update and draw in order to view these changes
	all_sprites.update()
	all_sprites.draw(display)
	#Set score = 0 at the beginning of each round
	score = 0
	#Measure points for player 1 by comparing y coordinates of the sprite and the coordinates of the obstacles so points can be awarded
	if player == 1:
		temp = y + 64
		for i in ylist:
			if temp <= i:
				score = score + 10
		for i in y2list:
			if temp <= i:
				score = score + 5
	#Measure points for Player 2 similarly but in opposite direction to update score
	else : 
		temp = y
		for i in ylist :
			if temp >= i + 64:
				score = score + 10
		for i in y2list:
			if temp >= i + 64:
				score = score + 5

	#Call scoreboard function to display the updated score
	scoreboard(score)
	#sec variable stores the time that has elapsed which is useful in score calculation later in the winner and loser functions
	sec = timer()

	#Set the start and end for Player 1 and Player 2 on opposite ends to show the user how to navigate the game
	if player == 1:
		tstart = smallFont.render('Start', False, black)
		display.blit(tstart, (5, 964))
		tend = smallFont.render('End', False, black)
		display.blit(tend, (5, 20))
	else :
		tstart = smallFont.render('Start', False, black)
		display.blit(tstart, (5, 20))
		tend = smallFont.render('End', False, black)
		display.blit(tend, (5, 964))
	#c1 is the set of collisions with fixed obstacles and c2 is the same for moving obstacles
	c1 = pygame.sprite.spritecollide(player1, fobs, False)
	c2 = pygame.sprite.spritecollide(player1, mobs, False)
	#Check for collisions with fixed and moving obstacles. If detected, call the loser function from config.py file
	for enemy in c1:
		pygame.time.delay(2000)
		scores.append(score)
		#This function displays the fact that you lost
		loser()
		pygame.time.delay(2000)
		#Player is 1 if player 1 is playing and 0 if player 2. This makes it easy to keep track for current player
		player = (player + 1)%2
		#Increment round to keep track of what round is going on irrespective of the player currently playing
		rounds = rounds + 1
		#If there are more than 6 rounds (3 levels each) stop game and display the final scores
		if rounds > 6:
			show()
			pygame.time.delay(5000)
			#Quit after displaying score for 5 seconds
			pygame.quit()
			quit()
		else:
			#If there are more rounds remaining, refresh the game for the next player with the required speeds
			refresh(speed, player, rounds)

	#Similar to fixed obstacles, check for collisions with moving obstacles and perform the same
	for enemy in c2:
		pygame.time.delay(2000)
		scores.append(score)
		loser()
		pygame.time.delay(2000)
		player = (player + 1)%2
		rounds = rounds + 1
		if (rounds > 6):
			show()
			pygame.time.delay(5000)
			pygame.quit()
			quit()
		else:
			refresh(speed, player, rounds)

	#Check if the player has reached the other side. If they cross the threshold, they have won.
	#Call winner function from config.py to display the score for that round
	if player == 1:
		if y <= 32 :
			pygame.time.delay(2000)
			
			if sec <= 8:
				score = score + 50
			elif sec <= 12:
				score = score + 25
			elif sec <= 20:
				score = score - 25
			else:
				score = score - 50
			scores.append(score)
			winner(score, sec)
			pygame.time.delay(2000)
			player = (player + 1)%2
			rounds = rounds + 1
			if rounds > 6:
				show()
				pygame.time.delay(5000)	
				pygame.quit()
				quit()
			else :
				refresh(speed, player, rounds)

	#Similarly check if Player 2 has won
	else :
		if y >= 968:	
			display.fill((100, 150, 255))
			pygame.time.delay(2000)
			if sec <= 8:
				score = score + 50
			elif sec <= 12:
				score = score + 25
			elif sec <= 20:
				score = score - 25
			else:
				score = score - 50
			scores.append(score)
			winner(score, sec)
			pygame.time.delay(2000)
			player = (player + 1)%2
			rounds = rounds + 1
			if rounds > 6:
				show()
				pygame.time.delay(5000)
				pygame.quit()
				quit()
			else :
				refresh(speed, player, rounds)
	#Update the screen with all the changes made so the user can see
	pygame.display.update()
	#Let the clock progress to carry out the next cycle at 60 FPS
	c.tick(60)

#Quit the game at the end
pygame.quit()
quit()