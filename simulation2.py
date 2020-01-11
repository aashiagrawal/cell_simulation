from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib
import random
import numpy as np

# matplotlib.interactive(True)


class Grid:
    def __init__ (self, numCells):
        self.height = 100
        self.width = 100
        self.numCells = numCells
        self.listOfCells = []
        self.listOfPositions = []
    

    # def getNumCells(self):
    #     return self.numCells

    def populateGridWithCells(self):
        for i in range(self.numCells):
            randomX = random.randint(0, 99)
            randomY = random.randint(0, 99)

            while ((randomX, randomY) in self.listOfPositions):
                randomX = random.randint(0, 99)
                randomY = random.randint(0, 99)

            self.listOfPositions.append((randomX, randomY))
            createdCell = Cell (1, randomX, randomY)
            self.listOfCells.append(createdCell)

    def updateAllCellPositions(self):
        # Code to update each cell's position based on curent position and current velocity
        for cell in range(len(self.listOfCells)):
            curCell = self.listOfCells[cell]
            curCell.x = (curCell.x + curCell.xVelocity) % self.width
            curCell.y = (curCell.y + curCell.yVelocity) % self.height
            if (curCell.x < 0):
                curCell.x += self.width
            if (curCell.y < 0):
                curCell.y += self.height
            self.listOfPositions[cell] = (curCell.x, curCell.y)

        # Code to check for collisions
        # Cells reverse velocity upon collision
        for i in range(len(self.listOfCells)):
            curCell = self.listOfCells[i]
            for j in range(i+1, len(self.listOfCells)):
                nextCell = self.listOfCells[j]
                dist = np.sqrt((curCell.x - nextCell.x)**2 + (curCell.y - nextCell.y)**2)
                if dist < (curCell.radius + nextCell.radius):
                    curCell.xVelocity = -1 * curCell.xVelocity
                    curCell.yVelocity = -1 * curCell.yVelocity
                    nextCell.xVelocity = -1 * nextCell.xVelocity
                    nextCell.yVelocity = -1 * nextCell.yVelocity
        
class Cell:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y
        self.xVelocity = random.randint(-2, 2) 
        while (self.xVelocity == 0):
            self.xVelocity = random.randint(-2, 2)
        self.yVelocity = random.randint(-2, 2) 
        while (self.yVelocity == 0):
            self.yVelocity = random.randint(-2, 2)
    

def main():
    # Create a new Grid class instance by specifiying number of cells
    # Call some type of a "Draw" function on this grid object, which will cause it to be drawn to the screen
    grid_size = 100
    g = Grid(grid_size)
    g.populateGridWithCells()

    plt.ion()
    fig, ax = plt.subplots()

    x = [val[0] for val in g.listOfPositions]
    y = [val[1] for val in g.listOfPositions]

    sc = ax.scatter(x,y)

    plt.xlim(0,grid_size)
    plt.ylim(0,grid_size)

    plt.draw()

    while(True):
        g.updateAllCellPositions()
        x = [val[0] for val in g.listOfPositions]
        y = [val[1] for val in g.listOfPositions]
        sc.set_offsets(np.c_[x,y])
        fig.canvas.draw_idle()
        plt.pause(0.1)

    plt.waitforbuttonpress()


main()