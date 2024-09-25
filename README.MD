# Monty Hall Game Project

## Overview

This project simulates the classic **Monty Hall problem**, a probability puzzle based on a game show scenario. The project is divided into two solutions:

- **Solution 1**: A command-line based version of the Monty Hall problem without any graphical user interface.
- **Solution 2**: An interactive version built with **Streamlit**, providing a user-friendly interface for players to experiment with the game.

## Project Structure

### Directory Layout

```bash
 montyhall/ 
 │ 
 ├── solution1/      # CLI-based solution without a UI
 │ ├── img/          # Contains images used in the game 
 │ └── src/          # Source code for Solution 1 
 │      ├── auto_version.py      # Automated gameplay logic 
 │      ├── game_mood.py         # Contains game modes 
 │      ├── main.py              # Entry point for the game 
 │      └── person_version.py    # Human player interaction logic 
 │ 
 ├── solution2/           # UI-based solution with Streamlit 
 │ ├── img/               # Contains images used in the game 
 │ └── src/               # Source code for Solution 2 
 │      ├── app.py        # Streamlit app interface 
 │      ├── auto_version.py         # Automated gameplay logic 
 │      ├── game_mood.py            # Contains game modes 
 │      ├── main.py                 # Entry point for the game 
 │      └── person_version.py       # Human player interaction logic 
 ```


## Solution 1: Command-Line Version

This version allows users to play the Monty Hall game through the command line. The user can choose to play the game or simulate it in automated modes.

### Key Features:
- **Manual mode**: Play the game by selecting doors manually.
- **Automated mode**: Simulates a large number of game runs, allowing the user to analyze probabilities and outcomes without manual intervention.
- **Game Modes**: 
  - Switch door
  - Stay with the original choice

### Files:
- `main.py`: The entry point to run the game.
- `auto_version.py`: Handles the logic for automated gameplay.
- `game_mood.py`: Defines different game modes.
- `person_version.py`: Allows human players to interact with the game.

## Solution 2: Streamlit UI Version

The second solution enhances the first by adding a graphical interface through **Streamlit**. Users can easily interact with the Monty Hall game and visualize the outcomes through the web interface.

### Key Features:
- **Interactive UI**: Play the game through a simple and clean interface.
- **Simulations**: Easily set up and run multiple simulations to observe the statistical results.
- **Real-time visualization**: View real-time updates on the results of the games and simulations.

### Files:
- `app.py`: The main file that runs the Streamlit app.
- Other files (`auto_version.py`, `game_mood.py`, `person_version.py`) function similarly to those in Solution 1 but integrate with the UI.

### Demo:

![alt text](Solution2/src/img/Screenshot%202024-09-25%20144455.png)

## How to Run the Project

### Solution 1: Command-Line Version
1. Navigate to the `solution1/src` folder.
2. Run the following command to start the game:
   ```bash
   python main.py
   ```

### Solution 2: Streamlit UI Version
1. Navigate to the `solution2/src` folder.
2. Run the following command to start the game:
   ```bash
   streamlit run app.py
   ```

