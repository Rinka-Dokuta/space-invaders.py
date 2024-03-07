import pygame #bring in moduel to handle graphics, input, etc

pygame.init()#Set up game
pygame.display.set_caption("Space invaders!") #Sets window title
Window = pygame.display.set_mode((800, 800)) #Creates game screen
Time = pygame.time.Clock() #Set up clock
gameover = False #Variable to run our game loop
xpos = 400
ypos = 750
moveleft = False

while not gameover: #GAME LOOP-----------------------------------
    Time.tick(60) #FPS
    
    #Input section-----------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True #quit game if x is pressed in top corner
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveleft = True
                
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveleft = False
    
    
    
    #Physics section
    if moveleft == True:
        vx =- 3
    else:
        vx = 0
    
    #update player position
    xpos += vx
    
    
    #Render section----------------------------------------------
    
    Window.fill((255, 255, 255)) #Wipe screen so it doesn't smear
    
    pygame.draw.rect(Window, (0, 250, 0), (xpos, ypos, 60, 20)) #Draw player
    pygame.draw.rect(Window, (0, 250, 0), (xpos, ypos+10, 70, 20)) #Right Wing
    pygame.draw.rect(Window, (0, 250, 0), (xpos+10, ypos+10, 70, 20)) #Left Wing
    pygame.draw.rect(Window, (0, 250, 0), (xpos+19, ypos-10, 20, 15)) #Blaster
    pygame.draw.rect(Window, (0, 250, 0), (xpos+24, ypos-20, 10, 15)) #Tiny blaster thing
    
    pygame.display.flip() #This flips the buffer (memory) where stuff has been "drawn" to the actual screen
    
#End game loop---------------------------------------------------
    
pygame.quit() 
