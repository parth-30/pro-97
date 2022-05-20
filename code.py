import random

print("Number guessing game")

number = random.randint(1, 9)

chances = 0

print("Guess a number (between 1 and 9):")


while chances < 5:

    
    guess = int(input("Enter your guess:- "))

    

    if guess == number:
  
        print("Congratulation YOU WON!!!")
        break
    
    elif guess < number: 

        print("your guess is too low", guess)

    else: 
        print("guess is too high", guess)

        # Increase the value of chance by 1
    chances += 1


# Check whether the user guessed the correct number
if not chances < 5:
    print("YOU LOSE!!! The number is", number)