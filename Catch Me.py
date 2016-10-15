import pygame
import time
import random
pygame.init()
display_width = 800
display_height  = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green =(144,238,144)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Catch It')


clock = pygame.time.Clock()
FPS = 10
block_size = 10

font = pygame.font.SysFont(None,25)

def message_to_screen(msg,color):
    gameDisplay.fill(white)
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text, [display_width/14,display_height/2])
    
def message_to_screen_top(msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text, [display_width/4,display_height/1.5])


def gameLoop():
    gameExit = False
    gameOver = False
    lead_x = 300
    lead_y = 300
    lead_x_change = 0
    lead_y_change = 0

    lead2_x = 200
    lead2_y = 200
    lead2_x_change = 0
    lead2_y_change = 0

    randAppleX = random.randrange(0,display_width-block_size,2*block_size)
    randAppleY = random.randrange(0,display_height-block_size,2*block_size)

    points_counter = 0
    while not gameExit:
        if lead_x==lead2_x and lead_y==lead2_y:
            lead_x=display_width
            lead_y=display_height
            lead2_x=display_width/2
            lead2_y=display_height/2
            gameOver = True

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over press C to play again ,Q to quit",black)
            message_to_screen_top("points---"+str(points_counter),green)
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            #for movement of first ball    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_y_change = 0
                    lead_x_change = -2*block_size
                if event.key == pygame.K_RIGHT:
                    lead_y_change = 0
                    lead_x_change = 2*block_size
                if event.key == pygame.K_UP:
                    lead_x_change =0
                    lead_y_change = -2*block_size
                if event.key == pygame.K_DOWN:
                    lead_x_change =0
                    lead_y_change = 2*block_size
             #for movement of second ball       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    lead2_y_change = 0
                    lead2_x_change = -block_size
                if event.key == pygame.K_d:
                    lead2_y_change = 0
                    lead2_x_change = block_size
                if event.key == pygame.K_w:
                    lead2_x_change =0
                    lead2_y_change = -block_size
                if event.key == pygame.K_s:
                    lead2_x_change =0
                    lead2_y_change = block_size

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key== pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_UP or event.key== pygame.K_DOWN:
                    lead_y_change = 0
            
        #for 1st window crossing
        lead_x += lead_x_change
        lead_y += lead_y_change
        if lead_x > display_width:
            lead_x=0
        if lead_y > display_height:
            lead_y = 0
        if lead_x <0:
            lead_x=display_width
        if lead_y < 0 :
            lead_y = display_height

            
        #for 2st window crossing
        lead2_x += lead2_x_change
        lead2_y += lead2_y_change
        if lead2_x > display_width:
            lead2_x=0
        if lead2_y > display_height:
            lead2_y = 0
        if lead2_x <0:
            lead2_x=display_width
        if lead2_y < 0 :
            lead2_y = display_height

        
        
            
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,green,[randAppleX,randAppleY,block_size,block_size])
        pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])
        pygame.draw.rect(gameDisplay,red,[lead2_x,lead2_y,block_size,block_size])
        pygame.display.update() 


        if lead2_x == randAppleX and lead2_y == randAppleY:
            randAppleX = random.randrange(0,display_width-block_size,2*block_size)
            randAppleY = random.randrange(0,display_height-block_size,2*block_size)
            points_counter +=1

        if lead_x == randAppleX and lead_y == randAppleY:
            lead_x =0
            lead_y =0
            
        clock.tick(FPS)
    
    pygame.quit()
    quit()

gameLoop()

