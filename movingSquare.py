from sys import platform
import pygame
from pygame import image
import keyboard

pygame.init()

# Local player
playerX = 400
playerY = 40
playerImage = pygame.image.load("Apps-Icon-Template-icon.png")
playerImage = pygame.transform.scale(playerImage, (64, 64))


def player():
    screen.blit(playerImage,(playerX, playerY))


running = 1
while running:
    screen = pygame.display.set_mode((800,800))
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
    
    if keyboard.is_pressed("a"):
        playerX -= 2
    if keyboard.is_pressed("d"):
        playerX += 2
    if keyboard.is_pressed("w"):
        playerY -= 2
    if keyboard.is_pressed("s"):
        playerY += 2

    player()
    pygame.display.update()

    if playerX <= 0:
        playerX = 0
    elif playerX >= 672:
        playerX = 672
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 672:
        playerY = 672

# force quit the game
    if keyboard.is_pressed("q"):
        running = 0