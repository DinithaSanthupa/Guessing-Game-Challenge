import random

#---------------Global varibles---------------#

#global varible turn for count how many guesses
turn = 0

#global list varible for store input numbers of player
guess_number_list = []

def guess(x):
    global turn
    global guess_number_list

    # genarate random number for game
    random_number = random.randint(1, x)

    #local varible for assign input number of a turn
    guess = 0

    while guess != random_number:

        #try except for bypass invalid user inputs
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess <0 or guess > 100:
                print("out of bounds")
            else:
                turn = turn +1
                guess_number_list.append(guess)

                #first turn
                if turn == 1 and abs(guess - random_number) <= 10:
                    print("WARM")
                elif turn == 1 and abs(guess - random_number) > 10:
                    print("COLD")

                #after first turn
                if turn>1 and guess == guess_number_list[turn-2]:
                    print(f"Input new guess number, You alredy input {guess} in prevoius turn")
                    turn = turn -1
                    guess_number_list.remove(guess)
                else:
                    if turn >1 and abs(guess_number_list[turn-1]-random_number) > abs(guess_number_list[turn-2]-random_number):
                        print("COOLER")
                    elif turn >1 and abs(guess_number_list[turn-1]-random_number) == abs(guess_number_list[turn-2]-random_number):
                        if guess_number_list[turn-1] > guess_number_list[turn-2]:
                            print("COOLER")
                        else:
                            print("WARM")
                    elif turn >1 and abs(guess_number_list[turn-1]-random_number) < abs(guess_number_list[turn-2]-random_number):
                        if guess == random_number:
                            break
                        print("WARMER")

                    
        except:       
            print("Please input valid number ")

    # User output with result
    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')
    print(f"You took {turn} guesses it took")

guess(100)