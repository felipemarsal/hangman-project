import random

print("H A N G M A N")


def start():
    user_input = input("Type 'play' to play the game, 'exit' to quit: ")
    while user_input != "play" or user_input != "exit":
        if user_input == "exit":
            break
        elif user_input == "play":
            game()
        break
    return


def game():
    k = 8
    list_of_words = ["python", "java", "kotlin", "javascript"]
    choice_computer = random.choice(list_of_words)
    guess_word = list("-" * len(choice_computer))
    all_tries = []
    while k > 0:

        print()
        print("".join(guess_word))
        letter = input("Input a letter: ")

        if (len(letter) > 1) and (len(letter) != 0):
            print("You should input a single letter")
        elif letter in all_tries:
            print("You've already guessed this letter")
        elif (letter.isupper()) or (letter.isalpha() is False):
            print("Please enter a lowercase English letter")
        elif letter not in choice_computer and letter not in guess_word and letter not in all_tries:
            k -= 1
            print("That letter doesn't appear in the word")
        else:

            for i in range(len(choice_computer)):

                if choice_computer[i] == letter:
                    guess_word[i] = letter
                    if "-" not in guess_word:
                        print(f"You guessed the word {''.join(guess_word)}! \nYou survived!""")
        all_tries.append(letter)

        if "-" not in guess_word:
            break

        if k == 0:
            print("You lost!")
    print()

    guess_word.clear()
    all_tries.clear()
    start()


start()
