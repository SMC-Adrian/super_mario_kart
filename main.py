import pygame 
import sys
import banen

# initialiseer pygame
pygame.init()

# maak scherm en geef titel
SCREENWIDTH, SCREENHEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Super Mario Kart - PO Informatica")

# maak variabelen voor kleuren
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 175, 0)

# laad afbeeldingen
loadingscreen = pygame.image.load(r"img/loadingscreen_16_9.jpg")


# beginscherm loop
beginscherm = True
while beginscherm:
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
    for event in pygame.event.get():
        # sluit de game af als er op het kruisje wordt geklikt
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # achtergrond is groen
    screen.fill(GREEN)
    banen.baan()
    pygame.display.update()

pygame.quit()
sys.exit()