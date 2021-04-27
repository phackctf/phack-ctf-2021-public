# Modified version of Jack92829 implementation
# https://github.com/Jack92829/Maze-Generation

import random

WALL = '#'
PATH = ' '
USER = 'x'
GOAL = '$'

UP    = '↑'
DOWN  = '↓'
LEFT  = '←'
RIGHT = '→'

# -- Cell class that defines each walkable Cell on the grid
class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = [True, True, True, True] # Left, Right, Up, Down

    # -- Check if the Cell has any surrounding unvisited Cells that are walkable
    def getChildren(self, grid: list) -> list:
        a = [(1, 0), (-1,0), (0, 1), (0, -1)]
        children = []
        for x, y in a:
            if self.x+x in [len(grid), -1] or self.y+y in [-1, len(grid)]:
                continue
            
            child = grid[self.y+y][self.x+x]
            if child.visited:
                continue
            children.append(child)
        return children

# -- A maze game
class Maze:
    def __init__(self, size: int):
        self.size = size
        self.grid = [[Cell(x, y) for x in range(size)] for y in range(size)]
        self.position = self.grid[0][0]
        self.stack = []

        self.generate()

    # -- Generate random maze
    def generate(self):
        while True:
            self.position.visited = True
            children = self.position.getChildren(self.grid)

            if children:
                choice = random.choice(children)
                choice.visited = True

                self.stack.append(self.position)
                self.removeWalls(choice)
                self.position = choice
            
            elif self.stack:
                self.position = self.stack.pop()

            else:
                break

    # -- Check if given solution is correct
    def solve(self, path):
        x = 1
        y = 1

        binGrid = [ list(x) for x in self.buildAsciiMaze(True).split('\n') ]

        for p in path:
            if p == LEFT and binGrid[x][y-1] in [PATH, GOAL]:
                y -= 1
            elif p == RIGHT and binGrid[x][y+1] in [PATH, GOAL]:
                y += 1
            elif p == UP and binGrid[x-1][y] in [PATH, GOAL]:
                x -= 1
            elif p == DOWN and binGrid[x+1][y] in [PATH, GOAL]:
                x += 1
            else:
                return False

        if binGrid[x][y] == GOAL:
            return True

        return False

    # -- Remove wall between current cell and specific children
    def removeWalls(self, choice: Cell):
        if choice.x > self.position.x:     
            self.position.walls[1] = False
            choice.walls[0] = False
        elif choice.x < self.position.x:
            self.position.walls[0] = False
            choice.walls[1] = False
        elif choice.y > self.position.y:
            self.position.walls[3] = False
            choice.walls[2] = False
        elif choice.y < self.position.y:
            self.position.walls[2] = False
            choice.walls[3] = False

    # -- Draw walls ASCII way
    def drawWalls(self, binGrid: list) -> list:
        for yindex, y in enumerate(self.grid):
            for xindex, x in enumerate(y):
                for i, w in enumerate(x.walls):
                    if i == 0 and w:
                        binGrid[yindex*2+1][xindex*2] = WALL
                    if i == 1 and w:
                        binGrid[yindex*2+1][xindex*2+2] = WALL
                    if i == 2 and w:
                        binGrid[yindex*2][xindex*2+1] = WALL
                    if i == 3 and w:
                        binGrid[yindex*2+2][xindex*2+1] = WALL
        return binGrid

    # -- Draw a border around the maze
    # Might be useless
    def drawBorder(self, grid: list) -> list:
        length = len(grid)
        for row in grid:
            row[0] = row[length-1] = WALL
            
        grid[0] = grid[length-1] = [WALL] * length
        return grid

    # -- Add user and goal on the ASCII map
    def addGoal(self, grid: list) -> list:
        grid[len(grid) - 2][len(grid) - 2] = GOAL
        grid[1][1] = USER
        return grid

    # -- Build ASCII map
    def buildAsciiMaze(self, pretty=False):
        binGrid = []
        length = len(self.grid) * 2 + 1
        for x in range(length):
            if x % 2 == 0:
                binGrid.append([PATH if x % 2 != 0 else WALL for x in range(length)])
            else:
                binGrid.append([PATH] * length)

        binGrid = self.drawWalls(binGrid)
        binGrid = self.drawBorder(binGrid)
        binGrid = self.addGoal(binGrid)

        EOL = '\n' if pretty else ''
        
        return EOL.join([''.join(x) for x in binGrid])
