import random

def monty_hall_game_auto(switch_doors, initial_choice):
    """
    Simulates the Monty Hall game in automatic mode.
    
    :param switch_doors: True if the player switches doors, False otherwise
    :param initial_choice: Initial door chosen
    :return: True if the player wins the car, False otherwise
    """
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    
    # Reveal a door with a goat that the player didn't choose
    doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
    door_revealed = random.choice(doors_revealed)
    
    # If the player switches, they pick the remaining unopened door
    if switch_doors:
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice
    
    return doors[final_choice] == 'car'


def simulation_game(num_games, initial_choice):
    """
    Simulates the Monty Hall game multiple times and calculates the win rates for switching and not switching.
    
    :param num_games: Number of games to simulate
    :param initial_choice: Initial choice of door
    :return: Tuple with win rates for switching and not switching
    """
    num_games_with_switching = sum(monty_hall_game_auto(True, initial_choice) for _ in range(num_games))
    num_games_without_switching = sum(monty_hall_game_auto(False, initial_choice) for _ in range(num_games))
    
    return num_games_with_switching / num_games, num_games_without_switching / num_games

