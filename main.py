import pygame as pg
import sys

# initialiseer pygame
pg.init()

# maak scherm en geef titel
SCREENWIDTH, SCREENHEIGHT = 1920, 1080
screen = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pg.display.set_caption("Super Mario Kart - PO Informatica")

# maak variabelen voor kleuren
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 175, 0)

# laad afbeeldingen
mario = pg.image.load(r"img/loadingscreen.webp.png")


# beginscherm loop
beginscherm = True
while beginscherm:
    pass