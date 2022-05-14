import pygame
import random
import time
import os
import math
pygame.init()
pygame.mixer.init()
win=pygame.display.set_mode((1020,700))
pygame.display.set_caption('naag ka khel')
#fps
fps=30
clock=pygame.time.Clock()
#font on screen
font=pygame.font.SysFont(None,50)
def screen_text(text,color,x ,y):
	screen_text=font.render(text,True,color)
	win.blit(screen_text,(x,y))

#length increment
def plot_snake(win,color,snk_list,size):
	for x,y in snk_list:
		pygame.draw.rect(win,color,(x,y,size,size))
#background
b_image=pygame.image.load('E:/snake/Back.png')
b_image=pygame.transform.scale(b_image,(1020,700))

b_y=0
b_x=0
def background(x,y):
	win.blit(b_image,(x,y))
#main screen image
a_image=pygame.image.load('E:/snake/anaconda.png')
a_x =220
a_y=-140
def ana(x,y):
	win.blit(a_image,(x,y))
def p():
	game_over1=False
	while not game_over1:
		screen_text('PAUSED',(0,0,255),400,100)
		screen_text('C to continue',(0,255,0),400,200)
		screen_text('Or Q to quit',(255,0,0),400,250)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_c:
					game_over1=True
				if event.key==pygame.K_q:
					welcome()

		clock.tick(10)
		pygame.display.update()
def welcome():
	exit_game=False
	while not exit_game:
		background(b_x,b_y)
		ana(a_x,a_y)
		screen_text('Welcome to python in python',(0,0,0),200,180)
		screen_text('Press SPACE to play',(255,0,0),200,400)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_SPACE:
					game_loop()
		clock.tick(fps)
		pygame.display.update()
#gameloop
def game_loop():
	#game specific variable
	exit_game=False
	game_over1=False
	game_over_2=False
	x=55
	y=75
	velocity_x=0
	velocity_y=0
	#food
	f_x=random.randint(50,1020)
	f_y=random.randint(50,700)
	#snakesize
	size=20
	black=(0,0,0)
	score=0
	init_velocity=5
	snk_list=[]
	snk_length=1
	i=0
	brown=(210,105,30)
	pygame.mixer.music.load('E:/snake/bm1.mp3')
	pygame.mixer.music.play(-1)
	if(not os.path.exists('untitled.txt')):
		with open('E:/snake/untitled.txt','r') as f:
			hiscore=f.read()
	with open('E:/snake/untitled.txt','r') as f:
		hiscore=f.read()
	while not exit_game:
		#gameover
		if game_over1:
			with open('E:/snake/untitled.txt','w') as f:
				f.write(str(hiscore))
			win.fill((0,0,0))
			screen_text('Self collision!',(255,255,0),15,250)
			screen_text(' PRESS ENTER TO REPLAY : )',(0,255,0),15,300)
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					exit_game=True
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RETURN:
						game_loop()
		else:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
						exit_game=True
				#moving our snake
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
						velocity_x=init_velocity
						velocity_y=0
					if event.key==pygame.K_a or event.key==pygame.K_LEFT:
						velocity_x= -init_velocity
						velocity_y=0
					if event.key==pygame.K_w or event.key==pygame.K_UP :
						velocity_x=0
						velocity_y= -init_velocity
					if event.key==pygame.K_s or event.key==pygame.K_DOWN :
						velocity_x=0
						velocity_y= init_velocity
					if event.key==pygame.K_p:
						p()
			#updating position of snake
			x=x + velocity_x
			y=y + velocity_y
			#eating food; below line commands that when the snake is in proximity of food increase the score by 1and change the location of food using random function
			if math.sqrt(math.pow(x-f_x,2)+math.pow(y-f_y,2)) <15:
				score=score +10
				f_x=random.randint(50,1020)
				f_y=random.randint(50,700)
				snk_length=snk_length+5
			# increasing score
			if score==100:
				init_velocity=8
			# equating scpre to hiscore when the score is past the previous Hiscore
			if score>int(hiscore):
				hiscore=score
			background(b_x,b_y)
				#calling screen_text function
			screen_text('Score :  '+ str(score)      + '     Hiscore :  '  +  str(hiscore),(255,0,200),25,25)
			#incraesing the length of snake
			head=[]
			head.append(x)
			head.append(y)
			snk_list.append(head)

			if len(snk_list) > snk_length:
				del snk_list[0]

			if head in snk_list[:-1]:
				pygame.mixer.music.load('E:/snake/Glass_Break.mp3')
				pygame.mixer.music.play()
				game_over1=True
			#teleporting the snke whenever the snake goes out of the frame
			if x<0:
				x=1040
			if x>1040:
				x=-10
			if y<-10:
				y=690
			if y>690:
				y=-10
			#food
			pygame.draw.circle(win,(255,0,0),(f_x,f_y),10)
			# plotting snake
			plot_snake(win,black,snk_list,size)
			#updating the screen
		pygame.display.update()
			#setting fps
		clock.tick(fps)
	pygame.quit()
	quit()

welcome()
