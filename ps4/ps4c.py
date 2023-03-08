import time
import string
from ps4a import get_permutations

def timing_with_time():
    start = time.perf_counter()
    time.sleep(1)
    end = time.perf_counter()
    print(end - start)
    
### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        dictionary = {char: char for char in string.ascii_letters}
        # for character in vowels_permutation ex. idx 0, 'e' 
        for i, char in enumerate(vowels_permutation):
            if char.isupper():
                dictionary[VOWELS_UPPER[i]] = char               
            else:
                # dictionary[ VOWELS_LOWER[0]=a ] = 'e'
                dictionary[VOWELS_LOWER[i]] = char
        return dictionary
    
##    # Method 2 - Dictionary Size = 52, Both Cases Updated
##    def build_transpose_dict(self, vowels_permutation):
##    dictionary = {char: char for char in string.ascii_letters}
##    for i, char in enumerate(vowels_permutation):
##        dictionary[VOWELS_UPPER[i]] = char.upper()
##        dictionary[VOWELS_LOWER[i]] = char.lower()
##    return dictionary

##    # Method 3 - Dictionary Size = len(vowels_permutation)
##    def build_transpose_dict(self, vowels_permutation):
##        dictionary = {}
##        for i, char in enumerate(vowels_permutation):
##            if char.isupper():
##                vowels = VOWELS_UPPER
##            else:
##                vowels = VOWELS_LOWER
##            dictionary[char] = VOWELS[i].upper() if char.isupper() else vowels[i].lower()
##        return dictionary         
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypted_message = ''
        for char in self.get_message_text():
            # if character is a letter, add corresponding letter
            if char in transpose_dict:
                encrypted_message += transpose_dict[char]
            # if character is not a letter, e.g., punctuations, add as is
            else:
                encrypted_message += char
        return encrypted_message
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)


    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        max_valid_words = 0
        permutations = get_permutations(permutation)

        for perm in permutations:
            # builds cipher dictionary for permutation and encrypts message
            encrypted_message = self.apply_transpose(self.build_transpose_dict(perm))

            # check encrypted message for valid words
            valid_word_count = 0
            for word in encrypted_message.split():
                if is_word(self.get_valid_words(), word):
                    valid_word_count += 1
                    
            # update decrypted messsage if more valid words found
            if valid_word_count > max_valid_words:
                max_valid_words = valid_word_count
                decrypted_message = encrypted_message
                
        if max_valid_words == 0:
            return self.get_message_text()
        else:
            return decrypted_message


if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    encrypted_dict = message.build_transpose_dict(permutation)
    actual_encryption = message.apply_transpose(encrypted_dict)
    print("Actual encryption:", actual_encryption)    
    encrypted_message = EncryptedSubMessage(actual_encryption)
    print("Decrypted message:", encrypted_message.decrypt_message())
    print(''*50)
     
    #TODO: WRITE YOUR TEST CASES HERE
    
timing_with_time()    
