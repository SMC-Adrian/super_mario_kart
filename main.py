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
GEEL = (255, 153, 51)
ROOD = (255, 0, 0)
LETTERS = pygame.font.SysFont("arial", 30, bold=True, italic=False)

# laad afbeeldingen
loadingscreen = pygame.image.load(r"img/loadingscreen_16_9.jpg")

# plaats achtergrondafbeelding in scherm
screen.blit(loadingscreen, (0, 0))

# beginscherm loop

image_1 = pygame.image.load("C:\\Users\\SMC\\super_mario_kart\\grasland.jpeg").convert()
image_2 = pygame.image.load("C:\\Users\\SMC\\super_mario_kart\\desert.jpeg").convert()
image_3 = pygame.image.load("C:\\Users\\SMC\\super_mario_kart\\arctic.jpeg").convert()
image_4 = pygame.image.load("C:\\Users\\SMC\\super_mario_kart\\city.jpeg").convert()
image_5 = pygame.image.load("C:\\Users\\SMC\\super_mario_kart\\settings.jpeg").convert()
text_1 = LETTERS.render("Settings", True, WIT)
text_2 = LETTERS.render("Quit", True, WIT)
text_3 = LETTERS.render("Return", True, WIT)

def main():
    pygame.display.update()
    game = 0
    beginscherm = True
    while beginscherm == True:
        rect_1 = pygame.draw.rect(screen, ZWART, (250.2, 95, 331, 106))
        rect_2 = pygame.draw.rect(screen, ZWART, (698.8, 95, 331, 106))
        rect_3 = pygame.draw.rect(screen, ZWART, (250.2, 254.8, 331, 106))
        rect_4 = pygame.draw.rect(screen, ZWART, (698.8, 254.8, 331,106))
        rect_5 = pygame.draw.rect(screen, ZWART, (20, 640, 127, 45))
        rect_6 = pygame.draw.rect(screen, GRIJS, (25, 645, 117, 35))
        rect_7 = pygame.draw.rect(screen, ZWART, (1190, 640, 70, 45))
        rect_8 = pygame.draw.rect(screen, GRIJS, (1195, 645, 60, 35))
        button_1 = screen.blit(image_1, (255.2, 100))
        button_2 = screen.blit(image_2, (703.8, 100))
        button_3 = screen.blit(image_3, (255.2, 259.8))
        button_4 = screen.blit(image_4, (703.8, 259.8))
        text1 = screen.blit(text_1, (25, 645))
        text2 = screen.blit(text_2, (1195, 645))
        pygame.display.update()
        for event in pygame.event.get():
            # gaat naar volgende loop als er geklikt wordt
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(event.pos):
                   beginscherm = False
                   game = 1
                   while game == 1:
                        screen.fill(GROEN)
                        baan1()
                        pygame.display.update()
                elif button_2.collidepoint(event.pos):
                    beginscherm = False
                    game = 2
                    while game == 2:
                        screen.fill(GEEL)
                        pygame.display.update()
                elif button_3.collidepoint(event.pos):
                    beginscherm = False
                    game = 3
                    while game == 3:
                        screen.fill(LICHTBLAUW)
                        pygame.display.update()
                elif button_4.collidepoint(event.pos):
                    beginscherm = False
                    game = 4
                    while game == 4:
                        screen.fill(GRIJS)
                        pygame.display.update()
                elif text1.collidepoint(event.pos):
                    beginscherm = False
                    game = 5
                    settingscherm = True
                    while game == 5 and settingscherm == True:
                        screen.blit(loadingscreen, (0, 0))
                        rect_9 = pygame.draw.rect(screen, ZWART, (20, 640, 107, 45))
                        rect_10 = pygame.draw.rect(screen, GRIJS, (25, 645, 97, 35))
                        text3 = screen.blit(text_3, (25, 645))
                        pygame.display.update()
                        for event in pygame.event.get(): 
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if rect_10.collidepoint(event.pos):
                                    settingscherm = False
                                    game = 0
                                    beginscherm = True
                                    pygame.display.update()
                                    break
                            break
                elif text2.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                else:
                    break
    
    # update het scherm
    pygame.display.update()

main()


while True:
    for event in pygame.event.get():
        # sluit de game af als er op het kruisje wordt geklikt
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


pygame.quit()
sys.exit()