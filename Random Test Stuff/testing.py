import logging
import math
import sys
import pygame

sys.set_int_max_str_digits(9999999)

DEBUG_MODE = True
if(DEBUG_MODE):
    logging.basicConfig(level=logging.DEBUG, format="{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M", filename="app.log", encoding="utf-8", filemode="a")
else:
    logging.basicConfig(format="{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M", filename="app.log", encoding="utf-8", filemode="a")

check_for_nth = int(input("Which position in the sequence do you want?\n"))

prev_x = 1
this_x = 1
next_x = 1
n = 1
while(check_for_nth != n): 
    next_x = prev_x + this_x
    n+=1
    #logging.debug(f"Current values: {prev_x} + {this_x} = {next_x}. n={n}")
    prev_x = this_x
    this_x = next_x
    if(n % 1000 == 0):
        print(f"Currently at {n}/{check_for_nth}")
print(f"{n}th position is {next_x}")