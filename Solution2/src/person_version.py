import random
import streamlit as st
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
    
    st.write(f"Door {door_revealed + 1} is revealed and it has a goat.")
    
    # Ask the person if they want to switch
    switch = st.selectbox("Do you want to switch doors? (yes/no): ",("None","NO","YES"))
    if switch == 'YES':
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    elif switch == "NO":
        final_choice = initial_choice

    
    if switch in ["YES","NO"]:
        return doors[final_choice] == 'car'
    else:
        return None
