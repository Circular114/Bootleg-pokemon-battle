import pygame
import sys, time
import random
clock = pygame.time.Clock()
pygame.init()
black = pygame.Color(0, 0, 0)
green = pygame.Color(22, 224, 49)
red = pygame.Color(75, 0, 0)
gree = pygame.Color(0, 75, 0)
white = pygame.Color(255, 255, 255)
yellow = pygame.Color(255, 255, 0)
brown = pygame.Color(200, 150, 0)
class Color:
    blue = pygame.Color(0, 0, 255)
    re = pygame.Color(255, 0, 0)
    gren = pygame.Color(0, 255, 0)
    orang = pygame.Color(255, 170, 0)
    yello = pygame.Color(255, 255, 0)
    purp = pygame.Color(255, 0, 255)
#def
colorchange = [Color.re, Color.orang, Color.yello, Color.gren, Color.blue, Color.purp]
colornum = 0
#game var
pikastat = [30, 587.5,  200, 300, 32.5, 589.9]
head = [100, 530]
body = [[50, 530], [40, 530], [30, 530]]
direction = "null"
score = 0
#GUI var
battle = [320, 450]
bag = [450, 450]
dotmon = [320, 550]
run = [450, 550]
arrow = [365, 400]
eevee = [500, 50, 200, 300, 430, 107.5, 432.5, 109.9]
action = "empty"
timer = 0
tackle = [320, 450]
QA = [450, 450]
leer =  [320, 550]
nuzzle = [450, 550]
wordbox1 = [10, 50]
mynum = random.randint(0, 99)
#window
WIDTH = 640
HEIGHT = 640
DELTA = 10
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BLOCK BATTLE EXTREME DELUX 4")


def scoreboard():
    font = pygame.font.SysFont("new times roman", 32)
    surface = font.render("score: " + str(score), True, black)
    rectangle = surface.get_rect()
    rectangle.midtop = (80, 10)
    window.blit(surface, rectangle)

def battlegui():
    font = pygame.font.SysFont("new times roman", 36)
    surface = font.render("battle!", True, black)
    rectangle = surface.get_rect()
    rectangle.midtop = (370, 465)
    window.blit(surface, rectangle)


    
def game_over():
    font = pygame.font.SysFont("new times roman", 72)
    surface = font.render("Game over", True, black)
    rectangle = surface.get_rect()
    rectangle.midtop = (320, 25)
    window.blit(surface, rectangle)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()
def game_overlose():
    font = pygame.font.SysFont("new times roman", 72)
    surface = font.render("You lost...", True, black)
    rectangle = surface.get_rect()
    rectangle.midtop = (320, 25)
    window.blit(surface, rectangle)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()
def game_overwin():
    font = pygame.font.SysFont("new times roman", 60)
    surface = font.render("You defeated the eevee trainer!", True, black)
    rectangle = surface.get_rect()
    rectangle.midtop = (320, 25)
    window.blit(surface, rectangle)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

    
