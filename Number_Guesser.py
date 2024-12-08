import random

# Prompt a user to set the range
top_of_range=input("Type a number: ")

# Validate if input is positive integer
if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

# Generate a randome number within the specific range
random_number= random.randint(0, top_of_range)
guesses= 0

#Start the guesing game loop
while True:
    guesses +=1
    user_guess=input("Make a guess: ") #prompt the user for a guess
    
    # Validate if the guess is a digit
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    #check if the user's guess is correct
    if user_guess==random_number:
        print("You got it right")
        break
    elif user_guess> random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")

