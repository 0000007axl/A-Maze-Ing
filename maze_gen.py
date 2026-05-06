import random

WIDTH: int = 20
HEIGHT: int = 12


OPPOSITES: dict[str, str] = {"n":"s",
                             "s":"n",
                             "e":"w",
                             "w":"e"}


PATTERN: list[list[int]] = [[0,1,0,0,0,1,1,0],
                            [0,1,0,0,0,0,0,1],
                            [0,1,0,1,0,1,1,0],
                            [0,1,1,1,0,1,0,0],
                            [0,0,0,1,0,1,1,1]]
#center of the 42 pattern is [y=2, x=4]


MIN_WIDTH: int = len(PATTERN[0]) + 2
MIN_HEIGHT: int = len(PATTERN) + 2

#-------------------

class Cell():
    def __init__(self) -> None:
        self.walls = {"n" : 1,
                      "s" : 1,
                      "e" : 1,
                      "w" : 1}
        self.is_checked: int = 0
        self.is_pattern: int = 0

#------------------

def display_maze(maze: list[list[Cell]]):
    height: int = len(maze)
    width: int = len(maze[0])

    for y in range(height):
        for x in range(width):
            print("+", end="")
            if maze[y][x].walls["n"] == 1:
                print("---", end="")
            else:
                print("   ", end="")
        print("+")

        for x in range(width):
            if maze[y][x].walls["w"] == 1:
                if maze[y][x].is_pattern == 1:
                    print("| # ", end="")
                else:
                    print("|   ", end="")
            else:
                print("    ", end="")
        print("|")

    for x in range(width):
        print("+", end="")
        if maze[height - 1][x].walls["s"] == 1:
            print("---", end="")
        else:
            print("   ", end="")
    print("+")

#--------------------

class MazeGenerator():
    def __init__ (self) -> None:
        self.width = WIDTH
        self.height = HEIGHT


    def apply_pattern(self,
                      maze: list[list[Cell]]) -> None:
        oy: int = (len(maze) - len(PATTERN)) // 2
        ox: int = (len(maze[0]) - len(PATTERN[0])) // 2
        for py in range(len(PATTERN)):
            for px in range(len(PATTERN[0])):
                if PATTERN[py][px] == 1:
                    maze[oy + py][ox + px].is_pattern = 1 


    def generate(self,
                 width: int,
                 height: int) -> list[list[Cell]]:
        maze: list[list[Cell]] = []

        for _ in range(height):
            row: list[Cell] = []
            for _ in range(width):
                cell: Cell = Cell()
                row.append(cell)
            maze.append(row)
        self.apply_pattern(maze)
        display_maze(maze)
        return (maze)
            
#----------------------
def main() -> None:
    maze_gen: MazeGenerator = MazeGenerator()
    maze: list[list[Cell]] = maze_gen.generate(WIDTH, HEIGHT)

if __name__ == "__main__":
    main()
