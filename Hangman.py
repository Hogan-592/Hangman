#This project uses random library that's built in python to randomly choose a word
#Let the user to guess the word
import random
from words import words #from words which is the python file and second words is the variable
import string

#To beigin with, we need the computers to radnomly choose a word for us to guess
def get_valid_word(words):
    word = random.choice(words) #It takes in a list and randomly chooses something from the list
    #but there will be dash line and white space in the list of words, so use a loop to get a valid word
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

#We need to able to keep track which letter we guessed and which letter in the word we correctly guessed
#Need to keeo track what is a valid letter

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #it saves all the letters in a word as a set
    alphabet = set(string.ascii_uppercase) #all uppercase letter in english dictionary, return 26 alphabet in uppercase.
    used_letter = set() #An empty set to keep track of what the user has guessed

    lives = 6

#Since we are going to remove a letter from the word everytime we guessed correctly, while as the length of word is bigger than zero
    while len(word_letters) > 0 and lives > 0:
        #Join to turn a list into string separated space before the dot join
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letter)) #This join method allows us to join the letter with whatever that is in front of the dot

        #Need to tell the user that current word is ( W - R D)
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        #getting user input
        user_input = input('Guess a letter: ').upper()
        #If the letter user inputted is a valid character we haven't used yet
        if user_input in alphabet - used_letter:
            used_letter.add(user_input)
            #Everytime I guessed the word correctly, the number of the letters in the word that computer generated decreases
            if user_input in word_letters:
                word_letters.remove(user_input)
            else: #If the letter user inputted is not in the word letter computer generated, we want take away a life
                lives -= 1
                print('Letter is not in the word')

        elif user_input in used_letter:
                print('You have already used that character. Please try again.')
        else:
                print('Invalid character. Please try again')
                
    #we reach here means the while loop is broke
    #we exist the whole loop when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')


hangman()
