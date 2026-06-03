import vars
import maze_utils
import maze_gen
import display
import subprocess


def main() -> None:
    subprocess.run(["clear"])
    vars.WIDTH, vars.HEIGHT = maze_utils.get_dimensions()
    display.print_title()
    maze_g: maze_gen.MazeGenerator = maze_gen.MazeGenerator()
    maze = maze_g.generate(vars.WIDTH, vars.HEIGHT)
    display.display_maze(maze)

main()
