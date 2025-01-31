import pygame 
from sys import exit
import math
from includes.banen import *

# wtf waarom werkt dit niet
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
rode_auto = pygame.image.load(r"img/red-car.png")

        
# functies
def checkpoints_baan1():
    pygame.draw.rect(screen, WIT, (500, 50, 10, 130))

def draai_blit(screen, image, top_left, angle):
    '''
    Deze functie neemt het scherm, de afbeelding, de positie van linksboven en de hoek om de blit te draaien om het midden inplaats van om de linkerbovenhoek
    Deze functie komt van "https://youtu.be/L3ktUWfAMPg"
    '''
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    screen.blit(rotated_image, new_rect.topleft)

def scale_image(img, factor):
    '''
    Deze functie komt ook van "https://youtu.be/L3ktUWfAMPg" en past de schaal van de blit aan. 
    '''
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

# classes
class auto:
    def __init__(self, image, start_x: int, start_y: int, max_snelheid: int = 10, draaisnelheid: int = 10):
        '''
        deze class neemt de afbeelding van de auto, 
        de startpositie, 
        de maximale snelheid en de draaisnelheid

        voorbeeld: 
        rode_auto = auto(pygame.image.load("img/red-car.png"), 100, 100, 10, 10)
        '''
        self.img = scale_image(image, 0.7)
        self.max_snelheid = max_snelheid
        self.snelheid = 0
        self.versnelling = 1
        self.draaisnelheid = draaisnelheid
        self.hoek = -90
        self.x, self.y = start_x, start_y
    
    def teken_auto(self):
        '''
        Deze functie tekent gedraaide de auto op het scherm
        '''
        draai_blit(screen, self.img, (self.x, self.y), self.hoek)

    def draai_auto(self, links: bool = False, rechts: bool = False):
        '''
        deze functie neem of links of rechts en draait de auto dan met de opgegeven draaisnelheid
        '''
        if links:
            self.hoek += self.draaisnelheid
        elif rechts:
            self.hoek -= self.draaisnelheid
    
    def voren_auto(self):
        '''
        Deze functie neemt berekent de nieuwe snelheid van de auto en neemt die of de maximale snelheid
        daarna verplaatst hij de auto met een mooie formule van het internet
        '''
        self.snelheid = min(self.snelheid + self.versnelling, self.max_snelheid)

        radialen = math.radians(self.hoek)
        verticaal = math.cos(radialen) * self.snelheid
        horizontaal = math.sin(radialen) * self.snelheid
        self.y -= verticaal
        self.x -= horizontaal

    def achter_auto(self):
        self.snelheid = min(self.snelheid + self.versnelling, self.max_snelheid)

        radialen = math.radians(self.hoek)
        verticaal = math.cos(radialen) * self.snelheid
        horizontaal = math.sin(radialen) * self.snelheid
        self.y += verticaal
        self.x += horizontaal

# beginscherm loop
beginscherm = True
clock = pygame.time.Clock()
while beginscherm:
    # set ticks
    for event in pygame.event.get():
        # sluit de game af als er op het kruisje wordt geklikt
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # gaat naar volgende loop als er geklikt wordt
        if event.type == pygame.MOUSEBUTTONDOWN:
            beginscherm = False
            break
    # plaats achtergrondafbeelding in scherm
    screen.blit(loadingscreen, (0, 0))

    # update het scherm
    pygame.display.update()

rode_auto = auto(pygame.image.load("img/red-car.png"), 100, 100, 10, 15)
grijze_auto = auto(pygame.image.load("img/grey-car.png"), 100, 100, 10, 12)
while True:
    # zorgt dat de game niet sneller dan 30 keer per seconden loopt
    clock.tick(FPS)
    # achtergrond is groen
    screen.fill(GROEN)
    # teken de baan uit banen.py
    baan1()
    checkpoints_baan1()

    rode_auto.teken_auto()
    grijze_auto.teken_auto()

    keys = pygame.key.get_pressed() # komt van python documentatie
    '''
    gekozen voor alleen if statements zodat als je allebei de toetsen indrukt ze elkaar cancelen
    '''
    if keys[pygame.K_w]:
        rode_auto.voren_auto()
    if keys[pygame.K_s]:
        rode_auto.achter_auto()
    if keys[pygame.K_d]:
        rode_auto.draai_auto(rechts=True)
    if keys[pygame.K_a]:
        rode_auto.draai_auto(links=True)
    if keys[pygame.K_UP]:
        grijze_auto.voren_auto()
    if keys[pygame.K_DOWN]:
        grijze_auto.achter_auto()
    if keys[pygame.K_LEFT]:
        grijze_auto.draai_auto(links=True)
    if keys[pygame.K_RIGHT]:
        grijze_auto.draai_auto(rechts=True)
    

    pygame.display.update()

    for event in pygame.event.get():
        # sluit de game af als er op het kruisje wordt geklikt
        '''        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                rode_auto.draai_auto(rechts=True)
            elif event.key == pygame.K_a:
                rode_auto.draai_auto(links=True)
        '''
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



pygame.quit()
exit()