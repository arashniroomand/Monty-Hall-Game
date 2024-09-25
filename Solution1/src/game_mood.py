import random

def game_mood(mood):
    """
    This function returns the player's initial choice based on the game mode ('auto' or 'person').
    """
    if mood == 'auto':
        initial_choice = random.choice(range(3))
    elif mood == 'person':
        try:
            initial_choice = int(input("Enter a number between 0, 1 and 2: "))
            if initial_choice not in [0, 1, 2]:
                print("The number you choose must be 0, 1, or 2.")
                return game_mood(mood)
        except ValueError:
            print("Please enter a valid number.")
            return game_mood(mood)
    else:
        raise ValueError("Invalid game mode. Choose 'auto' or 'person'.")
    
    return initial_choice


