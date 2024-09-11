import random
from utils import words_list, HANGMAN


def check_for_letters(word, guess, dashes):
    for i in range(len(word)):
        if word[i] == guess:
            dashes[i] = guess

    return dashes


def game(random_word, dash_arr, ind, hangman):
    guess = input("Guess the Word: ").lower()

    if guess in random_word and guess not in dash_arr:
        print(hangman[ind])
        ind -= 1
        dash_arr = check_for_letters(random_word, guess, dash_arr)
    else:
        print(hangman[ind+1])

    return dash_arr, ind


def main(hangman):
    random_word = random.choice(words_list)
    dash_arr = []
    for _ in random_word:
        dash_arr.append('_')
    print(dash_arr)

    ind = 0
    while ind < 6:
        dash_arr, ind = game(random_word, dash_arr, ind, hangman)
        if '_' not in dash_arr:
            print("Hurray!! You Won 💯 \n"
                  f"The word was {random_word}!")
            break
        print(dash_arr)
        ind += 1
    else:
        print("You Lost 🩻 \n"
              f"The word was {random_word}!")


print("""
WELCOME TO HANGMAN
""")
print(HANGMAN[0])

main(HANGMAN)
