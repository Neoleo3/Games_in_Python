#!/usr/bin/env python
# coding: utf-8

# # Project Part 2

# ### Task 1

# #### Word Guessing game 

# In[68]:


import random 

class Guessing_Game:
    def __init__(self):
        self.list = [
            {'lion': '4'}, {'company': '7'}, {'notepad': '7'}, {'software': '8'},
            {'analysis': '8'}, {'python': '6'}, {'keyboard': '8'}, 
            {'jupyterlab': '10'}, {'mouse': '5'}
        ]
        self.question = None
        self.qlist = []  
        self.help = None
        self.end_game = False
        self.guessed_letters = set()  

    def guess_word(self):
        rand_dict = random.choice(self.list)
        self.question = list(rand_dict.keys())[0]  
        self.qlist = list(self.question)  

    def help_for_user(self):
        print(f"Clue: The word has {len(self.question)} letters.")

    def game_play(self):
        self.guess_word()  
        print("Welcome to the Word Guessing Game! Try to guess the word letter by letter.")
        
        while not self.end_game:
            try:
                user_input = input(
                    "\nEnter a character in the hidden word | Type 'help' for a clue | Type 'exit' to quit: "
                ).lower()

           
                if len(user_input) != 1 and user_input not in ['help', 'exit']:
                    raise ValueError("Please enter only one letter at a time.")

                if user_input in self.qlist:
                    if user_input not in self.guessed_letters:
                        self.guessed_letters.add(user_input)
                        print(f"Good job! '{user_input}' is in the word.")
                    else:
                        print(f"You already guessed '{user_input}'. Try another letter.")

      
                    if set(self.qlist) == self.guessed_letters:
                        print(f"Congratulations! You guessed the word: {self.question}")
                        self.end_game = True
                
                elif user_input == 'help':
                    self.help_for_user()
                
                elif user_input == 'exit':
                    print("Thanks for playing! Goodbye!")
                    self.end_game = True
                
                else:
                    print(f"Oops! '{user_input}' is not in the word. Try again.")

            except ValueError as e:
                print(f"Invalid Input: {e}")


def main6():
    game6= Guessing_Game()
    game6.game_play()
if __name__=='__main__':
    main6()


# ## Task 2

# ### Pasted Codes from project 1 for all the games

# #### Riddle Game

# In[56]:


import random
class Riddle_puzzle:
    riddles = {'What has to be broken before you can use it?':'egg' ,
               'I’m tall when I’m young, and I’m short when I’m old. What am I?':'candle',
               'What can’t talk but will reply when spoken to?':'echo',
               'What is full of holes but still holds water?':'sponge',
               'What gets wet while drying?':'Towel',
               'What is always in front of you but can’t be seen?':'future',
               'What can you break, even if you never pick it up or touch it?':'promise',
               'What goes up but never comes down?':'age'
              }
    def __init__(self):
        self.current_riddle=None
        self.answer=None
        self.correct_ans=0
        self.count=0
    def question(self):
        q=random.choice(list(self.riddles.keys()))
        answer = self.riddles[q]
        self.current_riddle=q
        self.answer=answer
        self.flag_endgame =0
        print(q)
    def check(self):
        user_answer = input('Enter your answer')
        self.count=self.count+1
        if self.answer == user_answer.lower():
            self.correct_ans=self.correct_ans+1
            print('Correct')
        else:
            print('Incorrect')
            print(f'The correct answer is {self.answer}')
    def end_game(self):
        print(f'The total number of times played is {self.count}')
        print(f'The number of correct answers is {self.correct_ans}')
        print(f'Score is {round((self.correct_ans/self.count)*100)}%')
        print(f'Thank You! Good Bye')
    def playing_again(self):
        while self.flag_endgame==0:
            user_i=input('Play another riddle:Y/N')
            if user_i.lower()=='y':
                self.question()
                self.check()
            else:
                self.flag_endgame=1
                self.end_game()

def main1():
    game1=Riddle_puzzle()
    game1.question()
    game1.check()
    game1.playing_again()

if __name__ == '__main__':
    main1()
            


# #### Arithmetic Puzzle

# In[58]:


