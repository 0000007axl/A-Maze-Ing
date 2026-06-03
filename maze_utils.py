import vars
import subprocess
import time

def get_dimensions():
    while True:
        try:
            print("\n" * (vars.LINES // 2))
            for char in "Enter maze's width: ":
                print(char, end="", flush=True)
                time.sleep(0.1)
            w = int(input())
            for char in "Enter maze's height: ":
                print(char, end="", flush=True)
                time.sleep(0.1)
            h = int(input())
            if not (1 <= h <= vars.COLUMNS // 6 or 1 <= w <= vars.LINES//6):
               raise ValueError()
            return w, h
        except ValueError:
            invalid_value_message: str = "Please input a valid number, don't be stupid."
            subprocess.run(["clear"])
            print("\n"*4, (invalid_value_message).center(vars.COLUMNS))
            continue

