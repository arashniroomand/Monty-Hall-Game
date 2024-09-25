from src.game_mood import *
from src.auto_version import *
from src.person_version import *
import streamlit as st

def run_auto_mode():
    """Function to handle Auto Mode."""
    num_games = int(st.select_slider("Number of games to simulate:",options = range(1, 100001), value = 2))
    initial_choice = game_mood("auto")  # Simulate auto mode game mood
    switch_rate, no_switch_rate = simulation_game(num_games, initial_choice)
    
    # Display the results using Streamlit
    st.write(f"**Win rate with switching:** {switch_rate * 100:.2f}%")
    st.write(f"**Win rate without switching:** {no_switch_rate * 100:.2f}%")

def run_person_mode():
    """Function to handle Person Mode."""
    st.write("Choose a door (1, 2, or 3):")
    choice = st.selectbox("Your choice:", [1, 2, 3]) - 1
    
    # Simulate the game based on the user's choice
    win = monty_hall_game_person(choice)

    if win is not None:  # Check if win is explicitly None or not
        if win:
            st.success("Congratulations! You won the car!")
        else:
            st.warning("Sorry, you got a goat. Try again!")
    else:
        st.write("Please select an option.")
