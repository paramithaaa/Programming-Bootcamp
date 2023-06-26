"""
In this code, we are making a game which allows the user to guess a randomly
generated integer between 1 and 100. The user will be able to guess again and
until they get the correct answer. When programming this, it is easier to break down
the tasks the whole program needs to do. There are three main task, which are
generating random integer, asking the user for input, and checking the user's guess.
We split these tasks into functions. We need to import the random library, so we can
use the randint() function from that library.

1. generate_random_int function:
This function does not take any parameter. Its task is to generate random integer from
1 to 100 using the random.randint function. It will return the generated integer.

2. ask_user_input function:
This function does not take any parameter as well. Its task is to ask the user for the
input / guess. Here, we specify some conditions to make the input valid. The first one
is that it should be an integer, and second is it should be between 1 and 100. Hence,
use the try-except to catch a Value Error exception when the user input is not an intger.
It uses a while loop (while True) so it will keep asking for user input until a valid
input is provided. If a Value Error is raised, the code execution jumps to the except 
block and an error message will be shown. If the input is an integer, it will go to the 
next condition in which the input/ guess should be between 1 to 100. If the input statisfies 
with the conditions, it will return the input, otherwise it will print an error message.

3. check_user_guess function:
This function takes two parameters, which are user_guess (which is the guess input from
the user) and answer (which is the correct answer). Here, we use the if-else conditionals 
to check whether the guess is correct, too high or to low. Because there are three conditions 
(correct, too high, and too low), we use three branches. The 'if' statement is the starting 
point. It will compare and check if the guess and the answer is the same. If the condition is 
true, the code in the 'if' statement will be executed. However, when it is false (the guess is 
not the same as answer), it will move on to the 'else if' statement (2nd branch), which check 
if the guess is less than the answer. If it is true, the code inside the 'else if' statement 
will be executed. Here, we use else if because we still have a condition to be checked, and in 
python, 'else if' is written as 'elif'. Lastly, if the previous condition is still false, we only 
have one option left, which is the guess is larger than the answer. Hence, we use 'else' statement 
for it, and so if the two previous conditions are false, the code below the 'else' statement will be 
executed.

4. game function:
The purpose of this function is to compile the game and is the main logic of the game. First, the
program will choose a random number using the generate_random_int function and store it in a variable
called 'answer'. And then, the program will ask the user to guess a number, using the ask_user_input
function, and store it in a variable called user_guess (these two variables will be the parameter)
for the check_user_guess function). Next, it will call the check_user_guess function to check
whether the guess is correct, to high, or too low. The program will tell you whether your answer is
correct, too high, or too low. If it is wrong (too high or too low), the program will allow you to
guess again and again until you get the correct answer. Here, we use the while loop because we do
not have the exact amount of iteration until the loop will stop, as we need to keep on prompting the
plqyer for another guess until the answer is correct. A while loop aloows us to repeat a certain
code as long as a condition is true (here it is user_guess != answer). In that while loop, we keep
on asking user input and check it, and will stop if the guess is correct.
"""


import random #importing the random library for the random.randint()

def generate_random_int(): #function to generate random number
    ans = random.randint(1,100) #using the randint function from the random library
    # the two digits in the bracket shows the range of the integer generated
    return ans

def ask_user_input():
    while True:
        try:
            guess = int(input("Input a number: "))
            if 0 <= guess <= 100: #checking if the guess is between 1 and 100
                return guess
            else:
                print("Your input is invalid. Number should be an integer from 1 to 100.")
        except ValueError: #error will raise if the input is not integer or is not convertible to integer
            print("Please enter a valid number.")

def check_user_guess(user_guess, answer):
    if user_guess == answer: #checking whether it is correct
        print("You guessed the correct number!")
    elif user_guess < answer: #checking if the incorrect guess is lower than the answer
        print("Your guess is too low!")
    else: #checking if the incorrect guess is higher than the answer
        print("Your guess is too high!")

def game():
    answer = generate_random_int() #generating random number
    print("Hello! Welcome to the Secret Number game!")
    print("To start, you need to guess the secret number. The number will be an interger from 1 to 100.")
    print(" ")
    user_guess = ask_user_input() #asking user input
    check_user_guess(user_guess, answer)
    while user_guess != answer: #while loop to keep on asking if the answer is still incorect
        user_guess = ask_user_input()
        check_user_guess(user_guess, answer)
        
game() #calling the game function to execute the game