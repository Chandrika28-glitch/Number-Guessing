import random
#defined a function
def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    #using loop to check whether the given input is valid or not
    while True:
        # Ask the user for their guess
        user_guess = input("Guess a number: ")
        
        # Check if the input is a valid number
        #exception handling whether user enter any 0 or anything
        #try block
        try:
            user_guess = int(user_guess)
            #except block
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        # Increment the number of attempts
        attempts=attempts+1 <10
        
        # Check if the guess is correct
        if user_guess == number_to_guess:
            print(f"Congratulations! You found the number in {attempts} attempts.")
            break
        #giving clew to the user if the no is small
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
         #giving clew to the user if  the no is large   
        else:
            print("Too high! Try again.")

#calling the number _guessing _game() function
if __name__ == "__main__":
    number_guessing_game()

