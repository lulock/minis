# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 18:29:39 2020

@author: Lulock
"""

import pygame
import sys
from network import Network

w = 500
h = 500
pygame.init()
win = pygame.display.set_mode((w,h))
pygame.display.set_caption("Client")


clientNumber = 0

class Player():
    def __init__(self, x,y,width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 1
        
    def draw(self,win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        
        self.update()
        
    def update(self):
        self.rect = (self.x,self.y,self.width ,self.height)

def read_pos(string):
    string = string.split(",")
    return int(string[0]), int(string[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redrawWindow(win, player, player2):
    win.fill((255,255,255))
    
    player.draw(win)
    player2.draw(win)
    pygame.display.update()
    

def main():
    run = True
    print("before calling network")

    n = Network()
    print("after calling network")
    print(n.pos)
    startPos = read_pos(n.getPos())
    p = Player(startPos[0],startPos[1],100,100, (0,0,0))    
    p2 = Player(0,0,100,100,(0,255,0))
    while run:
        
        p2Pos = read_pos(n.send(make_pos((p.x,p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit(0)
        p.move()
        redrawWindow(win,p, p2)
        
main()