import pygame
import sys

pygame.init()

screen_info = pygame.display.Info()
screen_width = 1366
screen_height = 768
   
screen = pygame.display.set_mode((screen_width, screen_height))

        
GROEN = (44, 122, 44)
GRIJS = (79, 79, 79)
WIT = (255, 255, 255)
screen.fill(GROEN)
LETTERS = pygame.font.SysFont("arial", 20, bold=False, italic=False)
text = LETTERS.render("HALLO", True, WIT)
pygame.draw.rect(screen, GRIJS, (230, 64, 883, 100)) #BREEDTE, HOOGTE, LENGTE, BREEDTE


screen.blit(text, (650, 110))


pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
           
   


pygame.quit()
sys.exit()
