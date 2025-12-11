# acsavage-evcc_STEM_103_final
# Virtual Elevator

Andrew Savage
12/10/25
STEM 103

# Description

This program is an elevator simulator written in Python. The user starts on the 1st floor and is asked what floor they want to travel to. A random integer is generated to represent other passengers; the elevator capacity may be reached if there are too many people. Functions are used extensively to loop user input statements and handle invalid input, such as putting functions within functions to run endlessly until valid input is detected. While loops and try/except blocks are also used to handle user input. A for loop is used to simulate elevator travel, displaying ascending floor numbers as if inside an actual elevator.

To test the functionality of this program I input integers, floats, letters and other characters a user might type. Using if/else statements, try/except blocks and functions plugged into themselves, I was able to have the program handle user input errors without crashing and loop input prompts endlessly if needed. 

Overall I learned that every time I added a feature it would need to be tested and that the code added made sense in context of the flow of the rest of the program. For example, when adding the randomly generated passengers, the function to take elevator or stairs had to be placed directly after so the user could make an informed decision depending on the number of people already waiting. Initially, that function was placed before the random number generator. 

Random and try/except were the new things I learned for this project. Random.randint was used to generate a random integer within a range and try/except was used for input error handling. Testing for input errors was the biggest challenge I faced and spent the most project time on. Logical order of the code was also another challenge; even if the code worked it sometimes didn't make sense and some blocks or functions had to be moved around. 