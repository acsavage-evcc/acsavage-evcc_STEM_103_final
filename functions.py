import time

def elevator_or_stairs(): # function letting user decide to take elevator or stairs
    arrival_choice = input("Do you want to take the elevator or the stairs? Type 'e' or 's': ") # ask user for choice
    if arrival_choice == "e": # if user types "e" they will take elevator
        print('You have decided to take the elevator.')
    elif arrival_choice == 's': # if user types "s" they will take stairs
        print('You have decided to take the stairs.')
        exit() # program exits automatically
    else: 
        print("Invalid input") # if anything other than 'e' or 's' are typed user will be informed of bad input
        elevator_or_stairs() # starts function over after bad input detected

def floor_choice_loop(): # function for elevator floor choice and travel
    floors = [1, 2, 3, 4, 5] # list containing all floors 
    y = True # set bool condition for while loop to run
    while y == True: # while loop runs if bool is true
        floor_choice = input("There are 5 floors. What floor do you need to go to? ") # ask user for desired floor
        try: # try block evaluates floor_choice for integer input
            floor_choice = int(floor_choice) # cast floor_choice input as integer
            y = False # set y bool to false, break out of while loop
        except: # handle error if floor_choice input was not a integer
            print("Invalid input. Type a floor number between 2 - 5.") # tell user their input was invalid, run while loop again
    if floor_choice > 1 and floor_choice <= 5: # evaluate if floor number input was greater than 1 and less than or equal to 5
        print("You push the button for your floor.") 
        time.sleep(1)
        print("The elevator door closes.")
        time.sleep(1) # simulate pushing floor button and door closing ^^^
        for x in floors: # iterate through 'floors' list values
            if x > floor_choice: break # stop for loop once iteration goes above floor_choice value
            print(x) # print each iteration of 'floors' list up to user's desired floor
            time.sleep(1) # simulate elevator travel time
    elif floor_choice == 1: # if user typed floor number 1 
        print("You are already on the first floor.") 
        floor_choice_loop() # run function again
    else: # handle non-integer character input
        print("Invalid input. Type a floor number between 2 - 5.")
        floor_choice_loop() # run function again