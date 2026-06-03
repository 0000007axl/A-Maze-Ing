import vars
import maze_utils
import maze_gen
import display
import subprocess
import time


def welcome_screen():
    subprocess.run(["clear"])
    for char in "\n\nHello":
        print(char, end="", flush=True)
        time.sleep(0.1)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    time.sleep(1)
    vars.WIDTH, vars.HEIGHT = maze_utils.get_dimensions()
    subprocess.run(["clear"])


def main() -> None:
    welcome_screen()
    display.print_title()
    maze_g: maze_gen.MazeGenerator = maze_gen.MazeGenerator()
    maze = maze_g.generate(vars.WIDTH, vars.HEIGHT)
    display.display_maze(maze)

main()
