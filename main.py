import pygame 
from sys import exit
import math
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

game = 0

FPS = 30

# laad afbeeldingen en tekst
loadingscreen = pygame.image.load(r"img/loadingscreen_16_9.jpg") # deze afbeelding is door chatgpt gegenereed met de prompts: generate a image for the front of a small 2d racing game without any text using pixelart - Verbeeld an image in this style with 1280 by 720 pixels - only make a loadingscreen without side bars
car1 = pygame.image.load(r"img/car1.webp")
rode_auto = pygame.image.load(r"img/red-car.png")
image_1 = pygame.image.load(r"img/grasland.jpeg")
image_2 = pygame.image.load(r"img/desert.jpeg")
image_3 = pygame.image.load(r"img/arctic.jpeg")
image_4 = pygame.image.load(r"img/city.jpeg")
image_5 = pygame.image.load(r"img/settings.jpeg")
text_1 = LETTERS.render("Settings", True, WIT)
text_2 = LETTERS.render("Quit", True, WIT)
text_3 = LETTERS.render("Return", True, WIT)

        
# functies
def kies_baan(game: int):
    '''
    Deze functie kies laad de baan in die bij de game hoort met een match case statement. \n
    case 1 = baan1\n
    case 2 = dessert\n
    case 3 = ice\n
    case 4 = city\n
    case 5 = settings\n
    case 6 = auto kiezen\n
    '''
    match game:
        case 1:
            baan1()
        case _:
            print("geen baan gevonden")
            pygame.quit()
            exit()

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

def beginscherm():
    # plaats achtergrondafbeelding in scherm
    screen.blit(loadingscreen, (0, 0))
    pygame.display.update()
    global game
    beginscherm = True
    while beginscherm == True:
        # update het scherm
        pygame.display.update()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
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
                   return 1
                elif button_2.collidepoint(event.pos):
                    beginscherm = False
                    return 2
                elif button_3.collidepoint(event.pos):
                    beginscherm = False
                    return 3
                elif button_4.collidepoint(event.pos):
                    beginscherm = False
                    return 4
                elif text1.collidepoint(event.pos):
                    beginscherm = False
                    return 5
                elif text2.collidepoint(event.pos):
                    pygame.quit()
                    exit()

    


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
    

game = beginscherm()

clock = pygame.time.Clock()
rode_auto = auto(pygame.image.load("img/red-car.png"), 100, 100, 10, 15)
grijze_auto = auto(pygame.image.load("img/grey-car.png"), 100, 100, 10, 12)

while game == 5:
    '''
    settings scherm
    ''' 
    screen.blit(loadingscreen, (0, 0))
    rect_9 = pygame.draw.rect(screen, ZWART, (1153, 640, 107, 45))
    rect_10 = pygame.draw.rect(screen, GRIJS, (1158, 645, 97, 35))
    text3 = screen.blit(text_3, (1158, 645))
    pygame.display.update()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_10.collidepoint(event.pos):
                game = 0
                beginscherm = True 
                break
while game == 6: 
    '''
    auto kiezen loop
    '''
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

while True:
    # zorgt dat de game niet sneller dan 30 keer per seconden loopt
    clock.tick(FPS)
    # achtergrond is groen
    screen.fill(GROEN)
    # teken de baan uit banen.py
    kies_baan(2)
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