import pygame
import time
import sys
import random


class snake:
    def __init__(self):
        self.position=[100,50]
        self.body = [[100, 50],[90, 50],[80, 50],[70, 50]]
        self.direction="RIGHT"
        self.changetoDir = self.direction


    def changetoDir(self,dir):
        if self.direction == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if self.direction == "LEFT" and not self.direction ==  "RIGHT":
            self.direction = "LEFT"

        if self.direction == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if self.direction == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"





    def move(self,foodpos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] += 10
        if self.direction == "DOWN":
            self.position[1] -= 10
        self.body.insert(0,self.direction)
        if self.position == foodpos:
            return 1
        else:
            self.pop()
            return 0


    def checkcollision(self):
        if self.position[0]>490 or self.position[0]<0:
            return 1
        elif self.position[1]>490 or self.position[1]<0:
            return 1


        for bodypart in self.body[1:]:
            if self.position== bodypart:
                return 1
        return 0


    def getheadpos(self):
        return self.position


    def getbodypos(self):
        return self.body




class foodgenerate:
    def __init__(self):
        self.position= [[random.randrange(1,50)*10],random.randrange(1,50)*10]
        self.isfoodonscreen = True
    def nofood(self):
        if self.isfoodonscreen == False:
            self.position= [[random.randrange(1,50)*10], [random.randrange(1,50*10)]]
            self.isfoodonscreen = True


    def setfood(self,food):
        self.isfoodonscreen= food



window = pygame.display.set_mode((500,500))
pygame.display.set_caption("SNAKE GAME")
fpv = pygame.time.clock()



score=0
snake =snake()
foodgenerate = foodgenerate()



def gameover():
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            gameover();
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                snake.changetoDir("RIGHT")
            if event.type == pygame.K_LEFT:
                snake.changetoDir("LEFT")
            if event.type == pygame.K_UP:
                snake.changetoDir("UP")
            if event.type == pygame.K_DOWN:
                snake.changetoDir("DOWN")
        foodpos= foodgenerate.nofood()

    if (snake.foodpos == 1):
        score+= 1
        foodgenerate.setfood(False)

window.fill(pygame.color(225,225,225))
for pos in snake.getbody():
    pygame.draw.rect(window,pygame.color(0,255,0),pygame.rect(pos[0],pos[1],10,10))
pygame.draw.rect(window, pygame.color(0, 255, 0), pygame.rect(foodpos[0],foodpos[1], 10, 10))

if (snake.checkcollision()== 1):
    gameover()

pygame.display.set_caption("WOW SNAKE GAME"+ str(score))
pygame.display.flip()
fpv.tick(24)




