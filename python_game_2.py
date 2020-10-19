import pygame
from pygame.draw import *
from random import randint
import numpy as np
pygame.init()

FPS = 100
screen = pygame.display.set_mode((1200, 900))

'''Цвета шариков'''
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


'''шарики'''
num = randint(2, 8)
x = np.random.randint(100, 1100, num).reshape((num, 1))
y = np.random.randint(100, 900, num).reshape((num, 1))
xspeed = np.random.randint(-10, 10, num).reshape((num, 1))
yspeed = np.random.randint(-10, 10, num).reshape((num, 1))
r = np.random.randint(50, 100, num).reshape((num, 1))
color = np.random.randint(0, 5, num).reshape((num, 1))
BALLS = np.concatenate((x, y, xspeed, yspeed, r, color), axis = 1)


screencolor = COLORS[randint(0, 5)]
global time, name, points
time = 0.0
name = input('Print your name:')
points = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False

def draw_ball(x, y, r, color):
    ball = circle(screen, color, (x, y), r)
    
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Набрано очков:", (points))
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (num):
                if (BALLS[i, 0] - BALLS[i, 4], BALLS[i, 1] - BALLS[i, 4]) < event.pos < (BALLS[i, 0] + BALLS[i, 4], BALLS[i, 1] + BALLS[i, 4]):
                    points += 1
                    screencolor = COLORS[BALLS[i, 5]]
                    screen.fill(screencolor)

    time += 1 / FPS
    if time >= 30:
        print('You collect ', (points), ' points.')
        finished = True
                
    for i in range(num):         
        if 0 < BALLS[i, 0] < 1200 and 0 < BALLS[i, 1] < 900:
            BALLS[i, 0] += BALLS[i, 2]
            BALLS[i, 1] += BALLS[i, 3]
            draw_ball(BALLS[i, 0], BALLS[i,1], BALLS[i, 4], COLORS[BALLS[i, 5]])
        elif BALLS[i, 1] <= 0:
            BALLS[i, 3] = randint(0, 20)
            BALLS[i, 1] += BALLS[i, 3]
            draw_ball(BALLS[i, 0], BALLS[i,1], BALLS[i, 4], COLORS[BALLS[i, 5]])
        elif BALLS[i, 1] >= 900:
            BALLS[i, 3] = randint(-20, 0)
            BALLS[i, 1] += BALLS[i, 3]
            draw_ball(BALLS[i, 0], BALLS[i,1], BALLS[i, 4], COLORS[BALLS[i, 5]])
        elif BALLS[i, 0] <= 0:
            BALLS[i, 2] = randint(0, 20)
            BALLS[i, 0] += BALLS[i, 2]
            draw_ball(BALLS[i, 0], BALLS[i,1], BALLS[i, 4], COLORS[BALLS[i, 5]])
        elif BALLS[i, 0] >= 1200:
            BALLS[i, 2] = randint(-20, 0)
            BALLS[i, 0] += BALLS[i, 2]
            draw_ball(BALLS[i, 0], BALLS[i,1], BALLS[i, 4], COLORS[BALLS[i, 5]])
                    
    pygame.display.update()
    screen.fill(screencolor)

file = open('results.txt', 'a')
file.write(name + ' ' + str(points) + '\n')
file.close()

pygame.quit()
