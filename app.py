import streamlit as st
from November2024_C3_S10_PracticeSolution import (
    Guessing_Game, Riddle_puzzle, Arithmetic_puzzle, General_Knowledge,
    Rock_paper_scissor, Rock_Paper_scissor_game, main1, main2, main3, main4, main5, main6
)

st.header("🎮 Welcome to a Catalog of Games!")

st.write("Pick a game of your choice and play on!")

# Create a dropdown instead of number input
game_choice = st.selectbox(
    "Select a game to play:",
    ["Select a game", "Riddle Puzzle", "Arithmetic Puzzle", "General Knowledge Quiz",
     "Rock Paper Scissor (vs Computer)", "Rock Paper Scissor (vs User)", "Word Guessing Game", "Exit"]
)

# Create a button to confirm game selection
if st.button("Start Game"):
    if game_choice == "Riddle Puzzle":
        main1()
    elif game_choice == "Arithmetic Puzzle":
        main2()
    elif game_choice == "General Knowledge Quiz":
        main3()
    elif game_choice == "Rock Paper Scissor (vs Computer)":
        main4()
    elif game_choice == "Rock Paper Scissor (vs User)":
        main5()
    elif game_choice == "Word Guessing Game":
        main6()
    elif game_choice == "Exit":
        st.write("🎮 Thank you! See you next time!")

