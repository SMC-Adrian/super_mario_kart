def Ice():

    screen_info = pygame.display.Info()  
    screen_width = 1366
    screen_height = 768

    screen = pygame.display.set_mode((screen_width, screen_height))

    LICHTBLAUW = (108, 217, 213)
    DONKERBLAUW = (21, 27, 56)
    GRIJS = (79, 79, 79)
    WIT = (255, 255, 255)

    ijsblok_x = 730
    ijsblok_speed = -0.3

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
    
        ellipse = pygame.draw.rect(screen, pygame.SRCALPHA , (1028, 195, 300, 392))
        screen.fill(WIT)
        pygame.draw.rect(screen, DONKERBLAUW, (230, 164, 900, 542))
        pygame.draw.rect(screen, LICHTBLAUW, (230, 64, 100, 100)) #BREEDTE, HOOGTE, LENGTE, BREEDTE
        pygame.draw.circle(screen, LICHTBLAUW, (330, 164), 100, width=0, draw_top_right=True, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=False) #BREEDTE, HOOGTE, STRAAL
        pygame.draw.circle(screen, LICHTBLAUW, (430, 164), 100, width=0, draw_top_right=False, draw_top_left=False, draw_bottom_left=True, draw_bottom_right=False)
        pygame.draw.rect(screen, LICHTBLAUW, (430, 164, 100, 100))
        pygame.draw.circle(screen, LICHTBLAUW, (530, 164), 100, width=0, draw_top_right=False, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=True)
        pygame.draw.circle(screen, LICHTBLAUW, (630, 164), 100, width=0, draw_top_right=False, draw_top_left=True, draw_bottom_left=False, draw_bottom_right=False)
        pygame.draw.rect(screen, LICHTBLAUW, (630, 64, 100, 100))
        pygame.draw.circle(screen, LICHTBLAUW, (730, 164), 100, width=0, draw_top_right=True, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=False)
        pygame.draw.circle(screen, LICHTBLAUW, (830, 164), 100, width=0, draw_top_right=False, draw_top_left=False, draw_bottom_left=True, draw_bottom_right=False)
        pygame.draw.rect(screen, LICHTBLAUW, (830, 164, 100, 100))
        pygame.draw.circle(screen, LICHTBLAUW, (930, 164), 100, width=0, draw_top_right=False, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=True)
        pygame.draw.circle(screen, LICHTBLAUW, (1030, 164), 100, width=0, draw_top_right=False, draw_top_left=True, draw_bottom_left=False, draw_bottom_right=False)
        pygame.draw.rect(screen, LICHTBLAUW, (1030, 64, 100, 100))
        pygame.draw.circle(screen, LICHTBLAUW, (1130, 164), 100, width=0, draw_top_right=True, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=False)
        pygame.draw.ellipse(screen, LICHTBLAUW, ellipse)
        ellipse_2 = pygame.draw.rect(screen, LICHTBLAUW , (1105, 290, 150, 200))
        pygame.draw.ellipse(screen, WIT, ellipse_2)
        pygame.draw.rect(screen, LICHTBLAUW, (1130, 164, 100, 50))
        pygame.draw.rect(screen, LICHTBLAUW, (1130, 556, 100, 50))
        pygame.draw.circle(screen, LICHTBLAUW, (1130, 606), 100, width=0, draw_top_right=False, draw_top_left=False, draw_bottom_left=False, draw_bottom_right=True)
        pygame.draw.rect(screen, LICHTBLAUW, (930, 606, 200, 100))
        pygame.draw.rect(screen, LICHTBLAUW, (230, 606, 200, 100))
        pygame.draw.circle(screen, LICHTBLAUW, (230, 606), 100, width=0, draw_top_right=False, draw_top_left=False, draw_bottom_left=True, draw_bottom_right=False)
        pygame.draw.rect(screen, LICHTBLAUW, (130, 165, 100, 441))
        pygame.draw.circle(screen, LICHTBLAUW, (230, 164), 100, width=0, draw_top_right=False, draw_top_left=True, draw_bottom_left=False, draw_bottom_right=False)
    
        if ijsblok_x <= 430:
            ijsblok_speed = 0.3   
    
        elif ijsblok_x >= 730:
            ijsblok_speed = -0.3  
    
        ijsblok_x = ijsblok_x + ijsblok_speed
        ijsblok = pygame.draw.rect(screen, LICHTBLAUW, (ijsblok_x, 606, 200, 100))
        pygame.display.update()
        
            
    


pygame.quit()
sys.exit()

    
