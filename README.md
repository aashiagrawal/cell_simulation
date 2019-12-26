## Overview

Mathematical modeling is....

### Task 1: Populating a grid with cells

To begin the cell simulation process, the foundation of the model must be programmed first. In this case, populating a grid with cells should be the first task. To start this task, a cell class must be created to create an instance for each cell and a grid class must be created to store a dictionary with a list of the cells. When initializing a cell object, the attributes that need to be defined are radius, x position, and y position.

```markdown
rom matplotlib import pyplot as plt
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
    

    def getNumCells(self):
        return self.numCells

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
class Cell:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y
```
### Task 2: Moving around the cells
```markdown

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/aashiagrawal/cell_simulation/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
