'''
rode auto is de variabele voor de eerste auto en het maakt niet uit welke kleur hij heeft. 
en datzelfde voor grijs bij auto 2.
'''

import pygame 
from sys import exit
import math
from includes.banen import *
import json

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
LICHTGRIJS = (121, 121, 121)
DONKERGRIJS = (31, 31, 31)
BRUIN = (115, 75, 39)
LETTERS = pygame.font.SysFont("arial", 30, bold=True, italic=False)



spelen = LETTERS.render("None", True, ZWART)
spelen2 = LETTERS.render("None", True, ZWART)

FPS = 30
clock = pygame.time.Clock()


# laad afbeeldingen en tekst
loadingscreen = pygame.image.load(r"img/loadingscreen_16_9.jpg") # deze afbeelding is door chatgpt gegenereed met de prompts: generate a image for the front of a small 2d racing game without any text using pixelart - Verbeeld an image in this style with 1280 by 720 pixels - only make a loadingscreen without side bars
car1 = pygame.image.load(r"img/car1.webp")
afbeelding1 = rode_auto_afbeelding = pygame.image.load(r"img/red-car.png")
groene_auto_afbeelding = pygame.image.load(r"img/green-car.png")
afbeelding2 = grijze_auto_afbeelding = pygame.image.load(r"img/grey-car.png")
paarse_auto_afbeelding = pygame.image.load(r"img/purple-car.png")
image_1 = pygame.image.load(r"img/grasland.jpeg")
image_2 = pygame.image.load(r"img/desert.jpeg")
image_3 = pygame.image.load(r"img/arctic.jpeg")
image_4 = pygame.image.load(r"img/city.jpeg")
image_5 = pygame.image.load(r"img/settings.jpeg")
image_6 = pygame.image.load(r"img/choosered.jpeg")
image_7 = pygame.image.load(r"img/choosegrey.jpeg")
image_8 = pygame.image.load(r"img/choosegreen.jpeg")
image_9 = pygame.image.load(r"img/choosepurple.jpeg")
image_10 = pygame.image.load(r"img/choosecar.jpeg")
text_1 = LETTERS.render("Settings", True, WIT)
text_2 = LETTERS.render("Quit", True, WIT)
text_3 = LETTERS.render("Return", True, WIT)
text_4 = LETTERS.render("Player 1:", True, DONKERBLAUW)
text_5 = LETTERS.render("Player 2:", True, WIT)
text_6 = LETTERS.render("Muziek:", True, WIT)
text_7 = LETTERS.render("AAN", True, WIT)
text_8 = LETTERS.render("UIT", True, WIT)

rode_auto_hitbox = rode_auto_afbeelding.get_rect()

check2 = False
check3 = False
check4 = False
check5 = False
check6 = False
check7 = False
check8 = False
check9 = False
Ronde1 = True
Ronde2 = False
Ronde3 = False
Ronde_Finish = False
FINISHED = False
P2_Ronde1 = True
P2_Ronde2 = False
P2_Ronde3 = False
P2_Ronde_Finish = False
P2_FINISHED = False
        
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
        case 2:
            baan2()
        case 3:
            baan3()
        case 4:
            baan4()
        case _:
            print("geen baan gevonden")
            pygame.quit()
            exit()



    

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


music = pygame.mixer.music.load("muziekjes/achtergrondmuziekje.mp3")
pygame.mixer.music.play(-1)


