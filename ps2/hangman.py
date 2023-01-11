# Problem Set 2, hangman.py

# Hangman Game
# -----------------------------------
# Problem 1: Basic Hangman

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    print('-'*10)
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()



# -----------------------------------
# Problem 2
# Hangman Part 1: Three Helper Functions

def is_word_guessed(secret_word, letters_guessed):
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):  
    display =[]
    for char in secret_word:
        if char in letters_guessed:
            display.append(char) 
        else:
            display.append('_ ')
    return display


def get_available_letters(letters_guessed):
    alphabet = list(string.ascii_lowercase)
    for char in letters_guessed:
        if char in alphabet:
            alphabet.remove(char)        
    print('Available letters: ', ''.join(alphabet))



# -----------------------------------
# Problem 3
# Hangman Part 2: The Game 

def hangman(secret_word):
    print('Welcome to the game Hangman!')
    print('I\'m thinking of a word that is %d letters long.' %len(secret_word))
    print('You have 3 warnings.')
    print('-'*10)

    vowel = list('aeiou')
    letters_guessed = []

    guesses_remaining = 6
    warnings_remaining = 3

    i = 0        
    while i <= guesses_remaining:

        print('You have', guesses_remaining, 'guesses left.')
        get_available_letters(letters_guessed)
        guess = str.lower(input('Please guess a letter: '))

        if guess.isalpha() == False:
            warnings_remaining -= 1
            print('Oops! That is not a valid letter.', end=' ')
            if warnings_remaining < 0 and guesses_remaining > 0:
                guesses_remaining -= 1
                print('You have no warnings left so you lose one guess:', end=' ')
            if warnings_remaining in range (0,3) and guesses_remaining > 0:
                print('You have', warnings_remaining, 'warnings left:', end=' ')
            print(''.join(get_guessed_word(secret_word, letters_guessed)))


        if guess.isalpha() == True:
            
            """New Guess"""
            if guess not in letters_guessed:
                letters_guessed.append(guess)

                """Correct Guess"""
                if guess in secret_word:
                    print('Good guess: ', end=' ')
                    print(''.join(get_guessed_word(secret_word, letters_guessed)))

                """Incorrect Guess"""
                else:
                    if guess in vowel:
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
                    print('Oops! That letter is not in the word: ', end=' ')
                    print(''.join(get_guessed_word(secret_word, letters_guessed)))

            """Already Guessed"""
            else:
                warnings_remaining -= 1
                print('Oops! You\'ve already guessed that letter.', end=' ')
                if warnings_remaining < 0 and guesses_remaining > 0:
                    guesses_remaining -= 1
                    print('You have no warnings left so you lose one guess:', end=' ')
                if warnings_remaining in range (0,3) and guesses_remaining > 0:
                    print('You have', warnings_remaining, 'warnings left:', end=' ')
                print(''.join(get_guessed_word(secret_word, letters_guessed)))

        if is_word_guessed(secret_word, letters_guessed) == True:
            print('-'*10)
            print('Congratulations! You win!') 
            print('Your total score for this game is:', guesses_remaining*len(set(secret_word)))
            print('Thanks for playing...')
            print('='*50)
            break

        if guesses_remaining <= 0:
            print('-'*10)
            print('Sorry, you ran out of guesses. You lose.')
            print('The word was:', secret_word)
            print('='*50)
            break
        
        print('-'*10)



# -----------------------------------
# Problem 4
# Hangman Part 3: The Game with Hints

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    m = list(my_word.replace(' ',''))
    c = list(other_word)
    idx = [i for i, _ in enumerate(m)]

    if len(m) != len(c):
        return False
    else:
        for num in idx:
            if m[num] in string.ascii_lowercase:
                if m[num] != c[num]:
                    return False
                    break
            else:
                if c[num] in m:
                    return False
                    break
                else:
                    return True  
        print(match_with_gaps(my_word, other_word))


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    p = list(my_word.replace(' ',''))
    indices = [i for i, ltr in enumerate(p) if ltr in string.ascii_lowercase]        
    guesses = []
    
    for word in wordlist:
        if len(word) == len(p):
            guesses.append(word)
            
    matches = guesses.copy()

    for word in guesses:
        for idx in indices:
            if word[idx] != p[idx] or match_with_gaps(my_word, word) == False: 
                if word in matches:
                    matches.remove(word)    
    if matches:
        print('Possible word matches are:', end=' ')
        print(*matches, sep=' ')

    else:
        print('No matches found')


def hangman_with_hints(secret_word):
    print('Welcome to the game Hangman!')
    print('I\'m thinking of a word that is %d letters long.' %len(secret_word))
    print('You have 3 warnings.')
    print('-'*10)

    vowel = list('aeiou')
    letters_guessed = []

    guesses_remaining = 6
    warnings_remaining = 3

    i = 0        
    while i <= guesses_remaining:

        print('You have', guesses_remaining, 'guesses left.')
        get_available_letters(letters_guessed)
        guess = str.lower(input('Please guess a letter: '))

        if guess.isalpha() == False:
            if guess == '*':
                hint = ''.join(get_guessed_word(secret_word, letters_guessed))
                print 
                show_possible_matches(hint)

            else:
                warnings_remaining -= 1
                print('Oops! That is not a valid letter.', end=' ')
                if warnings_remaining < 0 and guesses_remaining > 0:
                    guesses_remaining -= 1
                    print('You have no warnings left so you lose one guess:', end=' ')
                if warnings_remaining in range (0,3) and guesses_remaining > 0:
                    print('You have', warnings_remaining, 'warnings left:', end=' ')
                print(''.join(get_guessed_word(secret_word, letters_guessed)))

        if guess.isalpha() == True:
            
            if guess not in letters_guessed:
                letters_guessed.append(guess)

                if guess in secret_word:
                    print('Good guess: ', end=' ')
                    print(''.join(get_guessed_word(secret_word, letters_guessed)))

                else:
                    if guess in vowel:
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
                    print('Oops! That letter is not in the word: ', end=' ')
                    print(''.join(get_guessed_word(secret_word, letters_guessed)))

            else:
                warnings_remaining -= 1
                print('Oops! You\'ve already guessed that letter.', end=' ')
                if warnings_remaining < 0 and guesses_remaining > 0:
                    guesses_remaining -= 1
                    print('You have no warnings left so you lose one guess:', end=' ')
                if warnings_remaining in range (0,3) and guesses_remaining > 0:
                    print('You have', warnings_remaining, 'warnings left:', end=' ')
                print(''.join(get_guessed_word(secret_word, letters_guessed)))

        if is_word_guessed(secret_word, letters_guessed) == True:
            print('-'*10)
            print('Congratulations! You win!') 
            print('Your total score for this game is:', guesses_remaining*len(set(secret_word)))
            print('Thanks for playing...')
            print('='*50)
            break

        if guesses_remaining <= 0:
            print('-'*10)
            print('Sorry, you ran out of guesses. You lose.')
            print('The word was:', secret_word)
            print('='*50)
            break
        
        print('-'*10)


# To test part 2, uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    

# To test part 3, uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
