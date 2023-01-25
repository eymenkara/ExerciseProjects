import random
from typing import List

ex_list = ["World", "Pistol", "Cosmos", "Street", "Jerky", "Zookeeper", "magician", "chess", "important", "redemption",
           "unicorn", "gambit", "stramger", "extraordinary", "infection", "elephant", "supernova", "penguin", "mountain" ]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


# Choose a random word from a list and return it as a list with each of its letters
def random_word(word_list: List[str] ):
    word = random.choice(word_list)
    word = word.lower()
    word_l = []
    for letter in word:
        word_l.append(letter)
    return word_l

# Check if the guessed letter is inside the word and return a list of bool values
def check_letter(word: List[str], letter: str ):
    checklist = []
    for i in word:
        if i == letter.lower() :
            checklist.append(True)
        else:
            checklist.append(False)
    return checklist

# Take a bracketed list, insert correctly guessed letter
def bracketing(bracket_list: List[str], check_list: List[bool], guess: str ):
    temp_list = bracket_list.copy()
    for i in range(len(check_list)):
        if check_list[i] == True:
            temp_list[i] = guess
    return temp_list

# Check if guessed all the letters
def check_complete(list = List[str]):
    n = 0
    for i in list:
        if i == "_":
            n += 1

    if n == 0:
        return True
    else:
        return False


#Game setup ( random word, bracket setup )
word = random_word(ex_list)
brackets = []
for i in word:
    brackets.append("_")

#Start game
endgame = False
life = 6
print(logo)

while not endgame:
    print(stages[life])
    print(brackets)
    if life == 0:
        print("You lost! Try Again.")
        endgame = True
    elif check_complete(brackets):
        print("Congrats! You Won!")
        endgame = True
    else:
        guess = input("Please guess a letter: ").lower()
        check_list = check_letter(word, guess)
        brackets_temp = bracketing(brackets, check_list, guess)
        if brackets_temp == brackets: #Means wrong guess
            life -= 1
            print("Wrong!")
        else:
            brackets = brackets_temp
            print("Right!")




# print(word)
# print(brackets)
# print(check_letter(word, guess))
# round1 = bracketing(brackets, check_letter(word, guess), guess)
# print(round1)
# guess2 = input("Please enter a letter: ").lower()
# round2 = bracketing(round1, check_letter(word, guess2), guess2)
# print(round2)






