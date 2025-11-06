import random # Importing the random module to generate random numbers

# Define a function (a reusable block of code) for the number guessing game
def number_guessing_game(): #This is a function declaration
    print("Welcome to the Number Guessing Game!") # This just prints some welcome text in the terminal 
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100) # generates a random number between 1 and 100 
    attempts = 0 # this variable will keep track of how many attempts the user has made

    #" while True" creates an infinite loop that will keep running until we break out of it
    while True:  
        guess = input("Take a guess:") # Ask the player to type a guess and store their input in the variable "guess"

        # Check if the input is NOT a number (like if they typed letters or symbols)
        if not guess.isdigit(): 
            print("Please guess a valid number.") #Tell them to enter a valid number
            continue #  "continue" skips the rest of the loop and goes back to the start to ask for input again

        guess = int(guess) #convert the input (which is text) into an integer (a whole number)
        attempts += 1 # Add 1 to the attempts variable each time the player makes a guess
        
        # Compare the player's guess to the secret number
        if guess < secret_number: 
            print("Too low! Try again.") # If guess is smaller, hint to go higher
        # "elif" means "else if" - this only runs if the first "if" was false
        elif guess > secret_number:
            print("Too high! Try again.") # If guess is bigger, hint to go lower
        
        # "else" runs if none of the above "if" or "elif" conditions were true
        # In this case, it means the guess must be correct
        else:
            print(f"Yout got it! The number was {secret_number}.")
            print(f"It took you {attempts} attempts to guess the number.")
            break # "break" exits the loop since the game is over

# This part runs only if the file is executed directly (not imported by another file)
if __name__ == "__main__":
    number_guessing_game() # Call (run) the function to start the game