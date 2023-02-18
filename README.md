# Hangman-Game-Python :coffin:
A simple game of Hangman in Python (Word topic: Fruits). Python libraries used: random

## Thoughts on starting this project
My third programming project, in Python. (still a python game) My approach to this traditional python project is through dictionaries as well. Creating 2 dictionaries, one with key-values with
'_' as all its values and another dictionary of equal number of keys with alphabets of the word the user is supposed to guess as its values. If user guesses the correct letter,
then the key in the 'word' dictionary with that alphabet is taken, and used to update the same key of the 'blanks' dictionary to the correspondng alphabet,
then the 'blanks' dictionary is printed for the user to see the updated changes. Else if wrong letter is guessed, then an image of the 'hangman' will show, and will
become more complete as the user made more wrong guesses.

<br>

Computer program used for coding: VS Code

## Code description
Let's start with:
1. Imported Libraries
2. Defining the dictionary and lists
3. Self-defined functions
4. Main code

<br>

<br>

**1. Imported Libraries**
```python
from random import choice
```
Importing the 'random' library's 'choice' function.

<br>

<br>

**2. Defining the dictionary and lists**
```python
word_library = ["GRAPES", "ORANGE", "PEAR", "MELON", "MANGO", "PEACH"]
word_generated = choice(word_library)
```
This list contains all the possible words (topic: fruits), the computer will choose an element (word) at random in the list for the user to guess.

<br>

