# Hangman Game

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
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    temp=list(set(secret_word))
    if len(temp)!=len(letters_guessed):
        return False
    for letter in letters_guessed:
        if letter not in secret_word:
            return False
    return True

# function to help find the occurrences of a letter in the given word
def return_index(secret_word,letter):
    l = []
    for i in range(0,len(secret_word)):
        if secret_word[i]==letter:
            l.append(i)
    return l

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ['_']*len(secret_word)

    for letter in letters_guessed:
        pos=return_index(secret_word,letter)

        for i in pos:
            if guessed_word[i]=='_':
                guessed_word[i]=letter

    return ''.join(guessed_word)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabets = list(string.ascii_letters)[:26]
    for letter in letters_guessed:
        alphabets.remove(letter)
    return ''.join(alphabets)

# warning msg
def waring_msg(no_of_warnings_left):
    print("Oops! That is not a valid letter. You have {} warnings left:".format(no_of_warnings_left), end=" ")

# no of guess left msg
def guess_msg(no_of_guess_left):
    print("You have {} guesses left".format(no_of_guess_left))

# winning msg
def winning_msg(no_of_guess_left,letters_gussed):
    print("------------------------")
    print("Congratulations You Won! ")
    print("Your total score for this game is: {}".format(no_of_guess_left*len(letters_gussed)))

# losing msg
def losing_msg(secert_word):
    print("------------------------")
    print("Sorry, you ran out of guesses. The word was {}".format(secert_word))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 9 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    vowels=['a','e','i','o','u']
    print("Welcome to the game Hangman")
    print("I am thinking of a word that is {} letters long".format(len(secret_word)))
    no_of_guess_left=9
    no_of_warnings_left=3
    letters_guessed=[]
    letters_not_in_secert_word=[]
    is_successful=False
    while no_of_guess_left>0:
        print("--------------------------------------")
        guess_msg(no_of_guess_left)
        print(get_available_letters(letters_guessed+letters_not_in_secert_word))

        ''' Input from the user'''
        input1=input("Please guees a letter ")[:1]
        char1=input1.lower()

        if char1.isalpha():
            if char1 in secret_word:
                if char1 in letters_guessed:
                    no_of_warnings_left-=1
                    print("Oops! You've already guessed that letter. You now have {} warnings".format(no_of_warnings_left))
                    if no_of_warnings_left==0:
                        no_of_guess_left-=1
                else:
                    letters_guessed.append(char1)
                    print("Good Guess:",end=" ")
            else:
                if char1 in letters_not_in_secert_word:
                    no_of_warnings_left -= 1
                    print("Oops! You've already guessed that letter. You now have {} warnings".format(
                        no_of_warnings_left))
                    if no_of_warnings_left <= 0:
                        no_of_guess_left -= 1
                else:
                    letters_not_in_secert_word.append(char1)
                    if char1 in vowels:
                        no_of_guess_left-=2
                    else:
                        no_of_guess_left-=1
                    print("Oops! That letter is not in my word:", end=" ")
        else:
            no_of_warnings_left -= 1
            waring_msg(no_of_warnings_left)
            if no_of_warnings_left == 0:
                no_of_guess_left -= 1
        print(get_guessed_word(secret_word,letters_guessed+letters_not_in_secert_word))

        if is_word_guessed(secret_word,letters_guessed):
            is_successful=True
            break
    if is_successful:
        winning_msg(no_of_guess_left,letters_guessed)
    else:
        losing_msg(secret_word)
# --------------------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    if len(other_word)!=len(my_word):
        return False
    for pos in range(0,len(other_word)):
        if my_word[pos]!=other_word[pos] and my_word[pos]!='_':
            return False
    return True

def show_possible_matches(my_word,letters_not_included):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # all words must have equal length with myword
    same_length_words = [word for word in wordlist if len(word) == len(my_word)]

    # misgussed letters are removed
    for i in letters_not_included:
        same_length_words=[word for word in same_length_words if not word.__contains__(i)]

    ''' if starts with certain prefix '''
    prefix=''
    for letter in my_word:
        if letter=='_':
            break
        prefix+=letter
    starts_with_prefix= [ word for word in same_length_words if word.startswith(prefix)]

    ''' end with certain prefix'''
    suffix=''
    for letter in my_word[::-1]:
        if letter=='_':
            break
        suffix=letter+suffix
    ends_with_suffix= [ word for word in starts_with_prefix  if word.endswith(suffix)]

    ''' words that contains letter which are in myword'''
    words_at_pos=ends_with_suffix
    for pos in range(1,len(my_word)-1):
        if my_word[pos]!='_':
            words_at_pos=[word for word in words_at_pos if word[pos]==my_word[pos]]
    if len(words_at_pos)==0:
        print("No Matches Found")
    else:
        print("Possible word matches are:")
        print(words_at_pos)

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    print("Welcome to the game Hangman")
    print("I am thinking of a word that is {} letters long".format(len(secret_word)))
    no_of_guess_left = 6
    no_of_warnings_left = 3
    letters_guessed_correct = []
    is_successful = False
    letters_not_in_secert_word = []

    while no_of_guess_left > 0:
        print("--------------------------------------")
        guess_msg(no_of_guess_left)
        print(get_available_letters(letters_guessed_correct+letters_not_in_secert_word))

        ''' Input from the user: If user enters more than 1 word. first character is considered'''
        input1 = input("Please guees a letter ")[:1]
        char1 = input1.lower()

        if char1.isalpha() or char1=='*':
            if char1=='*':
                show_possible_matches(get_guessed_word(secret_word,letters_guessed_correct),letters_not_in_secert_word)
            elif char1 in secret_word:
                if char1 in letters_guessed_correct:
                    no_of_warnings_left -= 1
                    print("Oops! You've already guessed that letter. You now have {} warnings".format(
                        no_of_warnings_left))
                    if no_of_warnings_left == 0:
                        no_of_guess_left -= 1
                else:
                    letters_guessed_correct.append(char1)
                    print("Good Guess:", end=" ")
            else:
                if char1 in letters_not_in_secert_word:
                    no_of_warnings_left -= 1
                    print("Oops! You've already guessed that letter. You now have {} warnings".format(
                        no_of_warnings_left))
                    if no_of_warnings_left <= 0:
                        no_of_guess_left -= 1
                else:
                    letters_not_in_secert_word.append(char1)
                    if char1 in vowels:
                        no_of_guess_left-=2
                    else:
                        no_of_guess_left-=1
                    print("Oops! That letter is not in my word:", end=" ")
        else:
            no_of_warnings_left -= 1
            waring_msg(no_of_warnings_left)
            if no_of_warnings_left == 0:
                no_of_guess_left -= 1
        print(get_guessed_word(secret_word, letters_guessed_correct))

        if is_word_guessed(secret_word, letters_guessed_correct):
            is_successful = True
            break
    if is_successful:
        winning_msg(no_of_guess_left,letters_guessed_correct)
    else:
        losing_msg(secret_word)

##------------- start of main function ---------------
if __name__ == "__main__":
    secret_word = choose_word(wordlist)

    print("1.Hangman with hints","2.Hangman with no hints","3.Exit",sep='\n')
    choice=int(input("please enter your choice: "))
    print("---------------------------------------------")

    if choice==2:
        hangman(secret_word)
    elif choice==1:
        hangman_with_hints(secret_word)
    else:
        print("Thank you")
