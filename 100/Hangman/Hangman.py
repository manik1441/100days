import random
import ASCII

word_list = ["aardvark", "baboon", "camel"]
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO - Set lives of the user to guess
lives = 6

# TODO - Shows the blank spaces as per the chosen_word length
display = []
for i in range(len(chosen_word)):
    display += "_"

# TODO - Run Loop till all the words match
end_of_game = False
while not end_of_game:

    # TODO - Ask the user to guess a letter and assign their answer to a variable called guess.
    guess = input("Guess a letter: ").lower()

    # TODO-3 - Check if the letter guess is one of the letters in the chosen_word and put in the blank space.
    if guess not in chosen_word:
        lives -= 1
        print('Bad luck - ', display, ASCII.stages[-lives])
    else:
        for index in range(len(chosen_word)):
            if guess == chosen_word[index]:
                display[index] = guess
        print('Good - ', display)
    if '_' not in display:
        end_of_game = True
        print('You Win')
    if lives == 0:
        end_of_game = True
        print('You Lose')
