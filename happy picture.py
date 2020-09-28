import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 800)) #picture size

#background
rect(screen, (120, 190, 255), (0, 0, 1000, 800))
rect(screen, (100, 145, 95), (0, 500, 1000, 300))


#boy
line(screen, (0, 0, 0), (295, 288), (130, 480), 2) #left hand
line(screen, (0, 0, 0), (305, 565), (270, 775), 2) #left leg
line(screen, (0, 0, 0), (270, 775), (225, 785), 2) #left foot

line(screen, (0, 0, 0), (405, 288), (510, 520), 2) #right hand
line(screen, (0, 0, 0), (395, 565), (415, 775), 2) #right leg
line(screen, (0, 0, 0), (415, 775), (460, 775), 2) #right foot

ellipse(screen, (180, 60, 110), (250, 260, 200, 325))
circle(screen, (255, 255, 190), (350, 190), 80) 


#ice cream
ellipse(screen, (235, 185, 185), (100, 390, 50, 40)) #strawberry ice cream
ellipse(screen, (55, 10, 10), (80, 410, 50, 40)) #chocolate ice cream
ellipse(screen, (250, 250, 225), (83, 380, 50, 40)) #vanilla ice cream
polygon(screen, (250, 220, 110), [(165, 515), (85, 450), (155, 410)]) #ice cream cone 

    
#girl
line(screen, (0, 0, 0), (610, 335), (510, 520), 2) #left hand
line(screen, (0, 0, 0), (613, 582), (605, 775), 2) #left leg
line(screen, (0, 0, 0), (605, 775), (580, 775), 2) #left foot

line(screen, (0, 0, 0), (630, 330), (745, 450), 2) #right shoulder
line(screen, (0, 0, 0), (745, 450), (775, 370), 2) #right hand
line(screen, (0, 0, 0), (647, 582), (647, 775), 2) #right leg
line(screen, (0, 0, 0), (647, 775), (672, 775), 2) #right foot

polygon(screen, (250, 110, 110), [(530, 585), (760, 580), (620, 275)])
circle(screen, (255, 255, 190), (620, 230), 70)


#baloon
line(screen, (0, 0, 0), (775, 370), (830, 420)) #rope
line(screen, (0, 0, 0), (775, 370), (860, 165)) 
polygon(screen, (220, 40, 40), [(860, 165), (830, 90), (925, 120)]) #baloon   
circle(screen, (220, 40, 40), (860, 88), 30)
circle(screen, (220, 40, 40), (902, 102), 30)
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
