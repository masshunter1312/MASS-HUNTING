import os
import random
import time

def display_track(player_pos, computer_pos, track_length):
    print('Race Start!\n' + '-' * track_length)
    print(' ' * player_pos + 'P')
    print(' ' * computer_pos + 'C')
    print('-' * track_length + ' Finish Line')

def racing_game():
    player_pos = 0
    computer_pos = 0
    track_length = 30

    while True:
        os.system('clear')
        display_track(player_pos, computer_pos, track_length)

        if player_pos == track_length:
            print("Player Wins!")
            break
        elif computer_pos == track_length:
            print("Computer Wins!")
            break

        input("Press any key to run!")
        player_pos += random.randint(1, 3)
        computer_pos += random.randint(1, 3)

        time.sleep(0.5)

racing_game()
    
