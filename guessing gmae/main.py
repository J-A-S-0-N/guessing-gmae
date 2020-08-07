from os import system
from time import sleep
import sys
import random

chr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u" ,"v" ,"w" ,"x" ,"y", "z"]

def main():
    while True:
        print("guess an word from a to z")
        inp = input(">>> ")
        g = random.randint(0,26)
        guess = chr[g]
        if guess == inp:
            system("cls")
            print("nice")
            sleep(2)
            sys.exit()
        else:
            print("try agin")
            sleep(0.5)
            system("cls")
        

if __name__ == "__main__":
    main()