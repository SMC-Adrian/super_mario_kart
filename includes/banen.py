import pygame
GROEN = (44, 122, 44)
GRIJS = (79, 79, 79)
WIT = (255, 255, 255)

def Grasslands():
    screen_info = pygame.display.Info()
    screen_width = 1366
    screen_height = 768
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    screen.fill(GROEN)
    
    pygame.draw.rect(screen, GRIJS, (230, 64, 883, 100)) #BREEDTE, HOOGTE, LENGTE, BREEDTE
    pygame.draw.circle(screen, GRIJS, (1113, 215), 150, width=0, draw_top_right=True, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=True)
    pygame.draw.circle(screen, GROEN, (1113, 215), 50, width=0, draw_top_right=True, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=True)
    pygame.draw.rect(screen, GRIJS, (913, 265, 200, 100))
    
    Schuin_1 = pygame.Surface((300, 100), pygame.SRCALPHA)
    Schuin_1.fill((GRIJS), rect=None, special_flags=0)
    Schuin_1_Schuin= pygame.transform.rotate(Schuin_1, 45)
    screen.blit(Schuin_1_Schuin,(731, 293))
    
    Schuin_1 = pygame.Surface((100, 100), pygame.SRCALPHA)
    Schuin_1.fill((GROEN), rect=None, special_flags=0)
    Schuin_1_Schuin= pygame.transform.rotate(Schuin_1, 45)
    screen.blit(Schuin_1_Schuin,(830, 194))
    
    pygame.draw.circle(screen, GRIJS, (830, 506), 100, width=0, draw_top_right=False, draw_top_left=False, draw_bottom_left=True, draw_bottom_right=False)
    pygame.draw.rect(screen, GRIJS, (830, 506, 300, 100))
    pygame.draw.circle(screen, GRIJS, (1130, 606), 100, width=0, draw_top_right=True, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=True)
    pygame.draw.rect(screen, GRIJS, (230, 606, 900, 100))
    pygame.draw.rect(screen, WIT, (825, 606, 300, 1))
    pygame.draw.circle(screen, GRIJS, (230, 606), 100, width=0, draw_top_right=False, draw_top_left=False, draw_bottom_left=True, draw_bottom_right=False)
    pygame.draw.rect(screen, GRIJS, (130, 165, 100, 441))
    pygame.draw.circle(screen, GRIJS, (230, 164), 100, width=0, draw_top_right=False, draw_top_left=True, draw_bottom_left=False, draw_bottom_right=False)
    
    pygame.display.update()

def baan1(screen=pygame.display.set_mode((1280, 720)))->None:
    screen.fill(GROEN)

    pygame.draw.rect(screen, GRIJS, (230, 64, 883, 100)) #BREEDTE, HOOGTE, LENGTE, BREEDTE
    pygame.draw.circle(screen, GRIJS, (1113, 215), 150, width=0, draw_top_right=True, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=True)
    pygame.draw.circle(screen, GROEN, (1113, 215), 50, width=0, draw_top_right=True, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=True)
    pygame.draw.rect(screen, GRIJS, (913, 265, 200, 100))
    
    Schuin_1 = pygame.Surface((300, 100), pygame.SRCALPHA)
    Schuin_1.fill((GRIJS), rect=None, special_flags=0)
    Schuin_1_Schuin= pygame.transform.rotate(Schuin_1, 45)
    screen.blit(Schuin_1_Schuin,(731, 293))
    
    Schuin_1 = pygame.Surface((100, 100), pygame.SRCALPHA)
    Schuin_1.fill((GROEN), rect=None, special_flags=0)
    Schuin_1_Schuin= pygame.transform.rotate(Schuin_1, 45)
    screen.blit(Schuin_1_Schuin,(830, 194))
    
    pygame.draw.circle(screen, GRIJS, (830, 506), 100, width=0, draw_top_right=False, draw_top_left=False, draw_bottom_left=True, draw_bottom_right=False)
    pygame.draw.rect(screen, GRIJS, (830, 506, 300, 100))
    pygame.draw.circle(screen, GRIJS, (1130, 606), 100, width=0, draw_top_right=True, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=True)
    pygame.draw.rect(screen, GRIJS, (230, 606, 900, 100))
    pygame.draw.rect(screen, WIT, (825, 606, 300, 1))
    pygame.draw.circle(screen, GRIJS, (230, 606), 100, width=0, draw_top_right=False, draw_top_left=False, draw_bottom_left=True, draw_bottom_right=False)
    pygame.draw.rect(screen, GRIJS, (130, 165, 100, 441))
    pygame.draw.circle(screen, GRIJS, (230, 164), 100, width=0, draw_top_right=False, draw_top_left=True, draw_bottom_left=False, draw_bottom_right=False)

def DesertBaan(screen=pygame.display.set_mode((1280, 720)))->None:

    Achtergrond = pygame.image.load(r"img\Desert BG.jpg")
    Achtergond = pygame.transform.scale(Achtergrond, (screen_width, screen_height))
    screen.blit(Achtergrond, (0, 0))

    Bocht = pygame.Surface((200, 200), pygame.SRCALPHA)
    Weg_Texture = pygame.image.load(r"img\Desert Weg Texture.jpg")
    OffRoad_Texture = pygame.image.load(r"img\Offroad.jpg")
    Offroad = pygame.transform.scale(OffRoad_Texture, (600, 542))
    Weg = pygame.transform.scale(Weg_Texture, (600, 100))

    screen.blit(Weg, (230, 64))
    screen.blit(Offroad, (630, 64))
    pygame.draw.circle(Bocht, (255, 255, 255, 255), (100, 100), 100, width=0, draw_top_right=False, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=True)
    Bocht.blit(Weg_Texture, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    screen.blit(Bocht, (1030, 506))
    Weg = pygame.transform.scale(Weg_Texture, (95, 100))
    screen.blit(Weg, (1035, 606))
    Desert_Weg_Texture = pygame.transform.scale(Weg_Texture, (965, 100))
    Schuin_1 = pygame.Surface((965, 100), pygame.SRCALPHA)
    Schuin_1.blit(Desert_Weg_Texture, (0, 0))
    Schuin_1_Schuin = pygame.transform.rotate(Schuin_1, 332)
    screen.blit(Schuin_1_Schuin, (184, 164))
    Weg = pygame.transform.scale(Weg_Texture, (100, 360))
    screen.blit(Weg, (130, 164))
    Bocht_2 = pygame.Surface((100, 100), pygame.SRCALPHA)
    pygame.draw.circle(Bocht_2, (255, 255, 255, 255), (100, 100), 100, width=0, draw_top_right=False, draw_top_left=True, draw_bottom_left=False, draw_bottom_right=False)
    Bocht_2.blit(Weg_Texture, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    screen.blit(Bocht_2, (130, 64))  
    Bocht = pygame.Surface((200, 200), pygame.SRCALPHA)
    pygame.draw.circle(Bocht, (255, 255, 255, 255), (100, 100), 100, width=0)
    Bocht.blit(Weg_Texture, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    screen.blit(Bocht, (80, 506))  
    pygame.draw.circle(screen, GRIJS, (180, 606), 20, width=0, draw_top_right=True, draw_top_left=True, draw_bottom_left=True, draw_bottom_right=True)
