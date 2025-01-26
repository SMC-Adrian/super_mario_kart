import pygame 
import sys
from includes.banen import *

# initialiseer pygame
pygame.init()

# maak scherm en geef titel
SCREENWIDTH, SCREENHEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Super Mario Kart - PO Informatica")

# maak variabelen voor kleuren
WIT = (255, 255, 255)
ZWART = (0, 0, 0)
GROEN = (0, 175, 0)
GRIJS = (79, 79, 79)
LICHTBLAUW = (108, 217, 213)
DONKERBLAUW = (21, 27, 56)

FPS = 30

# laad afbeeldingen
loadingscreen = pygame.image.load(r"img/loadingscreen_16_9.jpg") # deze afbeelding is door chatgpt gegenereed met de prompts: generate a image for the front of a small 2d racing game without any text using pixelart - Verbeeld an image in this style with 1280 by 720 pixels - only make a loadingscreen without side bars
car1 = pygame.image.load(r"img/car1.webp")

# classes
class auto:
    def __init__(self, x: int=0, y: int=0, grootte: int=10):
        self.x: int = x
        self.y: int = y
        # pygame.draw.rect(screen, DONKERBLAUW, (x, y, grootte, grootte))
    
    def get_center():
        pass

    def horizontaal(self, snelheid):
        '''
        verplaats de auto horizontaal met het aantal pixels van snelheid
        '''
        self.x = self.x + snelheid
    
    def verticaal(self, snelheid):
        '''
        verplaats de auto verticaal met het aantal pixels van snelheid
        '''
        self.y = self.y + snelheid
        
# functies
def checkpoints_baan1():
    pygame.draw.rect(screen, WIT, (500, 50, 10, 130))

# beginscherm loop
beginscherm = True
clock = pygame.time.Clock()
while beginscherm:
    # set ticks
    for event in pygame.event.get():
        # sluit de game af als er op het kruisje wordt geklikt
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # gaat naar volgende loop als er geklikt wordt
        if event.type == pygame.MOUSEBUTTONDOWN:
            beginscherm = False
            break
    # plaats achtergrondafbeelding in scherm
    screen.blit(loadingscreen, (0, 0))
    
    # update het scherm
    pygame.display.update()

while True:
    # zorgt dat de game niet sneller dan 30 keer per seconden loopt
    clock.tick(FPS)
    # achtergrond is groen
    screen.fill(GROEN)
    # teken de baan uit banen.py
    baan1()
    checkpoints_baan1()
    pygame.draw.rect(screen, DONKERBLAUW, (10, 100, 40, 40))
    # screen.blit(car1, (100, 100))   





    pygame.display.update()

    for event in pygame.event.get():
        # sluit de game af als er op het kruisje wordt geklikt
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
pygame.quit()
sys.exit()