from wonderwords import RandomWord
from colorama import Fore, Style, init
from english_words import get_english_words_set
import nltk
from nltk.corpus import wordnet

# download dictionary
nltk.download('wordnet')

# initialize colorama
init(autoreset=True)

# english words database
web2lowerset = get_english_words_set(['web2'], lower=True)

# random word generator
r = RandomWord()


# FUNCTION TO SHOW WORD MEANING
def show_meaning(word):

    print(Fore.YELLOW + "\nMeaning:\n")

    synsets = wordnet.synsets(word)

    if len(synsets) > 0:

        print(
            Fore.LIGHTMAGENTA_EX
            + synsets[0].definition()
        )

    else:

        synsets = wordnet.synsets(word.lower())

        if len(synsets) > 0:

            print(
                Fore.LIGHTMAGENTA_EX
                + synsets[0].definition()
            )

        else:

            print(
                Fore.RED
                + "ERROR 404! Meaning Not Found :("
            )


# MAIN GAME LOOP
while True:

    # generate valid 5-letter word
    while True:

        secret_word = r.word(
            word_min_length=5,
            word_max_length=5
        ).lower()

        if (
            secret_word in web2lowerset
            and secret_word.isalpha()
            and len(secret_word) == 5
        ):
            break

    attempts = 10

    print(Fore.MAGENTA + "\n🌸 Welcome to Vocabloom <3 🌸")
    print(Fore.CYAN + "Be CAREFULL!!!! You Have Only 10 Guesses\n")

    # GAME ROUND LOOP
    while attempts > 0:

        # take input
        guess = input("enter your guess: ").lower()

        # checking length
        if len(guess) != 5:
            print(Fore.RED + "\nPlease Enter Exactly 5 Letters\n")
            continue

        # check alphabets only
        if not guess.isalpha():
            print(Fore.RED + "\nBeep Beep Only Alphabets :(\n")
            continue

        # checking valid english words
        if guess not in web2lowerset:
            print(
                Fore.RED
                + "\nErr... I don't know what that word is :/\nMaybe try some valid english word\n"
            )
            continue

        # WIN CONDITION
        if guess == secret_word:

            print(Fore.GREEN + "\nWohooooo YOU WON!!!!!!")

            print(
                Fore.CYAN
                + f"The Word Was: {secret_word.upper()}"
            )

            show_meaning(secret_word)

            break

        # RESULT DISPLAY
        print("\nResult: ", end="")

        # checking letters
        for i in range(5):

            # correct letter + correct position
            if guess[i] == secret_word[i]:

                print(
                    Fore.GREEN
                    + guess[i].upper(),
                    end=" "
                )

            # correct letter but wrong position
            elif guess[i] in secret_word:

                print(
                    Fore.YELLOW
                    + guess[i].upper(),
                    end=" "
                )

            # wrong letter
            else:

                print(
                    Fore.RED
                    + guess[i].upper(),
                    end=" "
                )

        print(Style.RESET_ALL)

        attempts -= 1

        print(
            Fore.WHITE
            + f"\n\nOopsie Doopsie You Only have Attempts left: {attempts}\n"
        )

    # LOSE CONDITION
    if attempts == 0:

        print(
            Fore.RED
            + "\nUhoh That's sad :( Game Over You Don't Have Any More Attempts Left"
        )

        print(
            Fore.CYAN
            + f"\nThe Word Was: {secret_word.upper()}"
        )

        show_meaning(secret_word)

    # PLAY AGAIN
    play_again = input(
        Fore.MAGENTA
        + "\nDo You Want To Play Again? (yes/no): "
    ).lower()

    # EXIT GAME
    if play_again != "yes":

        print(
            Fore.MAGENTA
            + "\nThat Is Sad You're Leaving Already But Never Mind... Thanks For Playing 🌸"
        )

        break
