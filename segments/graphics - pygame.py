import pygame # imports pygame
import random # imports the random module
import time
from pygame import mixer # import mixer from pygame

pygame.init() # initialises the window. Without this, pygame won't work.

window = pygame.display.set_mode((800, 600)) # window size

running = False 
intro = True # intro value set to true for intro loop

# title of game window
pygame.display.set_caption("Castle Kräftig - Pygame Edition")

# screen sizes in var
screenWidth = 800
screenHeight = 600

background = pygame.image.load('bg.png')  # this stores background in var (actual background is in mainloop)

sprite = pygame.image.load('characterUp.png')

rect = sprite.get_rect()


### rgb for white
##white = (255, 255, 255)
### rgb for green
##green = (0, 200, 0)
### rgb for red
##red = (200, 0, 0)
### rgb for bright green
##brightGreen = (0,255,0)
### rgb for bright red
##brightRed = (255,0,0)

# ----------- CLASSES -------------------------------------

# player class
class player:
    def __init__(self, x, y, w, h, xChange, yChange, vel):
        self.x = x # plater x value
        self.y = y # player y value
        self.w = w # player w (width)
        self.h = h # player h (height)
        self.xChange = xChange # player xChange (to add to x value to move player horizontally)
        self.yChange = yChange # player yChange (to aad to y value to move player vertically)
        self.vel = vel # velocity of player (needed for collision)

    #def draw(self, window):
    #    if self.left:
    #           window.blit(characterAssets[2]

# enemy class
class enemy:
    def __init__(self, x, y, w, h):
        self.x = x # enemy x value
        self.y = y # enemy y value 
        self.w = w # enemy w (width) value
        self.h = h # enemy h (height) value

# ----------------------------------------------------------------

"""enemy's x value (random value) (we pick 750 because the enemy width is 50 and
the screen width is 800. If we set the random value to 800, then the enemy has a
chance of spawning outside of the screen.)"""
enemyX = random.randint(0, 700)

"""enemy's y value (random value) (we pick 540 because the enemy height is 60
and the screen height is 600. If we set the random value to 600, the enemy has a
chance of spawning outside of the screen.)"""
enemyY = random.randint(0, 540) # enemy's y value

score = 0 # score set to 0. Will update in while loop.

rec = player(50, 50, 24, 32, 0, 0, 5) # the player's values (x, y, w, h, xChange, yChange, vel)
redRec = enemy(enemyX, enemyY, 24, 32) # the enemy's values (x, y, w, h)
#---------------------- FUNCTIONS ------------------------

# https://youtu.be/jeZkAKtDIX0 Explination
# collision system function
def detCollision(x, y, w, h, x2, y2, w2, h2):
    if (x2 + w2 >= x >= x2 and y2 + h2 >= y >= y2):
        return True
    elif (x2 + w2 >= x + w >= x2 and y2 + h2 >= y >= y2):
        return True
    elif (x2 + w2 >= x >= x2 and y2 + h2 >= y + h >= y2):
        return True
    elif (x2 + w2 >= x + w >= x2 and y2 + h2 >= y + h >= y2):
        return True
    else:
        return False

"""In case if exiting Pygame for like the window or a button isn't working
properly"""
# quit game function
def quitGame():
    pygame.quit() # quit's pygame
    """SystemExit is here so Pygame doesn't through initialization errors"""
    raise SystemExit # raises a SystemExit so python won't keep running it.

