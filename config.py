import pygame
pygame.init()

#COLORS
white = (255, 255, 255) #for background
black = (0, 0, 0)		#for text
green = (0, 128, 0)		#for text
blue = (100, 150, 255)	#for river background
path = (180, 80, 80)    #for bridges
#FONTS
bigFont = pygame.font.SysFont("comicsansms", 72) 
medFont = pygame.font.SysFont("comicsansms", 36)
smallFont = pygame.font.SysFont("comicsansms", 32)


#winner function to display score of the winner with the time bonus/penalty
def winner (score, sec) :
	if (sec <= 8):
		text = medFont.render("You Win! Your Score Was " + str(score - 50) + " and a 50 point time bonus! Your total score is " + str(score) + "!", True, green)	
	elif (sec <= 12):
		text = medFont.render("You Win! Your Score Was " + str(score - 25) + " and a 25 point time bonus! Your total score is " + str(score) + "!", True, green)	
	elif (sec <= 20):
		text = medFont.render("You Win! Your Score Was " + str(score + 25) + " and a 25 point time penalty! Your total score is " + str(score) + "!", True, green)
	else:
		text = medFont.render("You Win! Your Score Was " + str(score + 50) + " and a 50 point time penalty! Your total score is " + str(score) + "!", True, green)	
	
	display = pygame.display.set_mode((1000, 1000))
	display.fill(white)		
	display.blit(text, (50, 500))
	pygame.display.update()

def loser () : 
	text = bigFont.render("You Lose", True, green)
	display = pygame.display.set_mode((1000, 1000))
	display.fill((255, 255, 255))
	display.blit(text, (400, 500))
	pygame.display.update()