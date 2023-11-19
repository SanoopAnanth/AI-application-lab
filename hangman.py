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