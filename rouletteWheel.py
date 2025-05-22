import random
from time import sleep

def rouletteRandom():
    wheel = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
    
    # ANSI escape sequences
    CLEAR = "\x1b[2K"
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"

    i = 0
    steps = random.randint(20, 60)  

    for _ in range(steps):

        numColor = ""

        print(HIDE_CURSOR, end="")
        b = 0.8
        sleepTime = 1 / (steps ** b)                    # gradually slows down the display of numbers

        print(wheel[i], end="\r")
        sleep(sleepTime)  
        print(CLEAR, end="")

        i = (i + 1) % len(wheel)
        steps -= 1
    
    # checks if number is black, red or green
    if i == 0:
        numColor = "Green"
    elif i % 2 == 0:
        numColor = "Black"
    else:
        numColor = "Red"

    print(SHOW_CURSOR, end="")    
    print(numColor, wheel[i] )
    return wheel[i]
    

if __name__ == "__main__":
    rouletteRandom()