import random 
class Arithmetic_puzzle:
    def __init__(self):
        self.count=0
        self.point=0
        self.end_game =0
        self.result=0
    numbers=range(1,21)
    operators = ['+','-','/','*']
    def question_and_answer(self):
        num1=random.choice(self.numbers)
        num2=random.choice(self.numbers)
        operator = random.choice(self.operators)
        expression=f'{num1}{operator}{num2}'
        result=eval(expression)
        formatted_result = "{:.2f}".format(result)
        self.result=formatted_result
        print('The expression is:')
        print(f'{expression}=?')
            
        
    def user_input(self):
        while self.end_game==0:
            try:
                user_in=float(input('Enter your answer'))
            except ValueError as e:
                print(f'{e} as entered value is not a int, float')
            else:
                formated_user_in = '{:.2f}'.format(user_in)
                self.count=self.count+1
                if formated_user_in==self.result:
                    print('Correct Answer')
                    self.point=self.point+1
                    play_end=input('Do you want to play another round : Y/N')
                    if play_end.lower()=='y':
                        self.question_and_answer()
                        continue
                    else:
                        score=(self.point/self.count)*100
                        print(f'The final score is {round(score,2)}%') 
                        break
                
                else:
                    print('Incorrect')
                    print(f'Answer is {self.result}')
                    play_end=input('Do you want to play another round : Y/N')
                    if play_end.lower()=='y':
                        self.question_and_answer()
                        continue
                    else:
                        score=(self.point/self.count)*100
                        print(f'The final score is {round(score,2)}%') 
                        break


def main2():
    game2=Arithmetic_puzzle()
    game2.question_and_answer()
    game2.user_input()
if __name__=='__main__':
    main2()
    


# #### General Knowledge Quiz Game

# In[1]:


