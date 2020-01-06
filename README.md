# Overview

Mathematical models are effective tools that are used to simulate real world scenarios to develop a better understanding of what occurs in situtations that cannot be modeled in real life. By using mathematical models, various factors can be manipulated to reveal the behavior of a system in response to any variable, making these conceptual models reliable tools when investigating certain real world behaviors. 

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
After creating a grid with cells, adding velocities to each cell and updating its position is the next step. 

### i. Update Cell class to generate velocities
Within the Cell class, random values for each X and Y component for the cell's velocity is generated. To prevent the cell from moving in a straight line - either vertical or horizontal - the regenerates a random value for the velocity component if either one of the components for the cell is 0.
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
Within the Grid class, the updateAllCellPositions() function adds each component of the cell's velocity to the corresponding coordinate of the cell and then updates listOfPositions with the new position of each cell.
```Python
class Grid:
    ...
    def updateAllCellPositions(self):
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
The final task is to accurately represent the simulation of cells by preventing cells from overlapping with each other once they come into contact with each other.

### i. Update Grid class to control collision amongst moving cells
Since a collision between two cells happens when they are in contact with each other, the distance between the centers of the two cells would be the combined length of the radii of the cells. The following code checks for when the distance between any two cells is each to the combined radii length of the cells and then changes each component of the cell's velocity to be negative. This way, the cells will appear as if they bounce off of each other.
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
## Final Program:
The following code includes the Grid and Cell classes as well as the main method which calls the necessary functions and creates instances of the two classes.
```Python
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib
import random
import numpy as np

class Grid:
    def __init__ (self, numCells):
        self.height = 100
        self.width = 100
        self.numCells = numCells
        self.listOfCells = []
        self.listOfPositions = []

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
```

<iframe src="https://giphy.com/embed/TdWhk2AyBspEbJgYEK" width="480" height="384" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/TdWhk2AyBspEbJgYEK">via GIPHY</a></p>
