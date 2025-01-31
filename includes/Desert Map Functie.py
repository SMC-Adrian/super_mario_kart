def Desert():

    screen_info = pygame.display.Info()  
    screen_width = 1366
    screen_height = 768

    screen = pygame.display.set_mode((screen_width, screen_height))


    WEG = (203, 189, 147)
    ZAND = (252, 225, 102)
    OFFROAD = (112, 84, 62)
    screen.fill(ZAND)

    pygame.draw.rect(screen, WEG, (230, 64, 400, 100)) #BREEDTE, HOOGTE, LENGTE, BREEDTE
    pygame.draw.rect(screen, OFFROAD, (630, 64, 600, 542)) 
    pygame.draw.circle(screen, WEG, (1130, 606), 100, width=0, draw_top_right=False, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=True)
    pygame.draw.rect(screen, WEG, (1035, 606, 95, 100)) 
    Schuin_1 = pygame.Surface((965, 100), pygame.SRCALPHA)
    Schuin_1.fill((WEG), rect=None, special_flags=0)
    Schuin_1_Schuin= pygame.transform.rotate(Schuin_1, 332)
    screen.blit(Schuin_1_Schuin,(184, 164))
    pygame.draw.rect(screen, WEG, (130, 164, 100, 360)) 
    pygame.draw.circle(screen, WEG, (180, 606), 100, width=0, draw_top_right=True, draw_top_left=True, draw_bottom_left=True, draw_bottom_right=True)
    pygame.draw.circle(screen, ZAND, (180, 606), 20, width=0, draw_top_right=True, draw_top_left=True, draw_bottom_left=True, draw_bottom_right=True)
    pygame.draw.circle(screen, WEG, (230, 164), 100, width=0, draw_top_right=False, draw_top_left=True, draw_bottom_left=False, draw_bottom_right=False)

    pygame.display.update()