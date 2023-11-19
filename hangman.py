# import random
# word_list = ["python", "hangman", "programming", "computer", "game", "developer","openai"]
# def choose_word():
#     return random.choice(word_list)
# def display_word(word, guessed_letters):
#     display = ""
#     for letter in word:
#         if letter in guessed_letters:
#             display += letter
#         else:
#             display += "_"
#     return display
# def hangman():
#     selected_word = choose_word()
#     guessed_letters = []
#     attempts = 6 # Number of allowed incorrect attempts
#     print("Welcome to Hangman!")
#     while attempts > 0:
#         display = display_word(selected_word, guessed_letters)
#         print("\nWord:", display)
#         guess = input("Guess a letter: ").lower()
#         if len(guess) != 1 or not guess.isalpha():
#             print("Please enter a single letter.")
#             continue
#         if guess in guessed_letters:
#             print("You've already guessed that letter.")
#             continue
#         guessed_letters.append(guess)
#         if guess in selected_word:
#             print("Correct guess!")
#         else:
#             attempts -= 1
#             print("Incorrect guess. Attempts left:", attempts)
#         if "_" not in display:
#             print("\nCongratulations! You've guessed the word:", selected_word)
#             break
#         if "_" in display:
#             print("\nGame over! The word was:", selected_word)

# hangman()
import random
word_list = ["python", "hangman", "programming", "computer", "game", "developer","openai"]

chosen_word=random.choice(word_list)

lives=6
game_end=False
display=[]
for letter in range(len(chosen_word)):
    display.extend("_")
print(f"{' '.join(display)}")
while not game_end:
    guess=input("Guess a letter? ").lower()
        
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            display[position]=letter
        
    if guess not in chosen_word:
        print(f"you have guessed letter {guess},that's not in the word.You lose a life.")
        lives -= 1
        print("Lives left",lives)
        if lives == 0:
            game_end=True
            print("you lose!")
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        game_end=True
        print("you won!")