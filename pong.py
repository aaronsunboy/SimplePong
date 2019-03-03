'''
Creator: Aaron Lin
Name: pong.py
Date Created: March 3, 2019
Description: Based on the game pong, this is a very similar game. Instead of two players,
this game is a single playered game. The ball starts bouncing around, and the player has
a paddle to prevent the ball from reaching the bottom of the screen. When the ball reaches
the bottom of the the screen, the player loses a life. The player has three lives in all.
When a player runs out of lives, it is game over. A player earns a point when the ball 
touches the top of the screen.
'''

import pygame, sys

# defining a class
class MyBallClass(pygame.sprite.Sprite):
	def __init__(self, image_file, speed, location): # initializing the ball
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file) # the sprite's image file
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location # sprite's location
		self.speed = speed # sprite's speed

	def move(self): # when the ball moves
		global score, score_surf, score_font
		self.rect = self.rect.move(self.speed) # change the ball's location
		if self.rect.left < 0 or self.rect.right > screen.get_width(): # when it bounces on the side wall
			self.speed[0] = -self.speed[0]
			hit.play() # playing the bounce sound
		if self.rect.top <= 0: # when it bounces on the top wall
			self.speed[1] = -self.speed[1]
			hit.play() # playing the bounce sound
			score += 1
			score_surf = score_font.render(str(score), 1, (0, 0, 0)) # display the score

class MyPaddleClass(pygame.sprite.Sprite): # the paddle class
	def __init__(self, location = [0, 0]): # initiate
		pygame.sprite.Sprite.__init__(self)
		image_surface = pygame.surface.Surface([100, 20]) # draw the paddle's outline
		image_surface.fill([0, 0, 0]) # fill the paddle
		self.image = image_surface.convert()
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location # the paddle's location

pygame.init() # initialize a game screen
pygame.mixer.init() # initialize music
screen_size = 640, 480
screen = pygame.display.set_mode(screen_size) # screen size
clock = pygame.time.Clock()
ball_speed = [1, 1] # ball speed
paddle_start = 270, 400
ball_start = 320, 50
hit = pygame.mixer.Sound('Bounce.WAV') # bounce sound
hit.set_volume(0.25) # set sound volume
myBall = MyBallClass('BlackBall.png', ball_speed, ball_start) # create myBall
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass(paddle_start) # create paddle
lives = 3 # lives
score = 0 # score
score_font = pygame.font.Font(None, 50) # score font
score_surf = score_font.render(str(score), 1, (0, 0, 0)) # display the score
score_pos = [10, 10] # where the score is
done = False # whether the game is over
running = True # whether the window is running

while running:
	screen.fill([255, 255, 255])

	# quit the game when closing the window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		# move the paddle when the mouse moves
		elif event.type == pygame.MOUSEMOTION:
			paddle.rect.centerx = event.pos[0]

	# when the ball hits the paddle
	if pygame.sprite.spritecollide(paddle, ballGroup, False):
		myBall.speed[1] = -myBall.speed[1]
		hit.play()
	myBall.move()
	if not done:
		# draw paddle and ball
		screen.blit(myBall.image, myBall.rect)
		screen.blit(paddle.image, paddle.rect)
		screen.blit(score_surf, score_pos)
		# show how many lives left
		for i in range(lives):
			width = screen.get_width()
			screen.blit(myBall.image, [width- 40 * i, 20])
		pygame.display.flip()
	# player loses life
	if myBall.rect.top >= screen.get_rect().bottom:
		lives += -1
		if lives == 0: # player runs out of lives
			final_text1 = 'Game Over'
			final_text2 = 'Your final score is: ' + str(score)
			ft1_font = pygame.font.Font(None, 70)
			ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0))
			ft2_font = pygame.font.Font(None, 50)
			ft2_surf = ft2_font.render(final_text2, 1, (0, 0, 0))
			screen.blit(ft1_surf, [screen.get_width()/2 - ft1_surf.get_width()/2, 100]) # dipslay game over
			screen.blit(ft2_surf, [screen.get_width()/2 - ft2_surf.get_width()/2, 200]) # display score
			pygame.display.flip()
			done = True
		else:
			pygame.time.delay(2000) # wait two seconds after the player loses life
			myBall.rect.topleft = [50, 50] # replace the ball

pygame.quit()