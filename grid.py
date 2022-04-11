import numpy as np
import pygame

class Grid:
    def __init__(self, width, height, block):
        self.width = int(width/block)
        self.height = int(height/block)
        self.block = block
        self.cel = np.ndarray(shape=(int(self.width), int(self.height)))

    def init(self, surface):
        for x in range(self.width):
            pygame.draw.line(surface, (255, 0, 0), ((x*self.block),(0)), ((x*self.block),(self.height*self.block)))
            for y in range(self.height):
                self.cel[x][y] = np.random.randint(2)
                pygame.draw.line(surface, (255, 0, 0), ((0),(y*self.block)), ((self.width*self.block),(y*self.block)))
        pygame.draw.line(surface, (255, 0, 0), ((self.width*self.block-1),(0)), ((self.width*self.block-1),(self.height*self.block)))
        pygame.draw.line(surface, (255, 0, 0), ((0),(self.height*self.block-1)), ((self.width*self.block),(self.height*self.block-1)))

    def turno(self, surface, color):
        for x in range(self.width):
            for y in range(self.height):
                if self.cel[x][y] == 1:
                    pygame.draw.rect(surface, color, [(y*self.block), (x*self.block), self.block-1, self.block-1])
                else:
                    pygame.draw.rect(surface, (255, 255, 255), [(y*self.block), (x*self.block), self.block-1, self.block-1])

        temp = np.ndarray(shape=(int(self.width), int(self.height)))
        for x in range(self.width):
            for y in range(self.height):
                    neighbours = self.neighborhood(x,y)
                    if self.cel[x][y] == 0 and neighbours == 3:
                        temp[x][y] = 1
                    elif self.cel[x][y] == 1 and (neighbours < 2 or neighbours > 3):
                        temp[x][y] = 0
                    else:
                        temp[x][y] = self.cel[x][y]
        self.cel = temp

    def neighborhood(self, x, y):
        total = 0
        for a in range(-1, 2):
            for d in range(-1, 2):
                if x+a < self.width and y+d < self.height:
                    if self.cel[x+a][y+d] == 1:
                        total += 1
        total -= self.cel[x][y]
        return total