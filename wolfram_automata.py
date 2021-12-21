# https://mathworld.wolfram.com/ElementaryCellularAutomaton.html


import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import time
from random import *
import copy
import random
import argparse
import imageio
import pygame
from numpy import fliplr, rot90


# Parameters
dt = 0.1

pauseKey = True

blockSize =  2
mainNum = 240

background = (168,167,167)
fill = (204,82,122)


parser = argparse.ArgumentParser()

parser.add_argument('-r',  action='store', dest='rule', help='Rule number', type=int)
parser.add_argument('-g', action='store_true', default=False,
                    dest='bool_gif',
                    help='Create a gif file')

results = parser.parse_args()

numRule = 0
if results.rule or results.rule == 0:
    numRule = results.rule
else:
    numRule = random.randint(0,255)

strRule = list('{0:08b}'.format(numRule))
strRule.reverse()
lstRules = [int(s) for s in strRule]

print('Rule ' + str(numRule))
print('Press ENTER to continue and pause')

pygame.init()
title = 'Rule ' + str(numRule)
pygame.display.set_caption(title)

nx_cells = 2*mainNum +1
ny_cells = mainNum

size = width, height = blockSize*nx_cells, blockSize*ny_cells



gameBoard = [[0 for col in range(mainNum+1)] for row in range(4*mainNum +1)]
gameBoard[int((4*mainNum +1)/2)][0] = 1

screen = pygame.display.set_mode(size)
screen.fill(background)

for x in range(nx_cells):
    for y in range(ny_cells):
        rect = pygame.Rect(x*blockSize, y*blockSize,
                             blockSize, blockSize)

        if gameBoard[x+mainNum][y] == 1:
            pygame.draw.rect(screen, fill, rect, 0)
        else:
            pygame.draw.rect(screen,background, rect, 1)


frames = []
duration = []

y = 0

while y < ny_cells:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Add pause option
        if event.type == pygame.KEYDOWN:
            pauseKey = not pauseKey

    time.sleep(dt)

    for x in range(4*mainNum):
        if x >= mainNum and x < 3*mainNum+1:
            rect = pygame.Rect((x-mainNum)*blockSize, y*blockSize,
                             blockSize, blockSize)

            if gameBoard[x][y] == 1:
                pygame.draw.rect(screen, fill, rect, 0)
            else:
                pygame.draw.rect(screen, background, rect, 1)

        if not pauseKey:
            ruleIdx = 4 * gameBoard[x-1][y] + 2 * gameBoard[x][y] + 1 * gameBoard[x+1][y]
            gameBoard[x][y+1] = lstRules[ruleIdx]

    if not pauseKey:
        y +=1

    pygame.display.flip()

    if results.bool_gif and not pauseKey:
        frames.append(pygame.surfarray.array3d(screen))
        duration.append(dt)


if results.bool_gif:
    print("Creating GIF file...")

    strName = "rule" + str(numRule) + ".gif"
    imageio.mimwrite(strName,
            [fliplr(rot90(f, 3)) for f in frames], duration=duration)
    print("Ready!!")


#gifsicle Rule30.gif --resize 1000x500 > resized.gif
