import pygame
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('snake_game')

gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

lead2_x = 200
lead2_y = 200
lead2_x_change = 0
lead2_y_change = 0
clock = pygame.time.Clock()

while not gameExit:
    if lead_x==lead2_x and lead_y==lead2_y:
        lead_x=300
        lead_y=300
        lead2_x=200
        lead2_y=200
        break
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        #for movement of first ball    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_y_change = 0
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_y_change = 0
                lead_x_change = 10
            if event.key == pygame.K_UP:
                lead_x_change =0
                lead_y_change = -10
            if event.key == pygame.K_DOWN:
                lead_x_change =0
                lead_y_change = 10
         #for movement of second ball       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                lead2_y_change = 0
                lead2_x_change = -10
            if event.key == pygame.K_d:
                lead2_y_change = 0
                lead2_x_change = 10
            if event.key == pygame.K_w:
                lead2_x_change =0
                lead2_y_change = -10
            if event.key == pygame.K_s:
                lead2_x_change =0
                lead2_y_change = 10
        
    #for 1st window crossing
    lead_x += lead_x_change
    lead_y += lead_y_change
    if lead_x > 800:
        lead_x=0
    if lead_y > 600:
        lead_y = 0
    if lead_x <0:
        lead_x=800
    if lead_y < 0 :
        lead_y = 600
        
    #for 2st window crossing
    lead2_x += lead2_x_change
    lead2_y += lead2_y_change
    if lead2_x > 800:
        lead2_x=0
    if lead2_y > 600:
        lead2_y = 0
    if lead2_x <0:
        lead2_x=800
    if lead2_y < 0 :
        lead2_y = 600

    
        
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,10,10])
    pygame.draw.rect(gameDisplay,red,[lead2_x,lead2_y,10,10])
    pygame.display.update() 

    clock.tick(10)
    
pygame.display.update()
pygame.quit()
quit()
