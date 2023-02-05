from random import choice

print("Welcome to a game of Hangman!")
print("You have 7 guesses before you lose!\n")
print("Your word:")

word_library = ["GRAPES", "ORANGE", "PEAR", "MELON", "MANGO", "PEACH"]
word_generated = choice(word_library)

#///////////////////////////////////////
list_number = []
for i in range(len(word_generated)):
    list_number.append(i + 1)

list_character = []
list_character.extend(word_generated)

global chosen_word_dictionary
chosen_word_dictionary = dict(zip(list_number, list_character))

#///////////////////////////////////////
list_blanks = []
for i in range(len(word_generated)):
    list_blanks.append("_")

global blanks_chosen_word_dictionary
blanks_chosen_word_dictionary = dict(zip(list_number, list_blanks))

#///////////////////////////////////////
for value in blanks_chosen_word_dictionary.values():
    print(value, end="")
print("\n")


def main():

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
            
        for value in blanks_chosen_word_dictionary.values():
            print(value, end="")
        print("\n")

        if check_win() is True:
            print("You found the word! You won!")
            break
        

def check_win():
    if "_" not in blanks_chosen_word_dictionary.values():
        return True
    return False

def check_lost():
    if counter == 0:
        print("You lost!")
        return True

def get_user_input():
    while True:
        try:
            n = input("Please guess a letter: ").upper()
            if len(n) == 1 and ord(n) > 64 and ord(n) < 91:
                break
        except:
            print("Please type in a single alphabet!")
    return n

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
    
def get_key(val):
    for key in chosen_word_dictionary:
        if chosen_word_dictionary[key] == val:
            return key


main()
                



            

