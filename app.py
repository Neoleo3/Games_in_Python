import streamlit as st
from November2024_C3_S10_PracticeSolution import Guessing_Game,Riddle_puzzle,Arithmetic_puzzle,General_Knowledge,Rock_paper_scissor,Rock_Paper_scissor_game,main1,main2,main3,main4,main5,main6

st.title('Welcome to a Catalog of games, fellow User!')
if st.button('Click here'):
    def main():
        print('Pick a game of your choice and play on!')
        valid_choices = [1,2,3,4,5,6,7]
        end_game =0
        while end_game==0:
            try:
                inpt_of_the_user = int(input('Game code: 1 is Riddle Puzzle, 2 is Arithmatic Puzzle, 3 is General Knowledge Quiz Game, 4 is Rock Paper Scissor with computer,5 is a Rock Paper Scissor game with a User,6 is Word Guessing game,7 to exit the game'))
                if inpt_of_the_user not in valid_choices:
                    print('You have entered the wrong option')
                    continue
            except ValueError as e:
                print(f'{e}')
            else:
                if inpt_of_the_user==1:
                    main1()
                elif inpt_of_the_user==2:
                    main2()
                elif inpt_of_the_user==3:
                    main3()
                elif inpt_of_the_user==4:
                    main4()
                elif inpt_of_the_user==5:
                    main5()
                elif inpt_of_the_user==6:
                    main6()
                else:
                    print('Thank you! GoodBye')
                    break    

