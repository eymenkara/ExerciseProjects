import random




game_on = True

while game_on:
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    else:
        print("Wrong input...")
        lives = 0

    found = False
    while lives > 0 and not found:
        print(f"You have {lives} attempts remaining.")
        guess = int(input("Make a guess: "))

        if guess < number:
            print("Too low.")
            print("Guess again")
            lives -= 1
        elif guess > number:
            print("Too high.")
            print("Guess again")
            lives -= 1
        else:
            print(f"You got it! Answer was {number}." )
            found = True

    if not found:
        print("You Lost!")
    else:
        print("You Won!")

    again = input("Wanna play again? Type 'y' or 'n': ")
    if again == "n":
        game_on = False
