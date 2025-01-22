def Grasslands():
    screen_info = pygame.display.Info()
    screen_width = 1366
    screen_height = 768
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    GROEN = (44, 122, 44)
    GRIJS = (79, 79, 79)
    WIT = (255, 255, 255)
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
