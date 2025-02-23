import streamlit as st
from November2024_C3_S10_PracticeSolution import Guessing_Game,Riddle_puzzle,Arithmetic_puzzle,General_Knowledge,Rock_paper_scissor,Rock_Paper_scissor_game,main1,main2,main3,main4,main5,main6

st.header('Welcome to a Catalog of games, fellow User!')
def main():
    st.write('Pick a game of your choice and play on!')
    valid_choices = [1,2,3,4,5,6,7]
    end_game =0
    while end_game==0:
        try:
            user_num=st.number_input('Game code: 1 is Riddle Puzzle, 2 is Arithmatic Puzzle, 3 is General Knowledge Quiz Game, 4 is Rock Paper Scissor with computer,5 is a Rock Paper Scissor game with a User,6 is Word Guessing game,7 to exit the game',min_value=1,max_value=7)
            if user_num not in valid_choices:
                print('You have entered the wrong option')
                continue
        except ValueError as e:
            print(f'{e}')
        else:
            if user_num==1:
                main1()
            elif user_num==2:
                main2()
            elif user_num==3:
                main3()
            elif user_num==4:
                main4()
            elif user_num==5:
                main5()
            elif user_num==6:
                main6()
            else:
                print('Thank you! GoodBye')
                break 

if st.button('Play Game'):
    main()   

