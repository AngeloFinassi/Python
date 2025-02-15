import argparse
from random import randint

def Challenge(name, range):
    pl_name = name
    pc_wins = 0
    pl_wins = 0

    def GuessNumber_Game():
        nonlocal pl_name, pc_wins, pl_wins, range
        win_var = 3

        chose_number = randint(0, range)
        p_chose_number = int(input(f"Write a number between 0 and {range}: "))

        #Some normal mistake
        if p_chose_number > range or p_chose_number < 0:
            p_chose_number = int(input(f"Please a number in the corrent interval (0 to {range}): "))

        #Game
        if pc_wins < win_var and pl_wins < win_var:
            if p_chose_number == chose_number:
                print("\nUhu, you win!")
                pl_wins += 1
            else:
                print(f"\nNah, you lose! The Machine chose {chose_number}.")
                pc_wins += 1

            print("\nSCOREBOARD:")
            print(f"Python Points: {pc_wins}\nPlayer Points: {pl_wins}\n")

        #If the game and
        if pc_wins == win_var:
            print(f"\nHum... Sorry, it wasn't this time ;-; The Machine chose {chose_number}!")
            print(f"\nFinal Score - Python: {pc_wins} | Player: {pl_wins}")
            return

        elif pl_wins == win_var:
            print(f"\nCongratulations! You win! The number was: {chose_number}")
            print(f"\nFinal Score - Python: {pc_wins} | Player: {pl_wins}")
            return

    return GuessNumber_Game

#arguments to give the informaiton to the game
parser = argparse.ArgumentParser(
    description="Play a Game"
)

parser.add_argument(
    '-n', '--name', metavar = 'name', required=True, help="The name of the player"
)

parser.add_argument(
    '-r', '--range', metavar='range', required=True, help='Give the Range of the "Guess the Number Game"'
)

game_info = parser.parse_args()
play = Challenge(game_info.name, int(game_info.range))

#loop that run the game
while True:
    play()
    stop = input("\nDo you want to continue? (Y/N): ").strip().lower()
    if stop not in ['y', 'yes', 'Y', 'YES']:
        print("\nThanks for playing!")
        break
