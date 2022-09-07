import random
from hangman_art import logo,stickman_art
from words import word_list


def clear():
    print('\n'*50)


#generate a random word
# test_list = ['Balloon', 'Car', 'Monkey']
rand_word = random.choice(word_list).lower()
print(word_list)

#hide the word to display
hidden_word = []
for x in range(len(rand_word)):
    hidden_word.append('_')

game_over = False
lives = 6
letters_guessed = []

print(logo)
print(stickman_art[lives])

while not game_over:

    print(hidden_word)
    #have the user guess a letter
    guess = input('Guess a letter: ').lower()

    clear()


    #remove a life for incorrect answer
    if guess not in rand_word and guess not in letters_guessed:
        lives -= 1
        letters_guessed.append(guess)
    elif guess in letters_guessed:
        print(f'You have already guessed letter: {guess}')
    else:
        # check if guess matches a letter in word
        for x in range(len(rand_word)):
            if guess == rand_word[x]:
                hidden_word[x] = rand_word[x]
        letters_guessed.append(guess)

    print(stickman_art[lives])

    # check if the player has lost
    if lives == 0:
        game_over = True
        print(f'Game Over. You Lost!\nThe word was: {rand_word}')

    if '_' not in hidden_word:
        game_over = True
        print(f'Congratulations! You guessed the word!\nThe word was: {rand_word}')