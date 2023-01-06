word = 'else'

print('Welcome to the game Hangman!')
print('I\'m thinking of a word that is %d letters long.' %len(word))
print('You have 3 warnings.')
print('-'*10)
dict = list('abcdefghijklmnopqrstuvwxyz')
vowel = list('aeiou')
hangman = ['_ ']*len(word)
used = []
num_guess = 6
warnings = 3
i = 0


def conditions(x):
    global num_guess

    if warnings < 0 and num_guess > 0:
        num_guess -= 1
        print('You have no warnings left so you lose one guess:', ''.join(hangman))

    if warnings in range (0,3) and num_guess > 0:
        print('You have', warnings, 'warnings left:', ''.join(hangman))
        

while i <= num_guess:

    print('You have', num_guess, 'guesses left.')
    print('Available letters:', ''.join(dict))
    guess = str.lower(input('Please guess a letter: '))

    if guess.isalpha() == False:
        warnings -= 1
        print('Oops! That is not a valid letter.', end=' ')
        conditions(warnings)

    if guess.isalpha() == True:

        ###New Guess###
        if guess not in used:

            ###Correct Guess###
            if guess in word:
                indices = [idx for idx, x in enumerate(word) if x == guess]  
                for char in indices:
                    hangman[char] = guess
                if guess in dict:
                    dict.remove(guess)
                print('Good guess: ', ''.join(hangman))

            ###Incorrect Guess###
            else:
                if guess in vowel:
                    num_guess -= 2
                else:
                    num_guess -= 1
                if guess in dict:
                    dict.remove(guess)
                print('Oops! That letter is not in the word: ', ''.join(hangman))

        ###Already Guessed###
        else:
            warnings -= 1
            print('Oops! You\'ve already guessed that letter.', end=' ')
            conditions(warnings)

    if guess not in used:
        used.append(guess)

    if ''.join(hangman) == word:
        print('-'*10)
        print('Congratulationds! You win!') 
        print('Your total score for this game is:', num_guess*len(set(word)))
        print('Thanks for playing...')
        print('='*50)
        break 

    if num_guess <= 0:
        print('-'*10)
        print('Sorry, you ran out of guesses. You lose.')
        print('The word was:', word); print('='*50)
        break
    
    print('-'*10)