# button function
# message to display,x,y,width,height,colour,colour when mouse is on button,
# locationX of text, locationY of text, and what the button should do
def button(msg,x,y,w,h,locX,locY,action):
    global intro, running, pause, score
    mouse = pygame.mouse.get_pos() # saves mouse position in var
    click = pygame.mouse.get_pressed() # saves if clicked positon in var
    # mouse[0] means no click. mouse[1] means left click. 
    # if the x coordinate + width > x value of mouse > x coordinate and y location + 50 (bottom of box) > y of mouse > then top and bottom of y
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        # if mouse is on button, make the button brighter
        pygame.draw.rect(window, (124,124,124), (x, y, w, h)) 
        if click[0] == 1: # if mouse click is now left click
            mixer.music.load('click.wav')
            mixer.music.play()
            if action == "start": # if the action is "start"
                """The next 2 lines were added because if u started the game
                then paused, then clicked the main menu, then click start,
                the player would keep moving if you held down any of WASD buttons
                while hitting pause menu button"""
                rec.xChange = 0 # resets player's x change so the player doesn't keep moving without player hitting any key
                rec.yChange = 0 # resets player's y change so the player doesn't keep moving without player hitting any key
                running=True # set running to True
                mainloop() # call mainloop to start game

            elif action == "quit": # if action is "quit"
                quitGame() # call quitGame function

            elif action == "mainMenu": # if action is "mainMenu"
                pause = False # pause var will be set to False
                intro = True # intro var will be set to True to have menu work
                score = 0 # reset score
                rec.x = 50 # put player's x back in starting pos
                rec.y = 50 # put player's y back in starting pos
                mainMenu() # call mainMenu function to start menu

            elif action == "restart": # if action is "restart"
                pause = False # set to false so pausemenu won't keep running
                running = True # set's running to True 
                score = 0 # restart's score
                rec.x = 50 # resets player's x value
                rec.y = 50 # reset player's y value
                rec.xChange = 0 # resets player's x change so player doesn't keep moving without player hitting any key
                rec.yChange = 0 # resets player's y change so player doesn't keep moving without player hitting any key
                mainloop() # starts mainloop to restart the game

            elif action == "resume": # if action is "resume"
                running = True # set running to True again
                rec.xChange = 0 # resets player's x change so player doesn't keep moving without player hitting any key
                rec.yChange = 0 # resets player's y change so player doesn't keep moving without player hitting any key
                mainloop() # start the game once more

            elif action == "direct": # if action is direct
                intro = False # stop showing intro screen
                dMenu() # show the directionsMenu

    else: # other wise
        # if mouse is not on button, don't change colour
        pygame.draw.rect(window, (94,94,94), (x,y,w,h)) 

    # msg = is the message locX is text x pos and locY is text y pos
    text(msg, (0,0,0), locX, locY, 20, True) # the text on the button

# text function which will make text with parameters
""" msg is the message to display. Colour is the colour of text. textX is text's
x pos and textY is text's y pos. size is text size and bold is if we want text
to be bold"""
def text(msg, colour, textX, textY, size, bold):
    font = pygame.font.SysFont('times-new-roman', size, bold)
    window.blit(font.render(msg, 1, colour), (textX, textY))

# redraw game window 
def redrawWin(collisions):
    global score, sprite
    # draws the enemy
    pygame.draw.rect(window, (255,0,0), (redRec.x, redRec.y, redRec.w, redRec.h))
    # draws the player

    pygame.draw.rect(window, (0,255,0), (rec.x, rec.y, rec.w, rec.h))
    # renders Score
    text("Score: " + str(score), (255,0,0), 5, 10, 30, True) 
    # updates screen

    pygame.display.update()
    if collisions == True: # if collisions happen
        score += 1 # add one to score
        redRec.x = random.randint(0, 750) # set a new enemy x value
        redRec.y = random.randint(0, 540) # set a new enemy y value



# mainMenu function
def mainMenu():
    global running, largeText, intro

    while intro:
        for event in pygame.event.get(): # for every event in game
            #print(event)
            if event.type == pygame.QUIT: # if tries to quit
                quitGame()

            if event.type == pygame.KEYDOWN: # if any key is pressed
                if event.key == pygame.K_F4:
                    quitGame()




        # fills window with white
        window.fill((0,0,0))
        # Text for main menu (one is there cuz it has to be)

        # title
        text("Castle Kräftig", (255,0,0), (screenWidth / 2 - 230), (screenHeight - (screenHeight / 2 + 150)), 75, True)
        # where to place the text above
        # directions text
        button("Directions", 350, 290, 100, 50, 353, 300, "direct") 
        #text('Controls: WASD to move', (0,0,0), (screenWidth / 2 - 200), (screenHeight - (screenHeight / 2)), 30, True)

        # buttons for main menu

        button("Start", 150, 450, 100, 50, 175, 465, "start")
        button("Quit", 550, 450, 100, 50, 580, 465, "quit")


        pygame.display.update() # updates screen
        pygame.time.delay(15) # delays by 15 ticks

    pygame.quit()   