def beginscherm():
    global game
    screen.blit(loadingscreen, (0, 0))
    
    beginscherm_actief = True
    while beginscherm_actief:
        clock.tick(FPS)
        rect_1 = pygame.draw.rect(screen, ZWART, (250.2, 95, 331, 106))
        rect_2 = pygame.draw.rect(screen, ZWART, (698.8, 95, 331, 106))
        rect_3 = pygame.draw.rect(screen, ZWART, (250.2, 254.8, 331, 106))
        rect_4 = pygame.draw.rect(screen, ZWART, (698.8, 254.8, 331,106))
        rect_5 = pygame.draw.rect(screen, ZWART, (20, 640, 127, 45))
        rect_6 = pygame.draw.rect(screen, GRIJS, (25, 645, 117, 35))
        rect_7 = pygame.draw.rect(screen, ZWART, (1190, 640, 70, 45))
        rect_8 = pygame.draw.rect(screen, GRIJS, (1195, 645, 60, 35))
        rect_9 = pygame.draw.rect(screen, ZWART, (484, 414.6, 312, 184))
        
        button_1 = screen.blit(image_1, (255.2, 100))
        button_2 = screen.blit(image_2, (703.8, 100))
        button_3 = screen.blit(image_3, (255.2, 259.8))
        button_4 = screen.blit(image_4, (703.8, 259.8))
        button_5 = screen.blit(image_10, (489, 419.6))
        
        text1 = screen.blit(text_1, (25, 645))
        text2 = screen.blit(text_2, (1195, 645))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if button_1.collidepoint(pos):
                    return 1
                elif button_2.collidepoint(pos):
                    return 2
                elif button_3.collidepoint(pos):
                    return 3
                elif button_4.collidepoint(pos):
                    return 4
                elif text1.collidepoint(pos):  # Settings
                    return 5
                elif button_5.collidepoint(pos): # Auto kiezen
                    return 6
                elif text2.collidepoint(pos):  # Quit
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
        
        self.rect = self.img.get_rect(topleft=(self.x, self.y))
    
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
        
        self.rect.topleft = (self.x, self.y)

    def achter_auto(self):
        self.snelheid = min(self.snelheid + self.versnelling, self.max_snelheid)

        radialen = math.radians(self.hoek)
        verticaal = math.cos(radialen) * self.snelheid
        horizontaal = math.sin(radialen) * self.snelheid
        self.y += verticaal
        self.x += horizontaal
        
        self.rect.topleft = (self.x, self.y)
    

game = beginscherm()


lengte_auto1 = 260
lengte_auto2 = 260
breedte_auto1 = 75
breedte_auto2 = 105

while game == 6:
    #kies auto scherm
    screen.blit(loadingscreen, (0,0))
    rect_10 = pygame.draw.rect(screen, ZWART, (35, 145, 280, 140))
    rect_11 = pygame.draw.rect(screen, ZWART, (345, 145, 280, 140))
    rect_12 = pygame.draw.rect(screen, ZWART, (655, 145, 280, 140))
    rect_13 = pygame.draw.rect(screen, ZWART, (965, 145, 280, 140))
    rect_14 = pygame.draw.rect(screen, ZWART, (35, 395, 280, 140))
    rect_15 = pygame.draw.rect(screen, ZWART, (345, 395, 280, 140))
    rect_16 = pygame.draw.rect(screen, ZWART, (655, 395, 280, 140))
    rect_17 = pygame.draw.rect(screen, ZWART, (965, 395, 280, 140))
    rect_18 = pygame.draw.rect(screen, WIT, (600, 100, 125, 35))
    rect_19 = pygame.draw.rect(screen, DONKERBLAUW, (600, 350, 125, 35))
    rect_20 = pygame.draw.rect(screen, ZWART, (1153, 640, 107, 45))
    rect_21 = pygame.draw.rect(screen, GRIJS, (1158, 645, 97, 35))
    screen.blit(text_3, (1158, 645))
    screen.blit(text_4, (600, 100))
    screen.blit(text_5, (600, 350))
    p1_red = screen.blit(image_6, (40, 150))
    p1_grey = screen.blit(image_7, (350, 150))
    p1_green = screen.blit(image_8, (660, 150))
    p1_purple = screen.blit(image_9, (970, 150))
    p2_red = screen.blit(image_6, (40, 400))
    p2_grey = screen.blit(image_7, (350, 400))
    p2_green = screen.blit(image_8, (660, 400))
    p2_purple = screen.blit(image_9, (970, 400))
    pygame.display.update()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_20.collidepoint(event.pos):
                game = beginscherm()
                break
            elif p1_red.collidepoint(event.pos):
                afbeelding1 = rode_auto_afbeelding
                # print("rode auto gekozen")
            elif p1_grey.collidepoint(event.pos):
                afbeelding1 = grijze_auto_afbeelding
                # print("grijze auto gekozen")
            elif p1_green.collidepoint(event.pos):
                afbeelding1 = groene_auto_afbeelding
                # print("groene auto gekozen")
            elif p1_purple.collidepoint(event.pos):
                afbeelding1 = paarse_auto_afbeelding
                # print("paarse auto gekozen")
            elif p2_red.collidepoint(event.pos):
                afbeelding2 = rode_auto_afbeelding
                # print("rode auto gekozen")
            elif p2_grey.collidepoint(event.pos):
                afbeelding2 = grijze_auto_afbeelding
                # print("grijze auto gekozen")
            elif p2_green.collidepoint(event.pos):
                afbeelding2 = groene_auto_afbeelding
                # print("groene auto gekozen")
            elif p2_purple.collidepoint(event.pos):
                afbeelding2 = paarse_auto_afbeelding
                # print("paarse auto gekozen")
    pygame.display.update()

