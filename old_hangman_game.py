import random

words = ['absurd', 'abyss', 'affix', 'avenue', 'bagpipes', 'bandwagon', 'beekeeper', 'blizzard', 'cobweb', 'crypt',
         'curacao', 'cycle', 'duplex', 'dwarves', 'equip', 'exodus', 'fixable', 'fjord', 'galaxy', 'glyph']
hangman = [
    '''
    |===|
        |
        |
        |
        |
   ======     
    ''',
    '''
    |===|
    o   |
        |
        |
        |
   ======     
    ''',
    '''
    |===|
    o   |
   /    |
        |
        |
   ======     
    ''',
    '''
    |===|
    o   |
   /|   |
        |
        |
   ======     
    ''',
    '''
    |===|
    o   |
   /|\\  |
        |
        |
   ======     
    ''',
    '''
    |===|
    o   |
   /|\\  |
   /    |
        |
   ======     
    ''',
    '''
    |===|
    o   |
   /|\\  |
   / \\  |
        |
   ======     
    '''
]
wrong_letters = []

word = random.choice(words)

tries, guess, guesses = 0, '', ''
check = ''.join(dict.fromkeys(word))

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

if len(check) == len(guesses):
    print(f'Congratulations! You guessed it! It was "{word}"')
else:
    print(f'You lose! Word was "{word}". Try again.')
