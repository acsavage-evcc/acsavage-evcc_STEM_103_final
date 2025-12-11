import time
from functions import *
import random

print("Initializing Virtual Elevator v1.0...") # program introduction
time.sleep(2) # "loading" 

ppl_wait_elev = random.randint(0, 25) # randomly generate a number representing people waiting for elevator
elev_capacity = (15) # elevator capacity
txt = "{} people are waiting for the elevator." # store string in variable, {} is a placeholder
print(txt.format(ppl_wait_elev)) # print txt string variable with format method to put ppl_wait_elev value in line 10 placeholder

elevator_or_stairs() # run function asking user to take elevator or stairs

if ppl_wait_elev >= elev_capacity: # evaluate if there are more people waiting than the elevator can hold, not including user
    print("Unfortunately, the elevator is over-capacity, you'll have to take the stairs. =(") # tell user they cannot use elevator
    exit() # exit program automatically
else:
    floor_choice_loop() # run floor choice function if elevator capacity was not reached

print("You have reached your floor.") # tell user they've reached desired floor, ending program