if afbeelding1: 
    rode_auto = auto(afbeelding1, lengte_auto1, breedte_auto1, 10, 10)
if afbeelding2:
    grijze_auto = auto(afbeelding2, lengte_auto2, breedte_auto2, 10, 10)

# groene_auto_1 = auto(pygame.image.load("img/green-car.png"), 260, 75, 10, 10)
# rode_auto_1 = auto(pygame.image.load("img/red-car.png"), 260, 75, 10, 10)
# grijze_auto_1 = auto(pygame.image.load("img/grey-car.png"), 260, 75, 10, 10)
# paarse_auto_1 = auto(pygame.image.load("img/purple-car.png"), 260, 75, 10, 10)

# groene_auto_2 = auto(pygame.image.load("img/green-car.png"), 260, 105, 10, 10)
# rode_auto_2 = auto(pygame.image.load("img/red-car.png"), 260, 105, 10, 10)
# grijze_auto_2 = auto(pygame.image.load("img/grey-car.png"), 260, 105, 10, 10)
# paarse_auto_2 = auto(pygame.image.load("img/purple-car.png"), 260, 105, 10, 10)

auto1 = auto(rode_auto_afbeelding, lengte_auto1, breedte_auto1, 10, 10)

start_tijd = clock.get_time()
while True:
    clock.tick(FPS)
    tijd = clock.get_time()
    if game == 5:  # Instellingen scherm
        screen.blit(loadingscreen, (0, 0))
        rect_9 = pygame.draw.rect(screen, ZWART, (1153, 640, 107, 45))
        rect_10 = pygame.draw.rect(screen, GRIJS, (1158, 645, 97, 35))
        rect_11 = pygame.draw.rect(screen, ZWART, (580, 95, 120, 45))
        rect_12 = pygame.draw.rect(screen, GRIJS, (585, 100, 110, 35))
        rect_13 = pygame.draw.rect(screen, ZWART, (557.5, 145, 75, 45))
        rect_14 = pygame.draw.rect(screen, GRIJS, (562.5, 150, 65, 35))
        rect_15 = pygame.draw.rect(screen, ZWART, (655, 145, 60, 45))
        rect_16 = pygame.draw.rect(screen, GRIJS, (660, 150, 50, 35))
        
        text3 = screen.blit(text_3, (1158, 645))
        text4 = screen.blit(text_6, (585, 100))
        text5 = screen.blit(text_7, (562.5, 150))
        text6 = screen.blit(text_8, (660, 150))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_10.collidepoint(event.pos):
                    game = beginscherm()  # Ga terug naar beginscherm
                elif rect_14.collidepoint(event.pos):
                    pygame.mixer.music.unpause()
                elif rect_16.collidepoint(event.pos):
                    pygame.mixer.music.pause()
                elif rect_16.collidepoint(event.pos):
                    pygame.mixer.music.pause()

    else:
        screen.fill(GROEN)
        kies_baan(game)  # Laad de juiste baan
        print(f"starttijd = {start_tijd}")
        print(f"current time = {tijd}")
        if game == 1:
            
            checkpoints_x_coördinaten = [1100, 1163, 1011, 735, 1115, 1115, 230, 230]
            
            checkpoint_hitbox2 = pygame.draw.rect(screen, DONKERGRIJS, (1100, 64, 10, 100))
            checkpoint_hitbox3 = pygame.draw.rect(screen, DONKERGRIJS, (1163, 210, 100, 10))
            checkpoint_hitbox4 = pygame.draw.rect(screen, DONKERGRIJS, (1011, 265, 10, 100))
            checkpoint_hitbox5 = pygame.draw.rect(screen, DONKERGRIJS, (735, 499, 140, 10))
            checkpoint_hitbox6 = pygame.draw.rect(screen, DONKERGRIJS, (1115, 506, 10, 100))
            checkpoint_hitbox7 = pygame.draw.rect(screen, DONKERGRIJS, (1115, 607, 10, 99))
            checkpoint_hitbox8 = pygame.draw.rect(screen, DONKERGRIJS, (230, 607, 10, 99))
            checkpoint_hitbox9 = pygame.draw.rect(screen, DONKERGRIJS, (230, 64, 10, 99))
            
            checkpoint_hitbox = pygame.draw.rect(screen, GRIJS, (540, 64, 10, 100))
            checkpoint = pygame.image.load(r"img/Finish Line.jpg")
            screen.blit(checkpoint, (540, 64))
            
            Rondes = ["Ronde 1","Ronde2","Ronde3"]
            
        elif game == 2:
        
            checkpoint_hitbox2 = pygame.draw.rect(screen, BRUIN, (1000, 64, 10, 100))
            checkpoint_hitbox3 = pygame.draw.rect(screen, BRUIN, (1100, 210, 100, 10))
            checkpoint_hitbox4 = pygame.draw.rect(screen, BRUIN, (1100, 596, 100, 10))
            checkpoint_hitbox5 = pygame.draw.rect(screen, DONKERGRIJS, (1060, 606, 10, 100))
            checkpoint_hitbox6 = pygame.draw.rect(screen, DONKERGRIJS, (230, 170, 10, 103))
            checkpoint_hitbox7 = pygame.draw.rect(screen, DONKERGRIJS, (130, 510, 100, 10))
            checkpoint_hitbox8 = pygame.draw.rect(screen, DONKERGRIJS, (175, 625, 10, 75))
            checkpoint_hitbox9 = pygame.draw.rect(screen, DONKERGRIJS, (230, 64, 10, 99))
            
            checkpoint_hitbox = pygame.draw.rect(screen, GRIJS, (540, 64, 10, 100))
            checkpoint = pygame.image.load(r"img\Finish Line.jpg")
            screen.blit(checkpoint, (540, 64))
            
            Rondes = ["Ronde 1","Ronde2","Ronde3"]
        
        elif game == 3:
        
            checkpoint_hitbox2 = pygame.draw.rect(screen, LICHTBLAUW, (475, 164, 10, 100))
            checkpoint_hitbox3 = pygame.draw.rect(screen, LICHTBLAUW, (675, 64, 10, 100))
            checkpoint_hitbox4 = pygame.draw.rect(screen, LICHTBLAUW, (875, 164, 10, 100))
            checkpoint_hitbox5 = pygame.draw.rect(screen, LICHTBLAUW, (1075, 64, 10, 100))
            checkpoint_hitbox6 = pygame.draw.rect(screen, LICHTBLAUW, (1130, 164, 100, 10))
            checkpoint_hitbox7 = pygame.draw.rect(screen, LICHTBLAUW, (1130, 596, 100, 10))
            checkpoint_hitbox8 = pygame.draw.rect(screen, LICHTBLAUW, (230, 606, 10, 100))
            checkpoint_hitbox9 = pygame.draw.rect(screen, LICHTBLAUW, (130, 164, 100, 10))
            
            checkpoint_hitbox = pygame.draw.rect(screen, GRIJS, (320, 64, 10, 100))
            checkpoint = pygame.image.load(r"img\Finish Line.jpg")
            screen.blit(checkpoint, (320, 64))
            
            Rondes = ["Ronde 1","Ronde2","Ronde3"]
        
        elif game == 4:
            checkpoint_hitbox2 = pygame.draw.rect(screen, DONKERGRIJS, (1020, 64, 10, 100))
            checkpoint_hitbox3 = pygame.draw.rect(screen, DONKERGRIJS, (1130, 264, 100, 10))
            checkpoint_hitbox4 = pygame.draw.rect(screen, DONKERGRIJS, (1130, 264, 100, 10))
            checkpoint_hitbox5 = pygame.draw.rect(screen, DONKERGRIJS, (1130, 594, 100, 10))
            checkpoint_hitbox6 = pygame.draw.rect(screen, DONKERGRIJS, (980, 606, 10, 100))
            checkpoint_hitbox7 = pygame.draw.rect(screen, DONKERGRIJS, (230, 606, 10, 100))
            checkpoint_hitbox8 = pygame.draw.rect(screen, DONKERGRIJS, (130, 335, 100, 10))
            checkpoint_hitbox9 = pygame.draw.rect(screen, DONKERGRIJS, (130, 164, 100, 10))
            
            checkpoint_hitbox = pygame.draw.rect(screen, GRIJS, (320, 64, 10, 100))
            checkpoint = pygame.image.load(r"img\Finish Line.jpg")
            screen.blit(checkpoint, (320, 64))
            
            Rondes = ["Ronde 1","Ronde2","Ronde3"]
            
        if rode_auto.rect.colliderect(checkpoint_hitbox) & Ronde_Finish == True & check9 == True:
            FINISHED = True
        
        if FINISHED == True:
            WIN_P1 = pygame.draw.rect(screen, DONKERGRIJS, (0, 0, 1280, 720))
            spelen = LETTERS.render("P1 GEWONNEN", True, WIT)
            EXIT_RECT = pygame.draw.rect(screen, ROOD, (590, 360, 100, 50))
            EXIT = LETTERS.render("EXIT", True, DONKERGRIJS)
            screen.blit(EXIT,(605, 365))
            if rode_auto.rect.colliderect(EXIT_RECT):
                game = beginscherm()
                check2 = False
                check3 = False
                check4 = False
                check5 = False
                check6 = False
                check7 = False
                check8 = False
                check9 = False
                Ronde1 = True
                Ronde2 = False
                Ronde3 = False
                Ronde_Finish = False
                FINISHED = False
                P2_Ronde1 = True
                P2_Ronde2 = False
                P2_Ronde3 = False
                P2_Ronde_Finish = False
                lengte_auto1 = 260
                lengte_auto2 = 260
                breedte_auto1 = 75
                breedte_auto2 = 105
                rode_auto = auto(pygame.image.load("img/red-car.png"), lengte_auto1, breedte_auto1, 10, 15)
                grijze_auto = auto(pygame.image.load("img/grey-car.png"), lengte_auto2, breedte_auto2, 10, 12)
                P2_FINISHED = False
                spelen = LETTERS.render("---", True, ZWART)
                spelen2 = LETTERS.render("---", True, ZWART)
        
        elif rode_auto.rect.colliderect(checkpoint_hitbox) & Ronde3 == True & check9 == True: #Start Ronde 3
            spelen = LETTERS.render(Rondes[2], True, ZWART)
            Ronde3 = False
            check2 = True
            check9 = False
            Ronde_Finish = True
          
         
            
        elif rode_auto.rect.colliderect(checkpoint_hitbox) & Ronde2 == True & check9 == True: #Start Ronde 2
            spelen = LETTERS.render(Rondes[1], True, ZWART)
            Ronde2 = False
            Ronde3 = True
            check2 = True
            check9 = False
            
        elif rode_auto.rect.colliderect(checkpoint_hitbox) & Ronde1 == True: #Start Ronde 1
            spelen = LETTERS.render(Rondes[0], True, ZWART)
            Ronde1 = False
            Ronde2 = True
            check2 = True
            
            
        if rode_auto.rect.colliderect(checkpoint_hitbox2) & check2 == True:
            spelen = LETTERS.render("2", True, ZWART)
            check3 = True
            
        if rode_auto.rect.colliderect(checkpoint_hitbox3) & check3 == True:
            spelen = LETTERS.render("3", True, ZWART)
            check4 = True
            
        if rode_auto.rect.colliderect(checkpoint_hitbox4) & check4 == True:
            spelen = LETTERS.render("4", True, ZWART)
            check5 = True
            
        if rode_auto.rect.colliderect(checkpoint_hitbox5) & check5 == True:
            spelen = LETTERS.render("5", True, ZWART)
            check6 = True
            
        if rode_auto.rect.colliderect(checkpoint_hitbox6) & check6 == True:
            spelen = LETTERS.render("6", True, ZWART)
            check7 = True
        
        if rode_auto.rect.colliderect(checkpoint_hitbox7) & check7 == True:
            spelen = LETTERS.render("7", True, ZWART)
            check8 = True
            
        if rode_auto.rect.colliderect(checkpoint_hitbox8) & check8 == True:
            spelen = LETTERS.render("8", True, ZWART)
            check9 = True
        
        if rode_auto.rect.colliderect(checkpoint_hitbox9) & check9 == True:
            spelen = LETTERS.render("9", True, ZWART)
            Ronde2 = True
            check1 = False
            check2 = False
            check3 = False
            check4 = False
            check5 = False
            check6 = False
            check7 = False
            check8 = False
            
        screen.blit(spelen, (0,0))
    
        if grijze_auto.rect.colliderect(checkpoint_hitbox) & P2_Ronde_Finish == True & check9 == True:
            P2_FINISHED = True
        
        if P2_FINISHED == True:
            WIN_P2 = pygame.draw.rect(screen, DONKERGRIJS, (0, 0, 1280, 720))
            spelen2 = LETTERS.render("P2 GEWONNEN", True, WIT)
            EXIT_RECT = pygame.draw.rect(screen, ROOD, (590, 360, 100, 50))
            EXIT = LETTERS.render("EXIT", True, DONKERGRIJS)
            screen.blit(EXIT,(605, 365))
            if grijze_auto.rect.colliderect(EXIT_RECT):
                game = beginscherm()
                check2 = False
                check3 = False
                check4 = False
                check5 = False
                check6 = False
                check7 = False
                check8 = False
                check9 = False
                Ronde1 = True
                Ronde2 = False
                Ronde3 = False
                Ronde_Finish = False
                FINISHED = False
                P2_Ronde1 = True
                P2_Ronde2 = False
                P2_Ronde3 = False
                P2_Ronde_Finish = False
                lengte_auto1 = 260
                lengte_auto2 = 260
                breedte_auto1 = 75
                breedte_auto2 = 105
                rode_auto = auto(pygame.image.load("img/red-car.png"), lengte_auto1, breedte_auto1, 10, 15)
                grijze_auto = auto(pygame.image.load("img/grey-car.png"), lengte_auto2, breedte_auto2, 10, 12)
                P2_FINISHED = False
                spelen = LETTERS.render("---", True, ZWART)
                spelen2 = LETTERS.render("---", True, ZWART)
                
            
        elif grijze_auto.rect.colliderect(checkpoint_hitbox) & P2_Ronde3 == True & check9 == True: #Start Ronde 3
            spelen2 = LETTERS.render(Rondes[2], True, ZWART)
            P2_Ronde3 = False
            check2 = True
            check9 = False
            P2_Ronde_Finish = True
          
         
            
        elif grijze_auto.rect.colliderect(checkpoint_hitbox) & P2_Ronde2 == True & check9 == True: #Start Ronde 2
            spelen2 = LETTERS.render(Rondes[1], True, ZWART)
            P2_Ronde2 = False
            P2_Ronde3 = True
            check2 = True
            check9 = False
            
        elif grijze_auto.rect.colliderect(checkpoint_hitbox) & P2_Ronde1 == True: #Start Ronde 1
            spelen2 = LETTERS.render(Rondes[0], True, ZWART)
            P2_Ronde1 = False
            Ronde2 = True
            check2 = True
            
            
        if grijze_auto.rect.colliderect(checkpoint_hitbox2) & check2 == True:
            spelen2 = LETTERS.render("2", True, ZWART)
            check3 = True
            
        if grijze_auto.rect.colliderect(checkpoint_hitbox3) & check3 == True:
            spelen2 = LETTERS.render("3", True, ZWART)
            check4 = True
            
        if grijze_auto.rect.colliderect(checkpoint_hitbox4) & check4 == True:
            spelen2 = LETTERS.render("4", True, ZWART)
            check5 = True
            
        if grijze_auto.rect.colliderect(checkpoint_hitbox5) & check5 == True:
            spelen2 = LETTERS.render("5", True, ZWART)
            check6 = True
            
        if grijze_auto.rect.colliderect(checkpoint_hitbox6) & check6 == True:
            spelen2 = LETTERS.render("6", True, ZWART)
            check7 = True
        
        if grijze_auto.rect.colliderect(checkpoint_hitbox7) & check7 == True:
            spelen2 = LETTERS.render("7", True, ZWART)
            check8 = True
            
        if grijze_auto.rect.colliderect(checkpoint_hitbox8) & check8 == True:
            spelen2 = LETTERS.render("8", True, ZWART)
            check9 = True
        
        if grijze_auto.rect.colliderect(checkpoint_hitbox9) & check9 == True:
            spelen2 = LETTERS.render("9", True, ZWART)
            P2_Ronde2 = True
            check1 = False
            check2 = False
            check3 = False
            check4 = False
            check5 = False
            check6 = False
            check7 = False
            check8 = False
            
        screen.blit(spelen2, (1000,0))
            
        rode_auto.teken_auto()
        grijze_auto.teken_auto()
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: rode_auto.voren_auto()
        if keys[pygame.K_s]: rode_auto.achter_auto()
        if keys[pygame.K_d]: rode_auto.draai_auto(rechts=True)
        if keys[pygame.K_a]: rode_auto.draai_auto(links=True)
        if keys[pygame.K_UP]: grijze_auto.voren_auto()
        if keys[pygame.K_DOWN]: grijze_auto.achter_auto()
        if keys[pygame.K_LEFT]: grijze_auto.draai_auto(links=True)
        if keys[pygame.K_RIGHT]: grijze_auto.draai_auto(rechts=True)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
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