#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 12:39:16 2020

@author: student

"""

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1200)) #размер картинки

#Рисуем фон
rect(screen, (180, 200, 255), (0, 0, 800, 1200))
rect(screen, (255, 255, 255), (0, 650, 800, 550))
rect(screen, (0, 0, 0), (0, 650, 800, 550), 2)
 
#Функции рисования медведя:
def draw_bear(surface, x, y, width, height, color):
    '''
    Функция рисует медведя на экране.
    surface - объект pygame.Surface
    x, y - координаты левого верхнего угла изображения
    width, weight - высота и ширина изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    draw_head(surface, x, y, width, height, color)
    draw_body(surface, x, y, width, height, color)
    draw_hand(surface, x, y, width, height, color)
    draw_leg(surface, x, y, width, height, color)

def draw_head(surface, x, y, width, height, color):
    '''
    Функция рисует голову медведя.
    x, y - координаты центра левого верхнего угла прямоугольника,
    в который вписан эллипс.
    Остальные параметры те же, что и в функции draw_bear.
    '''
    ellipse(surface, color, (x + width // 3,
                             y,
                             width // 2,
                             height * 2 // 10))
    #рисуем контур головы  
    ellipse(surface, (0, 0, 0), (x + width // 3,
                                 y,
                                 width // 2,
                                 height * 2 // 10), 2)
      
def draw_body(surface, x, y, width, height, color):
    '''
    Функция рисует тело медведя.
    x, y - координаты центра левого верхнего угла прямоугольника,
    в который вписан эллипс.
    Параметры те же, что и в функции draw_bear
    Странные числа 10, 3, 5... это пропорции элементов изображения
    относительно прямоугольника, в который оно вписано
    '''
    ellipse(surface, color, (x,
                             y + height // 10,
                             width * 3 // 5,
                             height * 9 // 10))
    #рисуем контур тела 
    ellipse(surface, (0, 0, 0), (x,
                                 y + height // 10,
                                 width * 3 // 5,
                                 height * 9 // 10), 2)

def draw_hand(surface, x, y, width, height, color):
    '''
    Функция рисует лапу медведя.
    x, y - координаты центра левого верхнего угла прямоугольника,
    в который вписан эллипс.
    Параметры те же, что и в функции draw_bear
    '''
    ellipse(surface, color, (x + width // 2,
                             y + height * 4 // 10,
                             width // 3,
                             height // 10))
    #рисуем контур лапы
    ellipse(surface, (0, 0, 0), (x + width // 2,
                                 y + height * 4 // 10,
                                 width // 3,
                                 height // 10), 2)

def draw_leg(surface, x, y, width, height, color):
    '''
    Функция рисует лапу медведя.
    Изобржение состоит из двух эллипсов:
    один - бедро, другой - стопа.
    Остальные параметры те же, что и в функции draw_bear.
    '''
    #рисуем бедро
    ellipse(surface, color, (x + width // 4,
                             y + height * 7 // 10,
                             width * 5 // 10,
                             height * 3 // 10))
    #рисуем контур бедра
    ellipse(surface, (0, 0, 0), (x + width // 4,
                                 y + height * 7 // 10,
                                 width * 5// 10,
                                 height * 3 // 10), 2)
    #рисуем стопу
    ellipse(surface, color, (x + width * 3 // 5,
                             y + height * 18 // 20,
                             width // 3,
                             height // 10))
    #рисуем контур стопы
    ellipse(surface, (0, 0, 0), (x + width * 3 // 5,
                                 y + height * 18 // 20,
                                 width // 3,
                                 height // 10), 2)

    
#Рисуем медведей   
num = 1
for i in range (num):

    #Ввод параметров изображения
    surface = screen #рисунок будет на поверхности screen
    color = (255, 255, 255) #медведь - белый
    width = 370
    height = 500
    x = 10
    y = 300
    draw_bear(surface, x, y, width, height, color)

    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()