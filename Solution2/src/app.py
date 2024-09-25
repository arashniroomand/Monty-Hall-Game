import streamlit as st
from main import run_auto_mode, run_person_mode  # Importing from main.py

# Initialize mode and image variables using session state to persist across reruns
if 'mode' not in st.session_state:
    st.session_state['mode'] = None
if 'image' not in st.session_state:
    st.session_state['image'] = None  # To store the image path

# Apply custom button style
st.markdown("""
    <style>
    .stButton > button {
        width: 500px;
        height: 60px;
        background-color: #429E9D; /* Main color */
        color: white; /* Button text color */
        font-size:50px;
        font-weight: bold;
        border-radius: 50px;
        border: none;
        text-align: center;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #367D7A; /* Darker color on hover */
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar content
st.sidebar.title("Monty Hall Game")
st.sidebar.markdown("""
### Summary
The Monty Hall problem is a famous probability puzzle based on a game show scenario. 
In the game, a contestant is presented with three doors: behind one door is a car (the prize), 
and behind the other two doors are goats. After the contestant picks a door, the host, who knows 
what is behind each door, opens another door to reveal a goat. The contestant then has the option 
to either stick with their original choice or switch to the other unopened door. 
Counterintuitively, switching doors gives the contestant a higher probability of winning the car.

### Info
- **Origin**: Named after the host of the television game show "Let's Make a Deal."
- **Probability**: If you stick with your initial choice, your chances of winning are 1/3; 
  if you switch, your chances improve to 2/3.
- **Strategy**: The optimal strategy is to always switch after the host reveals a goat.
""")

# Main content
st.title("Welcome to the Monty Hall Game!")
st.write("##### Try your luck with the Monty Hall problem. Choose a door and see if you can win the car!")

# Container for buttons to choose between Auto and Person modes
with st.container():
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        if st.button('Auto'):
            st.session_state['mode'] = "Auto"
            st.session_state['image'] = "img/Wall-E.jpg"  # Store the image for Auto mode

    with col2:
        if st.button('Person'):
            st.session_state['mode'] = "Person"
            st.session_state['image'] = "img/tintin-motobike.jpg"  # Store the image for Person mode

# Display the selected mode and image
if st.session_state['mode']:
    if st.session_state['image']:
        st.image(st.session_state['image'], caption=f"{st.session_state['mode']} Mode Selected",width = 500)
    
    if st.session_state['mode'] == "Auto":
        st.markdown("<h1 style='text-align: center; font-size: 32px; font-weight: bold;'>You have selected Auto mode!</h1>", unsafe_allow_html=True)
        run_auto_mode()  # Call the function from main.py to run the auto mode
    elif st.session_state['mode'] == "Person":
        st.markdown("<h1 style='text-align: center; font-size: 32px; font-weight: bold;'>You have selected Person mode!</h1>", unsafe_allow_html=True)
        run_person_mode()  # Call the function from main.py to run the person mode
else:
    st.markdown("<h1 style='text-align: center; font-size: 32px; font-weight: bold;'>Please select a mode.</h1>", unsafe_allow_html=True)