while True:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if direction != "right":
                    direction = "right"
                   
            elif event.key == pygame.K_a:
                if direction != "left":
                    direction = "left"
               
                    
            elif event.key == pygame.K_w:
                if direction != "up":
                    direction = "up"
                 
            elif event.key == pygame.K_s:
                if direction != "down":
                    direction = "down"
            elif event.key == pygame.K_e:
                if action == "empty" and arrow[0] == 495 and arrow[1] == 515:
                    action = "run"
                elif action == "empty" and arrow[0] == 365 and arrow[1] == 400:
                    action = "fight"
                elif action == "empty" and arrow[0] == 495 and arrow[1] == 400:
                    action = "bag"
                elif action == "empty" and arrow[0] == 495 and arrow[1] == 515:
                    action = "dotmon"
                    #arrow[0] = 700
                #elif action == "fight" and arrow[0] == 700:
                    #arrow[0] = 365
            elif event.key == pygame.K_q:
                if arrow[0] == 365 and arrow[1] == 400 and action == "fight":
                    action = "tackle"
                if arrow[0] == 495 and arrow[1] == 400 and action == "fight":
                    action = "tail whip"
                if arrow[0] == 495 and arrow[1] == 515 and action == "fight":
                    action = "nuzzle"
                if arrow[0] == 365 and arrow[1] == 515 and action == "fight":
                    action = "quick attack"
                
         
                   
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            
    #move
    if direction == "right":
        #head[0] += DELTA
        arrow[0] = 495
    elif direction == "left":
        #head[0] -= DELTA
        arrow[0] = 365
    elif direction == "down":
        #head[1] += DELTA
        arrow[1] = 515
    elif direction == "up":
        #head[1] -= DELTA
        arrow[1] = 400
    body.insert(0, list(head))
    body.pop()
    if action == "run":
        font = pygame.font.SysFont("new times roman", 36)
        surface = font.render("you can't do that right now!", True, black)
        rectangle = surface.get_rect()
        rectangle.midtop = (320, 320)
        window.blit(surface, rectangle)
    #draw

    window.fill(green)
    for posi in body:
        if posi == head:
            pygame.draw.rect(window, yellow, pygame.Rect(posi[0], posi[1], 50, 50))
        else:
            pygame.draw.rect(window, yellow, pygame.Rect(posi[0], posi[1], 3, 3))
        pygame.draw.rect(window, black, pygame.Rect(pikastat[0], pikastat[1], 205, 15))
        pygame.draw.rect(window, black, pygame.Rect(eevee[4], eevee[5], 205, 15))
        pygame.draw.rect(window, Color.re, pygame.Rect(eevee[6], eevee[7], eevee[2], 10))
        pygame.draw.rect(window, Color.re, pygame.Rect(pikastat[4], pikastat[5], pikastat[2], 10))

        
        pygame.draw.rect(window, white, pygame.Rect(battle[0], battle[1], 100, 50))
        pygame.draw.rect(window, white, pygame.Rect(bag[0], bag[1], 100, 50))
        pygame.draw.rect(window, white, pygame.Rect(dotmon[0], dotmon[1], 100, 50))
        pygame.draw.rect(window, white, pygame.Rect(run[0], run[1], 100, 50))
        pygame.draw.rect(window, Color.re, pygame.Rect(arrow[0], arrow[1], 10, 35))
        pygame.draw.rect(window, brown, pygame.Rect(eevee[0], eevee[1], 50, 50))

    #GUI
    font = pygame.font.SysFont("new times roman", 36)
    surface = font.render("battle!", True, black)
    rectangle = surface.get_rect()
    rectangle.midtop = (370, 465)
    window.blit(surface, rectangle)

    font = pygame.font.SysFont("new times roman", 36)
    surface = font.render("dotmon!", True, black)
    rectangle = surface.get_rect()
    rectangle.midtop = (370, 565)
    window.blit(surface, rectangle)

    font = pygame.font.SysFont("new times roman", 36)
    surface = font.render("bag!", True, black)
    rectangle = surface.get_rect()
    rectangle.midtop = (500, 465)
    window.blit(surface, rectangle)
    
    font = pygame.font.SysFont("new times roman", 36)
    surface = font.render("run!", True, black)
    rectangle = surface.get_rect()
    rectangle.midtop = (500, 565)
    window.blit(surface, rectangle)

    font = pygame.font.SysFont("new times roman", 36)
    surface = font.render("Pikachu", True, black)
    rectangle = surface.get_rect()
    rectangle.midtop = (125, 605)
    window.blit(surface, rectangle)

    font = pygame.font.SysFont("new times roman", 36)
    surface = font.render("Eevee", True, black)
    rectangle = surface.get_rect()
    rectangle.midtop = (525, 125)
    window.blit(surface, rectangle)

    if action == "run":
        font = pygame.font.SysFont("new times roman", 36)
        surface = font.render("you can't do that right now!", True, black)
        rectangle = surface.get_rect()
        rectangle.midtop = (320, 320)
        window.blit(surface, rectangle)
        if arrow[0] == 365 and arrow[1] == 400:
            action = "empty"
        elif arrow[0] == 495 and arrow[1] == 400:
            action = "empty"
        elif arrow[0] == 365 and arrow[1] == 515:
            action = "empty"
    if action == "bag":
        font = pygame.font.SysFont("new times roman", 36)
        surface = font.render("you can't do that right now!", True, black)
        rectangle = surface.get_rect()
        rectangle.midtop = (320, 320)
        window.blit(surface, rectangle)
        if arrow[0] == 365 and arrow[1] == 400:
            action = "empty"
        elif arrow[0] == 495 and arrow[1] == 515:
            action = "empty"
        elif arrow[0] == 365 and arrow[1] == 515:
            action = "empty"
    if action == "dotmon":
        font = pygame.font.SysFont("new times roman", 36)
        surface = font.render("you can't do that right now!", True, black)
        rectangle = surface.get_rect()
        rectangle.midtop = (320, 320)
        window.blit(surface, rectangle)
        if arrow[0] == 365 and arrow[1] == 400:
            action = "empty"
        elif arrow[0] == 495 and arrow[1] == 515:
            action = "empty"
        elif arrow[0] == 495 and arrow[1] == 400:
            action = "empty"
    if action == "fight":
        pygame.draw.rect(window, white, pygame.Rect(nuzzle[0], nuzzle[1], 100, 50))
        pygame.draw.rect(window, white, pygame.Rect(leer[0], leer[1], 100, 50))
        pygame.draw.rect(window, white, pygame.Rect(QA[0], QA[1], 100, 50))
        pygame.draw.rect(window, white, pygame.Rect(tackle[0], tackle[1], 100, 50))

        font = pygame.font.SysFont("new times roman", 36)
        surface = font.render("tackle!", True, black)
        rectangle = surface.get_rect()
        rectangle.midtop = (370, 465)
        window.blit(surface, rectangle)
        
    
        
        font = pygame.font.SysFont("new times roman", 26)
        surface = font.render("Quickattack!", True, black)
        rectangle = surface.get_rect()
        rectangle.midtop = (370, 565)
        window.blit(surface, rectangle)

        font = pygame.font.SysFont("new times roman", 36)
        surface = font.render("tail whip!", True, black)
        rectangle = surface.get_rect()
        rectangle.midtop = (500, 465)
        window.blit(surface, rectangle)

        font = pygame.font.SysFont("new times roman", 36)
        surface = font.render("nuzzle!", True, black)
        rectangle = surface.get_rect()
        rectangle.midtop = (500, 565)
        window.blit(surface, rectangle)

    if action == "tackle":
        font = pygame.font.SysFont("new times roman", 36)
        surface = font.render("Pikachu used tackle!", True, black)
        rectangle = surface.get_rect()
        rectangle.midtop = (320, 320)
        window.blit(surface, rectangle)
        timer += 1
        if timer == 1:
            if eevee[3] > 250:
                eevee[2] -= 40
            elif 250 >= eevee[3] > 200:
                eevee[2] -= 65
            elif 200 >= eevee[3] > 150:
                eevee[2] -= 90
            elif 150 >= eevee[3] > 100:
                eevee[2] -= 110
            elif 100 >= eevee[3] > 50:
                eevee[2] -= 140
            elif 50 >= eevee[3] >= 0:
                eevee[2] -= 155
        if timer >= 30:
            action = "opattack"
            timer = 0
    elif action == "tail whip":
        font = pygame.font.SysFont("new times roman", 36)
        surface = font.render("Pikachu used tail whip, lowering defence!", True, black)
        rectangle = surface.get_rect()
        rectangle.midtop = (320, 320)
        window.blit(surface, rectangle)
        timer += 1
        if timer == 1:
            eevee[3] -= 50
        if timer == 30:
            action = "opattack"
            timer = 0
    elif action == "quick attack":
        font = pygame.font.SysFont("new times roman", 36)
        surface = font.render("Pikachu used quick attack!", True, black)
        rectangle = surface.get_rect()
        rectangle.midtop = (320, 320)
        window.blit(surface, rectangle)
        timer += 1
        if timer == 1:
            if eevee[3] > 250:
                eevee[2] -= 50
            elif 250 >= eevee[3] > 200:
                eevee[2] -= 80
            elif 200 >= eevee[3] > 150:
                eevee[2] -= 100
            elif 150 >= eevee[3] > 100:
                eevee[2] -= 120
            elif 100 >= eevee[3] > 50:
                eevee[2] -= 140
            elif 50 >= eevee[3] >= 0:
                eevee[2] -= 155
        if timer >= 30:
            action = "opattack"
            timer = 0
    elif action == "nuzzle":
        font = pygame.font.SysFont("new times roman", 36)
        surface = font.render("Pikachu used nuzzle!", True, black)
        rectangle = surface.get_rect()
        rectangle.midtop = (320, 320)
        window.blit(surface, rectangle)
        timer += 1
        if timer == 1:
            if eevee[3] > 250:
                eevee[2] -= 60
            elif 250 >= eevee[3] > 200:
                eevee[2] -= 100
            elif 200 >= eevee[3] > 150:
                eevee[2] -= 120
            elif 150 >= eevee[3] > 100:
                    eevee[2] -= 140
            elif 100 >= eevee[3] > 50:
                eevee[2] -= 160
            elif 50 >= eevee[3] >= 0:
                eevee[2] -= 180
        if timer == 30:
            action = "opattack"
            timer = 0
                    
    if action == "opattack":
        if mynum <= 40:
            font = pygame.font.SysFont("new times roman", 36)
            surface = font.render("the eevee used tackle!", True, black)
            rectangle = surface.get_rect()
            rectangle.midtop = (320, 320)
            window.blit(surface, rectangle)
            timer += 1
            if timer == 1:
                if pikastat[3] > 250:
                    pikastat[2] -= 30
                elif 250 >= pikastat[3] > 200:
                    pikastat[2] -= 50
                elif 200 >= pikastat[3] > 150:
                    pikastat[2] -= 80
                elif 150 >= pikastat[3] > 100:
                    pikastat[2] -= 110
                elif 100 >= pikastat[3] > 50:
                    pikastat[2] -= 130
                elif 50 >= pikastat[3] >= 0:
                    pikastat[2] -= 150
                
            if timer == 30:
                action = "empty"
                timer = 0
                mynum = random.randint(0, 99)
        if 40 < mynum < 70:
            font = pygame.font.SysFont("new times roman", 36)
            surface = font.render("eevee used tail whip, lowering defence!", True, black)
            rectangle = surface.get_rect()
            rectangle.midtop = (320, 320)
            window.blit(surface, rectangle)
            timer += 1
            if timer == 1:
                pikastat[3] -= 50
            if timer == 30:
                action = "empty"
                timer = 0
                mynum = random.randint(0, 99)
        if 70 <= mynum <= 99:
            font = pygame.font.SysFont("new times roman", 36)
            surface = font.render("eevee used swift!", True, black)
            rectangle = surface.get_rect()
            rectangle.midtop = (320, 320)
            window.blit(surface, rectangle)
            timer += 1
            if timer == 1:
                if pikastat[3] > 250:
                    pikastat[2] -= 60
                elif 250 >= pikastat[3] > 200:
                    pikastat[2] -= 80
                elif 200 >= pikastat[3] > 150:
                    pikastat[2] -= 100
                elif 150 >= pikastat[3] > 100:
                    pikastat[2] -= 120
                elif 100 >= pikastat[3] > 50:
                    pikastat[2] -= 140
                elif 50 >= pikastat[3] >= 0:
                    pikastat[2] -= 160
            if timer == 30:
                action = "empty"
                timer = 0
                mynum = random.randint(0, 99)
            
    if eevee[2] <= 0 and action == "opattack":
        game_overwin()
    elif pikastat[2] <= 0 and action == "empty":
        game_overlose()
    
    scoreboard()
    #end GUI
   
   
        
    pygame.display.flip()

    #kill
    if head[0] >= WIDTH or head[0] < 0:
        game_over()
    if head[1] >= HEIGHT or head[1] < 0:
        game_over()
        
    
  
                                       
            
    if colornum < 5:
        colornum += 1
    if colornum == 5:
        colornum = 0
    #if score + 5:
        #clock.tick(25)
    clock.tick(10)

