import random


def Rock_Paper_Scissors():
    print(" ")
    print("***************")
    print(" ")

    print("Let's play Rock, Paper, Scissors!")

    i = random.randint(1, 3)
    play = i

    print(play)

    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    print(" ")
    print("***************")
    print(" ")

    guess = int(input(
        "Choose a number above to throw Rock, Paper, or Scissors. See if you can beat me. One, two, three—GO! "))

    if guess == play:
        print("It's a TIE! ")

    elif guess == 1 and play != 1:
        if play == 2:
            print("I threw a PAPER. Paper covers Rock. I win! ")
        else:
            print("I threw SCISSORS. Rock breaks Scissors. You win! ")

    elif guess == 2 and play != 2:
        if play == 1:
            print("I threw a ROCK! Paper covers Rock. You win! ")
        else:
            print("I threw SCISSORS. Scissors cut Paper. I win! ")

    elif guess == 3 and play != 3:
        if play == 1:
            print("I threw a ROCK! Rock breaks Scissors. I win! ")
        else:
            print("I threw PAPER. Scissors cuts Paper. You win! ")

    # else:
    #    print("Ooops! Something went wrong! ")

    print(" ")
    print("***************")
    print(" ")

    answer = input("Want to play again? Y or N? ")

    if answer == "Y" or answer == "y":
        print(" ")
        print("Great! Here we go!")
        Rock_Paper_Scissors()

    else:
        print("Thank you for playing! See you next time!")


Rock_Paper_Scissors()
