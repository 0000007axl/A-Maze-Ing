import vars
import subprocess


def get_dimensions():
    while True:
        try:
            w = int(input("Enter maze's width: "))
            h = int(input("Enter maze's height: "))
            if not (1 <= h <= vars.COLUMNS // 6 or 1 <= w <= vars.ROWS//6):
               raise ValueError()
            return w, h
        except ValueError:
            invalid_value_message: str = "Please input a valid number, don't be stupid."
            subprocess.run(["clear"])
            print("\n"*4, (invalid_value_message).center(vars.COLUMNS))
            continue