```python
list_number = []
for i in range(len(word_generated)):
    list_number.append(i + 1)

list_character = []
list_character.extend(word_generated)

global chosen_word_dictionary
chosen_word_dictionary = dict(zip(list_number, list_character))
```
The code creates the 'word' dictionary by zipping (or combining using 'dict(zip(list_number, list_character)) 2 lists of the same number of elements together. 
'list_number[]' as the key, and the 'list_character[]' as the corresponding values. 

'list_number[]' is created based on the word chosen using the length of that word. If there is e.g. 5 
letters in the word, there will be 5 keys appended numbered 1 to 5 in the list.  

'list_character[]' is created based on the word by taking the word as a string, and extending the list by taking the individual characters in the word (string)
as elements in the list.

'chosen_word_dictionary, is made 'global' so I can reference to it in my Self-defined functions.

<br>

```python
list_blanks = []
for i in range(len(word_generated)):
    list_blanks.append("_")

global blanks_chosen_word_dictionary
blanks_chosen_word_dictionary = dict(zip(list_number, list_blanks))
```
The code creates the 'blanks' dictionary by zipping (or combining using 'dict(zip(list_number, list_blanks)) 2 lists of the same number of elements together. 
'list_number[]' as the key, and the 'list_blanks[]' as the corresponding values. 

'list_blanks[]' basically contains all values of '_', with the same and corresponding number of keys to 'list_number[]'

'blanks_chosen_word_dictionary, is made 'global' so I can reference to it in my Self-defined functions.

<br>

<br>

**3. Self-defined functions**
```python
def check_win():
    if "_" not in blanks_chosen_word_dictionary.values():
        return True
    return False
```
The 'check_win()' function is to check if the full word has already been guessed, and will terminate the game indicating the user has won in the main loop.
It does so by checking if there is no more '_' as the value in the 'blanks' dictionary, if there is still '_' as its value means the user haven't guessed all the
hidden alphabets correctly yet.

<br>

```python
def check_lost():
    if counter == 0:
        print("You lost!")
        return True
```
The 'check_lost' function is to check if the user has lost the game. In the main code, the counter function is defined with int 7, and a if loop is in place to
make it countdown to -1 whenever a user made a wrong guess. When counter == 0 in this case, the main code's while loop will break and the game will tell
the user that he has lost.

The counter idea was taken from online, though I did not follow their code and made the function work to my code.

<br>

```python
def get_user_input():
    while True:
        try:
            n = input("Please guess a letter: ").upper()
            if len(n) == 1 and ord(n) > 64 and ord(n) < 91:
                break
        except:
            print("Please type in a single alphabet!")
    return 
```
The 'get_user_input()' function, like the previous 2 projects, gets user input, forces it to uppercase (this way, both lowercase and uppercase input is taken), 
and checks if that input is an uppercase alphabet (A-Z) using the 'ord()' function, and the corresponding number to the uppercase alphabet character in the ASCII table, of length 1, and not a string. If user input does not meet the conditions, the
user will be prompted infinitely until the desired input is given.

<br>

```python
def incorrect_guess(n):
    if n not in chosen_word_dictionary.values() and counter == 6:
        print("  _______ \n"
            "  |   |    \n"
            "  |        \n"
            "  |        \n"
            "  |        \n"
            "  |        \n"
            "  |        \n"
            "__|__\n")
        return True
    elif n not in chosen_word_dictionary.values() and counter == 5:
        print("  _______ \n"
            "  |   |    \n"
            "  |   o    \n"
            "  |        \n"
            "  |        \n"
            "  |        \n"
            "  |        \n"
            "__|__\n")
        return True
    elif n not in chosen_word_dictionary.values() and counter == 4:
        print("  _______ \n"
            "  |   |    \n"
            "  |   o    \n"
            "  |   |    \n"
            "  |        \n"
            "  |        \n"
            "  |        \n"
            "__|__\n")
        return True
    elif n not in chosen_word_dictionary.values() and counter == 3:
        print("  _______ \n"
            "  |   |    \n"
            "  |   o    \n"
            "  |  \|    \n"
            "  |        \n"
            "  |        \n"
            "  |        \n"
            "__|__\n")
        return True
    elif n not in chosen_word_dictionary.values() and counter == 2:
        print("  _______ \n"
            "  |   |    \n"
            "  |   o    \n"
            "  |  \|/   \n"
            "  |        \n"
            "  |        \n"
            "  |        \n"
            "__|__\n")
        return True
    elif n not in chosen_word_dictionary.values() and counter == 1:
        print("  _______ \n"
            "  |   |    \n"
            "  |   o    \n"
            "  |  \|/   \n"
            "  |  /     \n"
            "  |        \n"
            "  |        \n"
            "__|__\n")
        return True
    elif n not in chosen_word_dictionary.values() and counter == 0:
        print("  _______ \n"
            "  |   |    \n"
            "  |   o    \n"
            "  |  \|/   \n"
            "  |   /\   \n"
            "  |        \n"
            "  |        \n"
            "__|__\n")
        return True
    elif n in chosen_word_dictionary.values():
        return False
    print("Hi idk what to put here")
```
The 'incorrect_guess(n)' function takes an argument 'n', which is the alphabet the user has guessed in the main code, and checks if this alphabet is
in the word the user is supposed to guess by comparing to all the values in the 'word' dictionary. If alphabet is not in the 'word' dictionary, and depending
on the value of the counter, it prints out the phase at which the hangman is at. If the alpahbet user guessed is in the 'word' dictionary, this function
does nothing as passes to the next line in the main code. (drawn out picture taken from code online)

<br>

```python
def get_key(val):
    for key in chosen_word_dictionary:
        if chosen_word_dictionary[key] == val:
            return key
```
The 'get_key(val)' function took quite a few online tutorials to figure out. 'val' is the user's input (guess of an alphabet from main code).
'chosen_word_dictionary[key]' gets the values in the 'word' dictionary and iterates through the dictionary to find a value (alphabets in the word the user is supposed
to guess) in the dictionary. If it finds a value that matches the user's input (val), it then returns the key of that value and returns it to the main code.

In the main code, that key from 'word' dictionary is then used in the corresponding key in 'blanks' dictionary and updates the user's input in the
'blanks' dictionary which is then printed out for user to see.

<br>

<br>

**4. Main code**
```python
for value in blanks_chosen_word_dictionary.values():
    print(value, end="")
print("\n")
```
Prints out the 'blanks' dictionary, giving the user an idea of how many letters are there in the word the user need to guess.

<br>

```python
    global counter
    counter = 6

    while True:
        x = get_user_input()

        if incorrect_guess(x) is True:
            print(f"Incorrect guess! You have {counter} guess(es) remaining!")
            if check_lost() is True:
                break
            counter -= 1
        else:
            blanks_chosen_word_dictionary[get_key(x)] = x
```
Gives the user a counter of 6. 

Gets user input.

If the user makes a wrong guess, the counter will -1. This gives the user 7 gusses until he/she will lose (including 0). If counter == 0, 'check_lost()' will run.
And will break out of the game (while loop).

Else, the 'blanks' dictionary is updated.

<br>

```python
        for value in blanks_chosen_word_dictionary.values():
            print(value, end="")
        print("\n")
```
Prints out the updated 'blanks' dictionary if user guesses a letter correctly.

<br>
        
```python
        if check_win() is True:
                    print("You found the word! You won!")
                    break
```
Checks if 'check_win()' is True, refer to the 'check_win()' function in the Self-defined functions.

<br>

<br>

## Output
```
Welcome to a game of Hangman!
You have 7 guesses before you lose!

Your word:
_____

Please guess a letter: e
_E___

Please guess a letter: a
  _______ 
  |   |
  |
  |
  |
  |
  |
__|__

Incorrect guess! You have 6 guess(es) remaining!
_E___

Please guess a letter: t
  _______ 
  |   |
  |   o
  |
  |
  |
  |
__|__

Incorrect guess! You have 5 guess(es) remaining!
_E___

Please guess a letter: c
  _______ 
  |   |
  |   o
  |   |
  |
  |
  |
__|__

Incorrect guess! You have 4 guess(es) remaining!
_E___

Please guess a letter: o
_E_O_

Please guess a letter: y
  _______ 
  |   |
  |   o
  |  \|
  |
  |
  |
__|__

Incorrect guess! You have 3 guess(es) remaining!
_E_O_

Please guess a letter: l
_ELO_

Please guess a letter: p
  _______ 
  |   |
  |   o
  |  \|/
  |
  |
  |
__|__

Incorrect guess! You have 2 guess(es) remaining!
_ELO_

Please guess a letter: n
_ELON

Please guess a letter: m
MELON

You found the word! You won!
```
User lose has a different output at the end.

## Thoughts after the project
With better grasp of the concept after making my previous python game 'Tic-Tac-Toe', I found that myself more comfortable when making this one, even though it
still took me 2 days :weary:.

This project further expanded my knowledge on dictionaries, and the functionality of key-pair values. Learnt new commands such as zip(), ord(), append(), extend() converting lists into
dictionaries and using counter.

<br>

To be improved:
* This code does not work if you attempt to add words into the 'word_library' list with multiple of the same alphabet in the word such as 'APPLE' and 'BANANA'.
Have tested that if you guess e.g. letter 'P' in 'APPLE', only the first 'P' in 'APPLE' will be revealed to the user and updated. If user chose 'P' again,
it is classified as a wrong guess. Haven,t tried solving this, wanted to move on to other projects.
* Also, if you guess a letter that has already been guessed in the past such as 'M' again in 'MELON', it will be classified a wrong guess. Should be a quick
way to solve this such as adding a loop to re-prompt user for another guess like 'This letter has already been gussed!'if user typed in a letter already 
in the updated 'blanks' dictionary.
* Maybe can add a feature that shows the user the letters the user has already guessed as a reminder. If those letters are accidentally inputed again, they won't be
classified as a wrong guess and the user will be re-prompted.
* Like all code, more features can definitely be added to make the game more interactive like making generating a random word of maybe 5 to 7 letters in the
english dictionary instead of limiting it to only a list of words the programmer add in.

<br>

Have a gif:

![Semantic description of image](https://media.tenor.com/FFfFI5OA5-IAAAAM/elliot-katt.gif)
