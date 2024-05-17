import random
import hangman_game_ascii as short

playing = True
words = short.words
hangman = short.hangman
wrong_letters = []
word = random.choice(words)
tries, guess, guesses = 0, '', ''
check = ''.join(dict.fromkeys(word))


def game():
    global word, words, wrong_letters, tries, guess, guesses, check
    print("Let's play hangman! Try to guess word!")
    print(hangman[0])
    while len(check) != len(guesses) and tries < 6:
        for letter in word:
            if letter in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print('')
        guess = str(input('Guess one letter or whole word: ')).lower()
        if guess != word:
            if len(guess) > 1:
                print('Only one letter at the time!')
            elif guess not in word:
                print(f'Sorry, no letter {guess} in word')
                tries += 1
                wrong_letters += guess
                wrong_letters = ''.join(dict.fromkeys(wrong_letters))
                print(hangman[tries])
            else:
                guesses += guess
                guesses = "".join(dict.fromkeys(guesses))
                print(hangman[tries])
            print('Wrong letters: ', end='')
            [print(i, end=' ') for i in wrong_letters]
            print('\n')
        else:
            guesses += guess
            guesses = ''.join(dict.fromkeys(guesses))


def check_win():
    global check, guesses, word
    if len(check) == len(guesses):
        print(f'Congratulations! You guessed it! It was "{word}"')
    else:
        print(f'You lose! Word was "{word}". Try again.')


def play_again():
    global playing, word, tries, guess, guesses, wrong_letters, words, check
    again = input('Do you want to play again? (Y/N) ').upper()
    if again not in ['Y', 'N']:
        again = input('Do you want to play again? (Y/N) ').upper()
    else:
        if again == 'Y':
            playing = True
            words = short.words
            wrong_letters = []
            word = random.choice(words)
            tries, guess, guesses = 0, '', ''
            check = ''.join(dict.fromkeys(word))
        if again == 'N':
            print('Thank You for playing!')
            playing = False


while playing:
    game()
    check_win()
    play_again()