def pauseMenu():
    global running, largeText 
    intro = False # intro set to false and...
    running = False # running set to false so mainlooop & mainmenu won't run 
    pause = True # to start the Pause sreen
    while pause: # while pause is true
        for event in pygame.event.get(): # for all events in pygame
            if event.type == pygame.QUIT: # if tries to quit window
                quitGame() # call quitGame() function

            if event.type == pygame.KEYDOWN: # if any key is pressed
                if event.key == pygame.K_F4: # if F4 is pressed 
                    quitGame() # call quitGame() function

        # keep filling window with white (so no weirdness and also have
        # background white)
        window.fill((0,0,0))
        # Pause menu text display
        text("PAUSED", (255,0,0), (screenWidth / 2 - 150), (screenHeight - (screenHeight / 2 + 150)), 75, True)
        # Button for Main Menu
        button("Main Menu", 345, 450, 110, 50, 350, 465, "mainMenu")
        # button for restarting game 
        button("Restart", 350, 375, 100, 50, 365, 390, "restart")
        # button for resuming game
        button("Resume", 350, 300, 100, 50, 365, 315, "resume")
        # button for quitting game
        button("Quit", 350, 525, 100, 50, 380, 540, "quit")
        pygame.display.update() # updates screen
        pygame.time.delay(15) # delays by 15 ticks

# directions menu
def dMenu(): 
    insMenu = True # set loop to true
    while insMenu: # whiles insMenu is True
        for event in pygame.event.get(): # for all events that happen
            if event.type == pygame.QUIT: # if player tries to quit
                quitGame() # call quitGame()

            if event.type == pygame.KEYDOWN: # if any key is pressed
                if event.key == pygame.K_F4: # if F4 is pressed
                    quitGame() # call quitGame()

        window.fill((0,0,0)) # fill screen with white
        """ALL TEXT FOR DIRECTIONS/CONTROLS MENU WITH PLACEMENT"""
        text("DIRECTIONS/CONTROLS", (255,0,0), (screenWidth / 2 - 300), (screenHeight - (screenHeight / 2 + 250)), 50, True)
        text("W = Move Up", (140,140,140), (screenWidth / 2 - 75), (screenHeight - (screenHeight / 2 + 150)), 25, False)
        text("A = Move Left", (140,140,140), (screenWidth / 2 - 75), (screenHeight - (screenHeight / 2 + 125)), 25, False)
        text("S = Move Down", (140,140,140), (screenWidth / 2 - 75), (screenHeight - (screenHeight / 2 + 100)), 25, False)
        text("D = Move Right", (140,140,140), (screenWidth / 2 - 75), (screenHeight - (screenHeight / 2 + 75)), 25, False)
        text("F4 = Exit Game", (140,140,140), (screenWidth / 2 - 75), (screenHeight - (screenHeight / 2 + 50)), 25, False)
        text("O = Pause Game", (140,140,140), (screenWidth / 2 - 75), (screenHeight - (screenHeight / 2 + 25)), 25, False)
        text("Your goal in this game is to kill all ", (140,140,140), (screenWidth / 2 - 175), (screenHeight - (screenHeight / 2 - 75)), 25, False)
        text("the Nazis in Castle Kräftig. This game ", (140,140,140), (screenWidth / 2 - 175), (screenHeight - (screenHeight / 2 - 100)), 25, False)
        text("does NOT end. Play until you want to  ", (140,140,140), (screenWidth / 2 - 175), (screenHeight - (screenHeight / 2 - 125)), 25, False)      
        text("stop.", (140,140,140), (screenWidth / 2  - 175), (screenHeight - (screenHeight / 2 - 150)), 25, False)

        # Main Menu button to go back to main menu
        button("Main Menu", 345, 525, 110, 50, 350, 540, "mainMenu")

        pygame.display.update() # update python
        pygame.time.delay(15) # delay by 15 ticks

