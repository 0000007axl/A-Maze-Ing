import time

# The cursor goes back to the beginning of the line each loop iteration
i = 0
while True:
    print(f"Countdown: {i}", end="\r")
    i += 1
    time.sleep(1)
