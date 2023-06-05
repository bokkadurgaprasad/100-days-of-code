#HANGMAN GAME
import random
#Update the word list to use the 'word_list' from words_list.py
from words_list import word_list
#using random module to select the word randomly
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
#In this game we have 6 lives to guess the exact word
lives = 6
#to print the HANGMAN logo 
from stages_list import logo
print(logo)
#Create blanks using empty list
display = []
for _ in range(word_length):
    display += "_"
#While loop used for the end of the game when complete the word or lose all live
while not end_of_game:
    #Asking the user to guess the word
    guess = input("Guess a letter: ").lower()
    #Check guessed letter if already guessed or not
    if guess in display:
        print(f"You've already guessed {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    #if user enter a wrong guess then print it
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose all lives.\n**THE GAME IS OVER**")
            print(f"Hence the word is '{chosen_word}'")
    #Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")
    from stages_list import stages
    print(stages[lives])

