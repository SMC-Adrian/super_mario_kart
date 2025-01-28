import pygame
import math
from sys import exit
import random

pygame.init()

screen = pygame.display.set_mode((1000, 600))
screenDistance = 400
screenWidth, screenHeight = screen.get_size()
screenCenter = (screenWidth / 2, screenHeight / 2)

playerPos = [0, 10, 0]
playerSpeed = 2
playerAngle = math.radians(0)
vector = pygame.math.Vector2()

points = []
for y in range(2):
    for x in range(200):
        points.append([y*1000+100,x*5+100])
for y in range(2):
    for x in range(200):
        points.append([x*5+100,y*1000+100])
#'''
for y in range(2):
    for x in range(280):
        points.append([y*1400-100,x*5-100])
for y in range(2):
    for x in range(280):
        points.append([x*5-100,y*1400-100])
#'''




clock = pygame.time.Clock()

while True:
    clock.tick(60)
    screen.fill((200, 255, 255))
    pygame.draw.rect(screen, (100,100,100),(0,screenCenter[1],screenWidth,screenCenter[1]))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    sina, cosa = math.sin(playerAngle), math.cos(playerAngle)
    sinb, cosb = math.sin(0), math.cos(0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerAngle+= math.radians(90)
        playerPos[0] += playerSpeed * math.cos(playerAngle)
        playerPos[2] += playerSpeed * math.sin(playerAngle)
        playerAngle-= math.radians(90)
    if keys[pygame.K_s]:
        playerPos[0] -= playerSpeed * cosa
        playerPos[2] -= playerSpeed * sina
    if keys[pygame.K_a]:
        playerAngle += math.radians(2)
    if keys[pygame.K_d]:
        playerAngle -= math.radians(2)

    sina, cosa = math.sin(playerAngle), math.cos(playerAngle)
    sinb, cosb = math.sin(0), math.cos(0)
    

    for point in points:
        dx, dy, dz = point[0] - playerPos[0], 0 - playerPos[1], point[1] - playerPos[2]
        xr = dz * sina + dx * cosa
        zr = dz * cosa - dx * sina
        yr = dy
        x = xr
        y = yr * cosb - zr * sinb
        z = zr * cosb + yr * sinb

        if z > 0:

            projX = (x) / (z) * screenDistance + screenCenter[0]
            projY = -(y) / (z) * screenDistance + screenCenter[1]

       

            pygame.draw.circle(screen, (255,255,255), (projX,projY), 2/z*screenDistance)


    pygame.display.update()