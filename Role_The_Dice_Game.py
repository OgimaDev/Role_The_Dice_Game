#import random function
import random

# intro message for dice game
print("-----------------------------------------------------------")
print("- Hello and Welcome to The Dice Game!                     -")
print("- Computer will roll two dice values and display to user  -")
print("- User can then enter either options from below:          -")
print("- Enter 'yes' or 'y' to roll again                        -")
print("- or                                                      -")
print("- Enter 'no' 'n' or any other character to stop rolling   -")

# set dice low number and high number (1+6 = 1-6)
dice_min = 1
dice_max = 6

# ask user if they wanna roll again if yes start loop
keep_rolling_dice = "yes"

# while loop to roll dice and continue rolling if user desires
while keep_rolling_dice == "yes" or keep_rolling_dice == "y":

    # print game message showing dice being tossed
    print("-----------------------------------------------------------")
    print("- ** Rolling the Dice Now                              ** -")
    print("- ** Tossed two dice on the board                      ** -")
    print("- ** The dice rolled are                               ** -")
    print("-----------------------------------------------------------")

    # use random to select a value from 1-6 for first dice and assign to dice_roll_one
    dice_roll_one = str(random.randint(dice_min, dice_max))

    # use random to select a value from 1-6 for first dice and assign to dice_roll_two
    dice_roll_two = str(random.randint(dice_min, dice_max))

    # print dice values
    print("------------------  Dice 01  |  Dice 02  ------------------")
    print("-----------------------------------------------------------")
    print("------------------           |           ------------------")
    print("------------------    #####  |  #####    ------------------")
    print("------------------    # " + dice_roll_one + " #  |  # " + dice_roll_two + " #    ------------------")
    print("------------------    #####  |  #####    ------------------")
    print("------------------           |           ------------------")
    print("-----------------------------------------------------------")

    # ask user if they wanna continue rolling dice, is yes then toss more dice. if no or other input, end dice toss
    keep_rolling_dice = input("- Roll the Dices Again or Quit?                           -\n-----------------------------------------------------------\n- > ")

