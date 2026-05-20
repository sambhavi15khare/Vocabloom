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
        #difficulty:
    # DIFFICULTY SELECTION LOOP
    while True:

        print(Fore.CYAN + "\nChoose Difficulty:\n")

        print("1. EASY\n")
        print("2. MEDIUM\n")
        print("3. HARD\n")

        difficulty = input(
            Fore.YELLOW
            + "Enter your choice: (1/2/3) "
        )

        # EASY
        if difficulty == "1":

            word_length = 5
            attempts = 10
            break

        # MEDIUM
        elif difficulty == "2":

            word_length = 6
            attempts = 8
            break

        # HARD
        elif difficulty == "3":

            word_length = 7
            attempts = 6
            break

        # INVALID
        else:

            print(
                Fore.RED
                + "\nInvalid input! Please enter a valid input (1/2/3)\n"
            )
        
    # generate valid word
    while True:

        secret_word = r.word(
            word_min_length=word_length,
            word_max_length=word_length
        ).lower()

        if (
            secret_word in web2lowerset
            and secret_word.isalpha()
            and len(secret_word) == word_length
        ):
            break


    print(Fore.MAGENTA + "\n🌸 Welcome to Vocabloom <3 🌸")
    print(Fore.CYAN + f"\nBe CAREFULL!!!! You Have Only {attempts} Guesses")
    # GAME ROUND LOOP
    while attempts > 0:

        # take input
        guess = input("enter your guess: ").lower()

        # checking length
        if len(guess) != word_length:
            print(Fore.RED + f"\nPlease Enter Exactly {word_length} Letters")
            continue

        # check alphabets only
        if not guess.isalpha():
            print(Fore.RED + "\nBeep Beep Only Alphabets :(\n")
            continue

        # checking valid english words
        if guess not in web2lowerset:
            print(
                Fore.RED
                + "\nErr... I don't know what that word is :/Maybe try some valid english word\n"
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
        for i in range(word_length):

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
