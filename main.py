# -*- coding: utf-8 -*-
import pygame
from sys import exit
import random
import time 

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((450,700),0,32)
pygame.display.set_caption("fighter")
backgroud=pygame.image.load('backgroud.jpg').convert()
pygame.mouse.set_visible(False)
screen.blit(backgroud,(0,0))
pygame.display.update()

class Boss_van:
      def __init__(self):
            self.active=False
            self.x=20
            self.y=50
            self.images=[]
            self.images.extend([pygame.image.load("cd01.png"),
                                pygame.image.load("cd02.png"),
                                pygame.image.load("cd03.png"),
                                pygame.image.load("cd04.png"),
                                pygame.image.load("cd05.png"),
                                pygame.image.load("cd06.png"),
                                pygame.image.load("cd07.png"),
                                pygame.image.load("cd08.png"),
                                pygame.image.load("cd09.png"),
                                pygame.image.load("cd10.png"),
                                pygame.image.load("cd11.png"),
                                pygame.image.load("cd12.png"),
                                pygame.image.load("cd13.png"),
                                pygame.image.load("cd14.png"),
                                pygame.image.load("cd15.png"),
                                pygame.image.load("cd16.png")
                                ])
      def move1(self):
            self.x+=1
      def reset(self):
            self.x=0
            self.y=50
                               
class Bullet:
      def __init__(self):
            self.x=0
            self.y=-1
            self.image=pygame.image.load('bullet.png').convert_alpha()
            self.active=False

      def move(self):
            if self.y<0:
                  self.active=False
            if self.active:
                  self.y-=8
      def restart(self):
                  mouseX,mouseY=pygame.mouse.get_pos()
                  self.x=mouseX-self.image.get_width()/2
                  self.y=mouseY-self.image.get_height()/2
                  self.active=True
class Enemy:
      def restart(self):
            self.x=random.randint(40,400)
            self.y=random.randint(-200,-80)
            self.speed=random.uniform(5,10)+1
      def __init__(self):
            self.restart()
            self.image=pygame.image.load('enemy1.png').convert_alpha()

      def move(self):
            if self.y<700:
                  self.y+=self.speed
            else:
                  self.restart()
def checkhit(enemy,bullet):
      if (bullet.x>enemy.x and bullet.x<enemy.x+enemy.image.get_width()) and (bullet.y>enemy.y and bullet.y<enemy.y+enemy.image.get_height()):
            enemy.restart()
            bullet.active=False
            plane.score+=50

class Plane:
      def __init__(self):
            self.restart()
            self.image=pygame.image.load('plane.png').convert_alpha()
            self.active=True
            self.score=0
      def move(self):
            if self.active:
                  x,y=pygame.mouse.get_pos()
                  x-=self.image.get_width()/2
                  y-=self.image.get_height()/2
                  self.x=x
                  self.y=y
      def restart(self):
            self.x=0
            self.y=600
            self.active=True
def checkCrash(enemy,plane):
      if (plane.x+0.7*plane.image.get_width()>enemy.x) and (plane.x+0.3*plane.image.get_width()<enemy.x+enemy.image.get_width()) and (plane.y+0.7*plane.image.get_height()>enemy.y) and (plane.y+0.3*plane.image.get_height()<enemy.y+enemy.image.get_height()):
            plane.active=False
            enemy.restart()
enemies=[]
plane=Plane()
for i in range(random.randint(4,6)):
      enemies.append(Enemy())
bullets=[]
for i in range(5):
      bullets.append(Bullet())
b_count=len(bullets)
b_index=0
b_interval=0
font=pygame.font.Font(None, 25)
van=Boss_van()
van_index=0
delay=60
while True:
      for event in pygame.event.get():
            if event.type==pygame.QUIT:
                  pygame.quit()
                  exit()
      screen.blit(backgroud,(0,0))
      clock.tick(60)
      if delay==0:
            delay=60
            delay-=1
      if plane.active:
            if plane.score==2000:
                  van.active=True
            if van.active:
                  van.move1()
                  if van.x>450:
                        van.reset()
                        
                  if not (delay%12):
                         screen.blit(van.images[van_index],(van.x,van.y))
                         van_index=(van_index+1)%16
                               

                  
            b_interval-=1
            if b_interval<0:
                  bullets[b_index].restart()
                  b_interval=15
                  b_index=(b_index+1)%b_count
            for b in bullets:
                  if b.active:
                        for e in enemies:
                              checkhit(e,b)
                        b.move()
                        screen.blit(b.image,(b.x,b.y))

            for e in enemies:
                  e.move()
                  screen.blit(e.image,(e.x,e.y))
                  checkCrash(e, plane)
            plane.move()
            screen.blit(plane.image,(plane.x,plane.y))
            text=font.render("Socre:%d"%plane.score,1,(0,0,0))
            screen.blit(text,(0,0))
            pygame.display.update()
      if (plane.active==False and event.type==pygame.MOUSEBUTTONUP):
            plane.restart()
            plane.score=0
            for b in bullets:
                  b.restart()
            for e in enemies:
                  e.restart()
      
      if plane.active==False:
            text=font.render("Socre:%d"%plane.score,1,(0,0,0))
            screen.blit(text,(190,350))
            pygame.display.update()
            
      

      
