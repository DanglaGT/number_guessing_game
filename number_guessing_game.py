
from random import randint

scores = []
min_num = 1
max_num = 100
rand_num = randint(min_num, max_num)
response = "Y"
restart = "N"
i = 0
games = 0

print("")
print("-----------------------------------------------------------------")

intro = """I have selected a random integer between 1 and 100.
See how many attempts it takes you to guess it correctly."""
print(intro)

print("-----------------------------------------------------------------")

while response == "Y" or restart == "Y":

    # i = i + 1
    i += 1
    bad_input = 1

    while bad_input == 1:
        guess_raw = input("Enter guess > ")
        try:
            guess = int(guess_raw)
        except ValueError:
            print("That is not an integer! Try again!")
        except:
            bad_input = 0

    if guess == rand_num:
        print("")
        if i == 1:
            congrats = ("Wow, you guessed it on your first try. You "
            "should go buy a lottery ticket!!!")
            print(congrats)

        else:
            congrats = ("Good job, you guessed the correct number "
            "in %s tries.")
            print(congrats % str(i))

        print("")

        scores.append(i)
        times_played = len(scores)
        restart = input("Do you want to play again? (Y/N) > ")
        restart = restart.strip().upper()

        if restart == "Y":
            rand_num = randint(min_num,max_num)
            i = 0
        else:
            if len(scores) == 1:
                print("\nThanks for playing. You played " + str(len(scores)) + " time.\n")

            else:
                average = sum(scores)/len(scores)
                print("\nThanks for playing. You played " + str(len(scores)) + " times.")
                print("You averaged " + str(average) + " guesses.\n")
                print("Here is a summary of your games:\n")

                for score in scores:
                    games += 1
                    print("\tGame " + str(games).strip() + ": " + str(score) + " guesses.")
                print("")

            break

    else:
        if guess > max_num or guess < min_num:
            print("Come on! That is NOT between 1 and 100!!!\n")
        elif guess > rand_num:
            print("Sorry, too high.\n")
        elif guess < rand_num:
            print("Sorry, too low.\n")

        response = input("Do you want to try again? (Y/N) > ")
        response = response.strip().upper()
        print("")