############################## mainloop #############################
def mainloop():
    global running, score, intro, sprite, degrees

    while running:
        """keeps filling window with the colour of choice. without this, the
        rectangle will "paint" the screen."""
        window.blit(background, (0, 0))

        #window.blit(background, (0, 0))
        pygame.time.delay(25) # delay
        for event in pygame.event.get(): # for every event in game
            if event.type == pygame.QUIT: # if I exit the game
                pygame.quit()

            if event.type == pygame.KEYUP: # if any keys are let go
                if event.key == pygame.K_a: # if key a
                    rec.xChange = 0 # set xChange to 0 (stop moving rec)

                if event.key == pygame.K_d: # if key d
                    rec.xChange = 0 # set xChange to 0 (stop moving rec)

                if event.key == pygame.K_w: # if key w
                    rec.yChange = 0 # set xChange to 0 (stop moving rec)

                if event.key == pygame.K_s: # if key s
                    rec.yChange = 0 # set xChange to 0 (stop moving rec)

                # pause key to pause game
                if event.key == pygame.K_o: # if key o
                    running = False # set running to false
                    intro = False # intro set to False
                    pauseMenu() # pauseMenu is called

            if event.type == pygame.KEYDOWN: # if any keys are pressed
                if event.key == pygame.K_F4: # if key F4
                    """(when set to false, the game will exit because of the
                    pygame.quit() command below mainloop)"""
                    pygame.quit() # set running to false

                if event.key == pygame.K_a: # if key a
                    rec.xChange += -5 # add -5 to xChange (move rec left)

                if event.key == pygame.K_d: # if key a
                    rec.xChange += 5 # adds 5 to xChange (move rec right)

                if event.key == pygame.K_w: # if key a
                    #adds -5 to yChange (moves rec up). Yes, this is supposed to say up.
                    rec.yChange += -5 # 

                if event.key == pygame.K_s: # if key a
                    # adds 5 to yChange (moves rec down). Yes, this is supposed to say down.
                    rec.yChange += 5 


        rec.x += rec.xChange # add rec's xChange to x (to do the moving)
        rec.y += rec.yChange # adds rec's yChange to y (to do the moving)



        # ----------------BOUNDARIES------------------------------
        if rec.x <= 0: # if rec's x is less than or equal to 0 (if tries to escape screen)
            rec.x  = 0 # rec's x is set to 0 so it won't go off screen.

        """(we pick 750 because the player width is 50 and the screen width is 800.
        If we set it to 800, then the player can go outside of screen."""   
        if rec.x  >= 750: # if rec's x is greater than or equal to 750 (if tries to escape screen)
            rec.x  = 750  # set rec's x to 750 so it won't go off screen

        if rec.y <= 0: # if rec's y is less than or equal to 0 (if tries to escape screen)
            rec.y = 0 # set rec's y to 0 so it won't go off screen
        """we pick 540 because the player height is 60 and the screen height is 600.
            If we set it to 600, then the player can go outside of screen"""
        if rec.y >= 540: # if rec'y is greater than or equal to 540 (if tries to escape screen) 
            rec.y = 540 # set rec's y to 540 so it won't go off screen  

        collisions = detCollision(rec.x, rec.y, rec.w, rec.h, redRec.x, redRec.y, redRec.w, redRec.h)
        # activate the redrawWin function
        redrawWin(collisions)


mainMenu() # call mainMenu first
mainloop() # call mainloop if can
pygame.quit() # activates if nothing else is now running