import random
class General_Knowledge:
    def __init__(self):
        self.categories = {
            "Science": [
                {"question": "Which gas do plants absorb during photosynthesis?", "answer": "Carbon dioxide"},
                {"question": "What is the full name of WWW?", "answer": "World Wide Web"},
                {"question": "How many bones are there in the adult human body?", "answer": "206"}
            ],
            "Mathematics": [
                {"question": "What is the only even prime number?", "answer": "2"},
                {"question": "What is the sum of the first 5 natural numbers?", "answer": "15"},
                {"question": "What is the name of the mathematical symbol that is equal to 3.14?", "answer": "Pi"}
            ],
            "Geography": [
                {"question": "What is the tallest mountain on Earth?", "answer": "Mount Everest"},
                {"question": "What is the capital of France?", "answer": "Paris"},
                {"question": "Which planet is known as the Red Planet?", "answer": "Mars"}
            ],
            "Others": [
                {"question": "Which country won the most recent FIFA World Cup (as of 2022)?", "answer": "Argentina"},
                {"question": "Who invented the light bulb?", "answer": "Thomas Edison"},
                {"question": "In which year did India declare itself a Democratic and Republic State with the adoption of the constitution?", "answer": "1950"}
            ]
        }
    def ask_category(self):
        """ Presents category options and returns the selected category """
        while True:
            try:
                print("\nChoose a category:")
                for i, category in enumerate(self.categories.keys(), start=1):
                    print(f"{i}. {category}")
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(self.categories):
                    return list(self.categories.keys())[choice - 1]
                else:
                    print("Invalid choice. Please select a valid category number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    def ask_question(self, question_data):
        """ Displays the question and gets the user's answer """
        print(f"\nQuestion: {question_data['question']}")
        return input("Your answer: ").strip()
    def check_answer(self, user_answer, correct_answer):
        """ Compares the user's answer with the correct answer and gives feedback """
        if user_answer.lower() == correct_answer.lower():
            print("✅ Correct!")
            return True
        else:
            print(f"❌ Incorrect! The correct answer is: {correct_answer}")
            return False
    def display_score(self, total_questions, score):
        print("\n📊 Game Over! Here is your score:")
        print(f"✅ Correct Answers: {score}")
        print(f"❌ Incorrect Answers: {total_questions - score}")
        accuracy = (score / total_questions) * 100 if total_questions > 0 else 0
        print(f"🎯 Accuracy: {accuracy:.2f}%")
    def exec_questions(self, questions):
        """ Iterates through a set of questions, manages user input, and tracks score """
        random.shuffle(questions)  # Shuffle questions for variety
        score = 0
        for question_data in questions:
            user_answer = self.ask_question(question_data)
            if self.check_answer(user_answer, question_data["answer"]):
                score += 1
        return score, len(questions)
    def play_game(self):
        """Manages the main game loop, including category selection, question execution, and replay option."""
        while True:
            category = self.ask_category()
            questions = self.categories[category]

            score, total_questions = self.exec_questions(questions)
            self.display_score(total_questions, score)

            replay = input("\n🔄 Do you want to play again? (yes/no): ").strip().lower()
            if replay != "yes":
                print("🎉 Thank you for playing the General Knowledge Quiz! See you next time. 👋")
                break

def main3():
    print("🎮 Welcome to the General Knowledge Quiz Game!")
    game =General_Knowledge()  # Create an instance of the game
    game.play_game()  # Start the game
if __name__=='__main__':
    main3()
    


# #### Rock Paper Scissor Game with the computer

# In[62]:


import random
class Rock_paper_scissor:
    def __init__(self):
        self.comp=None
        self.human_ans=None
        self.list=['Rock','Paper','Scissor']
    def computer(self):
        self.comp = random.choice(self.list)
    def human(self):
        while True:
            try:
                self.human_ans= input("Enter your choice (Rock, Paper, or Scissor): ").capitalize()
                if self.human_ans not in self.list:
                    raise ValueError("Invalid choice! Please enter Rock, Paper, or Scissor.") 
                break 
            except ValueError as e:
                print(f"Error: {e}")
    def play_game(self):
        if self.human_ans.lower()=='rock' and self.comp.lower()=='rock':
            print('Draw')
        if self.human_ans.lower()=='rock' and self.comp.lower()=='paper':
            print('Computer wins as it is paper')
        if self.human_ans.lower()=='rock' and self.comp.lower()=='scissor':
            print('You Win!')
        if self.human_ans.lower()=='paper' and self.comp.lower()=='rock':
            print('You Win!')
        if self.human_ans.lower()=='paper' and self.comp.lower()=='paper':
            print('Draw!')
        if self.human_ans.lower()=='paper' and self.comp.lower()=='scissor':
            print('Computer wins as it is scissor!')
        if self.human_ans.lower()=='scissor' and self.comp.lower()=='rock':
            print('Computer wins as it is rock!')
        if self.human_ans.lower()=='scissor' and self.comp.lower()=='paper':
            print('You Win!')
        if self.human_ans.lower()=='scissor' and self.comp.lower()=='scissor':
            print('Draw!')

def main4():
    game4=Rock_paper_scissor()
    game4.computer()
    game4.human()
    game4.play_game()

if __name__ == '__main__':
    main4()   


# #### Rock Paper Scissor Game with a User

# In[64]:


class Rock_Paper_scissor_game:
    def __init__(self):
        self.choices=['rock','paper','Scissor']
        self.player1=None 
        self.player2=None
        self.play1=None
        self.play2=None
    def human1(self):
        self.player1=input('Player 1:Enter your name: ')
    def human2(self):
        self.player2=input('Player 2 : Enter your name : ')
    def game_play(self):
        try:
            while True:
                self.play1=input(f'{self.player1}:Enter your choice in (Rock,Paper,Scissor)').lower()
                self.play2=input(f'{self.player2}:Enter your choice in (Rock,Paper,Scissor)').lower()
                if self.play1.lower() not in self.choices or self.play2.lower() not in self.choices:
                    print(f'Invalid choices entered. Please Rock, Paper or Scissor')
                    continue
                else:
                    break
        except ValueError as e:
            print(f'{e} as entered is not a word in the list')
        else:
            if self.play1.lower()=='rock' and self.play2.lower()=='rock':
                print('Rock on Rock, Draw')
            if self.play1.lower()=='rock' and self.play2.lower()=='paper':
                print(f'Paper covers Rock, {self.player1} wins!')
            if self.play1.lower()=='rock' and self.play2.lower()=='scissor':
                print(f'Rock crushes Scissor, {self.player1} wins!')
            if self.play1.lower()=='paper' and self.play2.lower()=='rock':
                print(f'Paper covers Rock, {self.player1} wins!')
            if self.play1.lower()=='paper' and self.play2.lower()=='paper':
                print('Paper on Paer,Draw')
            if self.play1.lower()=='paper' and self.play2.lower()=='scissor':
                print(f'Scissor cuts Paper, {self.player2} wins!')
            if self.play1.lower()=='scissor' and self.play2.lower()=='rock':
                print(f'Rock crushes Scissor, {self.player2} wins!')
            if self.play1.lower()=='scissor' and self.play2.lower()=='paper':
                print(f'Paper covers Scissor, {self.player2} wins!')
            if self.play1.lower()=='scissor' and self.play2.lower()=='scissor':
                print('Scissor on Scissor, Draw')
            

def main5():
    game5=Rock_Paper_scissor_game()
    game5.human1()
    game5.human2()
    game5.game_play()

if __name__=='__main__':
    main5()


# #### Menu method

# In[80]:


def main():
    print('Welcoome! Pick a game of your choice and play on!')
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

if __name__=='__main__':
    main()
    

