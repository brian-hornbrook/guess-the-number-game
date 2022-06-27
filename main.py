import random

correct_guess = False
random_number = random.randrange(100)

while not correct_guess:
    user_input = input("Guess a number between 0 and 100: ")
    print("")

    try:
        user_number = int(user_input)

        if (random_number > user_number):
            print("your guess is too low")

        elif (random_number < user_number):
            print("your guess is too hight")

        elif (random_number == user_number):
            print("You guessed the right number!")
            correct_guess = True

    except:
        print("you must type only numbers")
