from src.game_mood import *
from src.auto_version import *
from src.person_version import *
                                                                                                
if __name__ == '__main__':
    mode = input("Enter the mode of the game (auto/person): ").lower()
    
    if mode == 'auto':
        num_games = 1600
        initial_choice = game_mood(mode)
        switch_rate, no_switch_rate = simulation_game(num_games, initial_choice)
        print(f"Win rate with switching: {switch_rate*100:.2f}%")
        print(f"Win rate without switching: {no_switch_rate*100:.2f}%")
    elif mode == 'person':
        initial_choice = game_mood(mode)
        win = monty_hall_game_person(initial_choice)
        if win:
            print("You won the car!")
        else:
            print("You got a goat!")
    else:
        print("Invalid mode. Choose 'auto' or 'person'.")
