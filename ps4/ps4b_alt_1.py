
import string

### HELPER CODE ###
def load_words(file_name):
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
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###


WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text
       
    def get_valid_words(self):
        return self.valid_words.copy()
        
    def build_shift_dict(self, shift):
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        shifted_alphabet = lowercase[shift:] + lowercase[:shift] + uppercase[shift:] + uppercase[:shift]
        dictionary = {letter: shifted_alphabet[i] for i, letter in enumerate(string.ascii_letters)}
        return dictionary
       
    def apply_shift(self, shift):   
        dictionary = self.build_shift_dict(shift)
        message_text_encrypted = ''
        #notice getter for self.message_text is used
        for char in self.get_message_text():      
            if char.isalpha():
                message_text_encrypted += dictionary[char]
            else:
                message_text_encrypted += char
        return message_text_encrypted

        
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        #initializes self.message_text and self.valid_words via inheritance
        super().__init__(text)    
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        return self.shift
   
    def get_encryption_dict(self):
        return self.encryption_dict.copy()
    
    def get_message_text_encrypted(self):
        return self.message_text_encrypted
 
    def change_shift(self, shift):
        #notice setters are not used since updates are within class
        if shift < 0 or shift >= 26:
            raise ValueError("Shift value must fail within 0 <= shift < 26")
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        #initializes self.message_text and self.valid_words via inheritance
        #implicitly uses self.get_message_text() if self.apply_shift called
        super().__init__(text)    
                                        
  
    def decrypt_message(self):
        valid_word_count = []
        for shift in range(26):
            decrypted_text = self.apply_shift(shift).split()   
            matches = 0
            
            #for each word in decrypted text split to list, add 1 to match if word is valid
            #add number of matches for each shift value
            for word in decrypted_text:                         
                if is_word(self.get_valid_words(), word):        
                    matches += 1
            valid_word_count.append(matches)                    
        best_shift = valid_word_count.index(max(valid_word_count))
        deciphered_text = self.apply_shift(best_shift - 26)
        return (best_shift, deciphered_text)

if __name__ == '__main__':

##    #Example test case (PlaintextMessage)
##    plaintext = PlaintextMessage('hello', 2)
##    print('Expected Output: jgnnq')
##    print('Actual Output:', plaintext.get_message_text_encrypted())
##    print(''*50)
##
##    #Example test case (CiphertextMessage)
##    ciphertext = CiphertextMessage('jgnnq')
##    print('Expected Output:', (24, 'hello'))
##    print('Actual Output:', ciphertext.decrypt_message())
##    print(''*50)

##    # Test case 1
##    plaintext = PlaintextMessage('Hello, world!', 4)
##    print('Test case for PlaintextMessage 1')           
##    print('Input:', plaintext.get_message_text())
##    print('Expected Output:', 'Lipps, asvph!')
##    print('Actual Output:', plaintext.get_message_text_encrypted())
##    print(''*50)           
##
##    # Test case 2
##    plaintext = PlaintextMessage('This is a test message.', 15)
##    print('Test case for PlaintextMessage 2')           
##    print('Input:', plaintext.get_message_text())
##    print('Expected Output:', 'Iwxh xh p ithi bthhpvt.')
##    print('Actual Output:', plaintext.get_message_text_encrypted())
##    print(''*50)
    
##    # Test case 1
##    ciphertext = CiphertextMessage('Khoor, zruog!')
##    print('Test case for CiphertextMessage 1')           
##    print('Input:', ciphertext.get_message_text())
##    print('Expected Output:', 'Hello, world!')
##    print('Actual Output:', ciphertext.decrypt_message())
##    print(''*50)
##    
##    # Test case 2
##    ciphertext = CiphertextMessage('Ocz lpdxf ajs')
##    print('Test case for CiphertextMessage 2')           
##    print('Input:', ciphertext.get_message_text())
##    print('Expected Output:', 'The quick fox')
##    print('Actual Output:', ciphertext.decrypt_message())
##    print(''*50)

    ##Best shift value and unencrypted story
    story = get_story_string()
    best_shift, decrypted_text = CiphertextMessage(story).decrypt_message()
    print('Best shift value:', best_shift)
    print('Decrypted story:', decrypted_text)
    print(''*50)



