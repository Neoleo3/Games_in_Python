
import streamlit as st
import random

# --------------------------- Word Guessing Game --------------------------- #
class WordGuessingGame:
    def __init__(self):
        self.words = ['lion', 'company', 'notepad', 'software', 'analysis', 'python', 'keyboard', 'jupyterlab', 'mouse']
        self.word = random.choice(self.words)
        self.guessed_letters = set()
        self.max_attempts = 10

    def play(self):
        st.subheader("🔤 Word Guessing Game")
        clue = f"The word has {len(self.word)} letters."
        st.info(clue)
        display_word = ''.join([char if char in self.guessed_letters else '_' for char in self.word])

        st.write("Word:", ' '.join(display_word.upper()))
        letter = st.text_input("Guess a letter:", max_chars=1, key='word_input')
        if letter:
            letter = letter.lower()
            if letter in self.word:
                self.guessed_letters.add(letter)
                st.success(f"'{letter}' is in the word!")
            else:
                st.error(f"'{letter}' is not in the word.")
            display_word = ''.join([char if char in self.guessed_letters else '_' for char in self.word])
            if set(display_word) == set(self.word):
                st.balloons()
                st.success(f"🎉 Congratulations! The word is: {self.word.upper()}")
                self.word = random.choice(self.words)
                self.guessed_letters.clear()

# --------------------------- Riddle Game --------------------------- #
class RiddleGame:
    riddles = {
        'What has to be broken before you can use it?': 'egg',
        'I’m tall when I’m young, and I’m short when I’m old. What am I?': 'candle',
        'What can’t talk but will reply when spoken to?': 'echo',
        'What is full of holes but still holds water?': 'sponge',
        'What gets wet while drying?': 'towel',
        'What is always in front of you but can’t be seen?': 'future',
        'What can you break, even if you never pick it up or touch it?': 'promise',
        'What goes up but never comes down?': 'age'
    }

    def play(self):
        st.subheader("🧩 Riddle Game")
        question = random.choice(list(self.riddles.keys()))
        correct_answer = self.riddles[question]
        st.write(f"Riddle: {question}")
        user_input = st.text_input("Your Answer:", key='riddle_input')
        if user_input:
            if user_input.lower() == correct_answer.lower():
                st.success("Correct! 🎉")
            else:
                st.error(f"Incorrect! The correct answer was: {correct_answer}")

# --------------------------- Arithmetic Puzzle --------------------------- #
class ArithmeticPuzzle:
    def play(self):
        st.subheader("➕ Arithmetic Puzzle")
        num1, num2 = random.randint(1, 20), random.randint(1, 20)
        op = random.choice(['+', '-', '*', '/'])
        expression = f"{num1} {op} {num2}"
        result = round(eval(expression), 2)
        st.write(f"Expression: **{expression} = ?**")
        user_answer = st.text_input("Your Answer:", key='math_input')
        if user_answer:
            try:
                if round(float(user_answer), 2) == result:
                    st.success("Correct ✅")
                else:
                    st.error(f"Incorrect ❌ The correct answer is {result}")
            except ValueError:
                st.warning("Please enter a valid number.")

# --------------------------- Rock Paper Scissors (vs Computer) --------------------------- #
def rock_paper_scissors():
    st.subheader("✊ Rock Paper Scissors (vs Computer)")
    choices = ["Rock", "Paper", "Scissor"]
    user_choice = st.radio("Choose:", choices)
    if st.button("Play", key="play_rps"):
        comp_choice = random.choice(choices)
        st.write(f"Computer chose: **{comp_choice}**")
        if user_choice == comp_choice:
            st.info("It's a Draw!")
        elif (user_choice == "Rock" and comp_choice == "Scissor") or              (user_choice == "Paper" and comp_choice == "Rock") or              (user_choice == "Scissor" and comp_choice == "Paper"):
            st.success("You Win! 🎉")
        else:
            st.error("Computer Wins!")

# --------------------------- Game Selector --------------------------- #
def main():
    st.title("🎮 My Python Game Arcade")
    game = st.sidebar.selectbox("Select a Game:", [
        "Word Guessing Game",
        "Riddle Game",
        "Arithmetic Puzzle",
        "Rock Paper Scissors (vs Computer)"
    ])

    if game == "Word Guessing Game":
        WordGuessingGame().play()
    elif game == "Riddle Game":
        RiddleGame().play()
    elif game == "Arithmetic Puzzle":
        ArithmeticPuzzle().play()
    elif game == "Rock Paper Scissors (vs Computer)":
        rock_paper_scissors()

if __name__ == '__main__':
    main()
    
