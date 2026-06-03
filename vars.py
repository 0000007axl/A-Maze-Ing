import shutil
import random
import maze_utils

COLUMNS = shutil.get_terminal_size().columns
ROWS = shutil.get_terminal_size().lines

WALL_COLOR: str = random.choice(["\033[38;5;104m",
                                 "\033[38;5;110m",
                                 "\033[38;5;74m"])

OPPOSITES: dict[str, str] = {"n": "s",
                             "s": "n",
                             "e": "w",
                             "w": "e"}

PATTERN: list[list[int]] = [[0, 0, 1, 0, 0, 1, 1, 0],
                            [0, 1, 1, 0, 1, 0, 0, 1],
                            [1, 0, 1, 0, 0, 0, 1, 0],
                            [1, 1, 1, 1, 0, 1, 0, 0],
                            [0, 0, 1, 0, 1, 1, 1, 1]]


WIDTH, HEIGHT = maze_utils.get_dimensions()


MIN_WIDTH: int = len(PATTERN[0]) + 2
MIN_HEIGHT: int = len(PATTERN) + 2

START_POINT = (COLUMNS//2) - (WIDTH * 2)
