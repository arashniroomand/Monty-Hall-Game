import random

def monty_hall_game_person(initial_choice):
    """
    Simulates the Monty Hall game with a person playing.
    
    :return: True if the player wins the car, False otherwise
    """
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    # Reveal a door with a goat
    doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
    door_revealed = random.choice(doors_revealed)
    
    print(f"Door {door_revealed} is revealed and it has a goat.")
    
    # Ask the person if they want to switch
    switch = input("Do you want to switch doors? (yes/no): ").lower()
    if switch == 'yes':
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice
    
    return doors[final_choice] == 'car'
