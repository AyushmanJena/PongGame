import pygame, sys, random, time

pygame.init()
clock = pygame.time.Clock()

opponent_score = 0
player_score = 0
font = pygame.font.SysFont('Calibri',40)

textX = 400 - 34
textY = 60

hit_sound = pygame.mixer.Sound('E:/Laptop/Ringtones/CoolGuy.MP3')
point_sound = pygame.mixer.Sound('E:/Ayush/Components/Flappy/audio/point.wav')

def show_score(x, y) :
	score = font.render(str(opponent_score) + " : " + str(player_score), True, (0, 200, 255))
	screen.blit(score, (x, y))


def ball_animation() :
	global ball_speed_x, ball_speed_y, opponent_score, player_score
	ball.x += ball_speed_x
	ball.y += ball_speed_y
	

	if ball.top <= 0 or ball.bottom >= screen_height :
		ball_speed_y *= -1

	if ball.left <= 0 :
		player_score +=1
		point_sound.play()
		ball_restart()

	if ball.right >= screen_width :
		opponent_score += 1
		point_sound.play()
		ball_restart()

	if ball.colliderect(player) or ball.colliderect(opponent):
		hit_sound.play()
		ball_speed_x *= -1

def player_animation() :
	player.y += player_speed

	if player.top <= 0 :
		player.top = 0
	if player.bottom >= screen_height :
		player.bottom = screen_height

def opponent_ai() :
	if opponent.top < ball.y :
		opponent.top += opponent_speed
	if opponent.bottom > ball.y :
		opponent.bottom -= opponent_speed

	if opponent.top <= 0 :
		opponent.top = 0
	if opponent.bottom >= screen_height :
		opponent.bottom = screen_height

def ball_restart() :
	global ball_speed_y, ball_speed_x
	ball.center = (screen_width/2, screen_height/2)
	ball_speed_y *= random.choice((1, -1))
	ball_speed_x *= random.choice((1, -1))


screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

#game rectangles
ball = pygame.Rect(screen_width/2 - 5, screen_height/2 - 15, 14, 14)
player = pygame.Rect(screen_width - 20, screen_height/2 - 40, 5, 80)
opponent = pygame.Rect(16, screen_height/2 - 40, 5, 150)

bg_color = (0, 0, 255)
light_grey = (255, 255, 255)

ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))
player_speed = 0
opponent_speed = 10

while True :
	for event in pygame.event.get() :
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN :
			if event.key == pygame.K_DOWN :
				player_speed += 5
			if event.key == pygame.K_UP :
				player_speed -= 5

		if event.type == pygame.KEYUP :
			if event.key == pygame.K_DOWN :
				player_speed -= 5
			if event.key == pygame.K_UP :
				player_speed += 5


			#visuals
		
		
	screen.fill(bg_color)
	pygame.draw.rect(screen, light_grey, player)
	pygame.draw.rect(screen, light_grey, opponent)
	pygame.draw.ellipse(screen, light_grey, ball)
	pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
	show_score(textX, textY)
	ball_animation()
	player_animation()
	opponent_ai()


	pygame.display.flip()
	clock.tick(50)
