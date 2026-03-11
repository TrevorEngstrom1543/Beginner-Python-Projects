import random

#Creates a variable named secret that chooses a random integer between 1 and 100
secret = random.randint(1, 100)

#Creates a variable for attempts and sets the initial value to 0
attempts = 0

#Prints starting text into console
print("I'm thinking of a number between 1 and 100. Please type a number to begin.")

while True:
    #Converts string text into an integer that the program understands.
    guess = int(input("Your Guess:"))

    #Increases the value of attempts variable after each guess
    attempts += 1

    if guess < secret:
        print("Your guess is too low, chud.")
    elif guess > secret:
        print("Your guess is too high. You're lowkirkenuinly worse than Epstein")
    else:
        #This has an f string, it allows for you to put a variable into your string text. In this instance, it's for attempts.
        print(f"Correct, you were blessed by Netanyahu after {attempts} attempts.")