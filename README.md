# Overview

Mathematical modeling is....

## Task 1: Populating a grid with cells

To begin the cell simulation process, the foundation of the model must be programmed first. In this case, populating a grid with cells should be the first task.

### i. Import Python plotting libraries
The following import statements must be coded to access the Python plotting library, to generate random values, and to store data values.
```Python
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib
import random
import numpy as np
```

### ii. Construct a Grid class
The Grid class contains a constructor to initialize a grid object. The parameter passed into the constructor is the number of cells populated on the grid. The height and width of the grid is hardcoded as well as lists containing cell objects and cell positions.
```Python
class Grid:
    def __init__ (self, numCells):
        self.height = 100
        self.width = 100
        self.numCells = numCells
        self.listOfCells = []
        self.listOfPositions = []
```
        
### iii. Create a function to populate cells on the grid
The populateGridWithCells() function generates a random X and Y valules for each cell. After generating a random position for a cell, the function traverses through the positions of each cell in listOfPositions to check for cells with the same position. If there is a cell with the same position, the function generates a new position for the current cell and adds the position to listOfPositions.
```Python
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
```

### iv. Construct a cell class
The Cell class contains a constructor to initialize a cell object. The parameters passed into the class are the postions of the cells as well as the radius.
```Python
class Cell:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y
```

## Task 2: Moving around the cells
After creating a grid with cells, adding velocities to each cell is the next step...

### i. Update Cell class to generate velocities
(add some commentary)
```Python
class Cell:
        ...
        self.xVelocity = random.randint(-2, 2) 
        while (self.xVelocity == 0):
            self.xVelocity = random.randint(-2, 2)
        self.yVelocity = random.randint(-2, 2) 
        while (self.yVelocity == 0):
            self.yVelocity = random.randint(-2, 2)
```
### ii. Update Grid class to compute new cell positions
(add some commentary)
```Python
class Grid:
    ...
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
```
## Task 3: Controlling collisions

(add commentary)
Finally, the last task is to accurately represent the simulation of cells by avoiding cells overlapping with each other...

### i. Update Grid class to control collision amongst moving cells
```Python
class Grid:
        ...
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

```

**Bold** and _Italic_ and `Code` text

To start this task, a cell class must be created to create an instance for each cell and a grid class must be created to store a dictionary with a list of the cells. When initializing a cell object, the attributes that need to be defined are radius, x position, and y position.
