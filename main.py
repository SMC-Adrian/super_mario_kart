import pygame as pg
import sys
import banen

# initialiseer pygame
pg.init()

# maak scherm en geef titel
SCREENWIDTH, SCREENHEIGHT = 1280, 720
screen = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pg.display.set_caption("Super Mario Kart - PO Informatica")

# maak variabelen voor kleuren
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 175, 0)

# laad afbeeldingen
loadingscreen = pg.image.load(r"img/loadingscreen_16_9.jpg")


# beginscherm loop
beginscherm = True
while beginscherm:
    for event in pg.event.get():
        # sluit de game af als er op het kruisje wordt geklikt
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # gaat naar volgende loop als er geklikt wordt
        if event.type == pg.MOUSEBUTTONDOWN:
            beginscherm = False
            break
    # plaats achtergrondafbeelding in scherm
    screen.blit(loadingscreen, (0, 0))
    
    # update het scherm
    pg.display.update()

while True:
    for event in pg.event.get():
        # sluit de game af als er op het kruisje wordt geklikt
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    # achtergrond is groen
    screen.fill(GREEN)
    banen.baan()
    pg.display.update()

pg.quit()
sys.exit()