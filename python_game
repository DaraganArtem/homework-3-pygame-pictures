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

'''Делаем массив координат шариков
num = randint(1, 8)
x = np.random.randint(100, 1100, num).reshape((num, 1))
y = np.random.randint(100, 900, num).reshape((num, 1))
BALLS = np.concatenate((x, y), axis = 1)
'''

global x, y, r
x = randint(100, 1100)
y = randint(100, 900)
r = randint(10, 100)
color = COLORS[randint(0, 5)]
xspeed = randint(-10, 10)
yspeed = randint(-10, 10)

def draw_ball():
    ball = circle(screen, color, (x, y), r)

points = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Набрано очков:", (points))
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos < (x + r, y + r) and event.pos > (x - r, y - r):
                print("+")
                points += 1
            else:
                print("miss")
                
            
    if 0 < x < 1200 and 0 < y < 900:
        x += xspeed
        y += yspeed
        draw_ball()
    elif y <= 0:
        yspeed = randint(0, 20)
        x += xspeed
        y += yspeed
        draw_ball()
    elif y >= 900:
        yspeed = randint(-20, 0)
        x += xspeed
        y += yspeed
        draw_ball()
    elif x <= 0:
        xspeed = randint(0, 20)
        x += xspeed
        y += yspeed
        draw_ball()
    elif x >= 1200:
        xspeed = randint(-20, 0)
        x += xspeed
        y += yspeed
        draw_ball()
    
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

