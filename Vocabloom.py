from wonderwords import RandomWord
from colorama import Fore, Style, init
from english_words import get_english_words_set
from PyDictionary import PyDictionary
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
init()
dictionary = PyDictionary()
web2lowerset = get_english_words_set(['web2'], lower=True)
while True:
    #random 5 letter word generation
    r= RandomWord()
    secret_word=r.word(word_min_length = 5,word_max_length =5)
    # print(secret_word)
    attempts=10
    print("\n 🌸 Wellcome to Vocabloom <3🌸")
    print("Be CAREFULL!!!! You Have Only 10 Guesses")
    #game round loops
    while attempts>0:
        #take input
        guess=input("enter your guess: ").lower()
        #checking the length
        if len(guess)!=5:
            print("\n Please Enter Exactly 5 Letters \n")
            continue
        #check for alphabets
        if not guess.isalpha():
            print("\nBeep Beep Only Alphabets :( \n")
            continue
        #checking valid english words
        if guess not in web2lowerset:
            print("\n Err... I don't know what that word is:/ maybe try some valid english word \n")
            continue
        #win condition
        if guess == secret_word:
            print(Fore.GREEN+"Wohooooo YOU WON!!!!!")
            print(Fore.CYAN + f"The Word Was: ", {secret_word.upper()})
            #WORD MEANING
            synsets = wordnet.synsets(secret_word)

            if len(synsets) > 0:

                print(
                    Fore.LIGHTMAGENTA_EX
                    + synsets[0].definition()
                )

            else:

                # try lowercase again just in case
                synsets = wordnet.synsets(secret_word.lower())

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
                    break
        #result display
        print("\nResult: ", end="")
        used_letters =[]
        #checking the letters
        for i in range(5):
            if guess[i] == secret_word[i]:
                print(Fore.GREEN + guess[i].upper(), end=" ")
                used_letters.append(i)
            elif guess[i] in secret_word:
                print(Fore.YELLOW + guess[i].upper(), end=" ")
            else:
                print(Fore.RED + guess[i].upper(), end=" ")
        print(Style.RESET_ALL)
        attempts -=1
        print(f"\n Oopsie Doopsie You Only have Attempts left: {attempts}\n")
    #lose condition
    if attempts ==0:
        print(Fore.RED + "\n uhoh That's sad Game Over You Don't Have Any More Attempts Left")
        print(Fore.CYAN + f" The Word Was:{secret_word.upper()}")
        synsets = wordnet.synsets(secret_word)
        if len(synsets) > 0:
            print(
                Fore.LIGHTMAGENTA_EX
                + synsets[0].definition()
            )

        else:

            # try lowercase again just in case
            synsets = wordnet.synsets(secret_word.lower())

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
                break
        #play again
        play_again=input(Fore.MAGENTA+"\n Do You Want To Play Again?(yes/no): ").lower()
        if play_again != "yes":
            print(Fore.MAGENTA + "\nThat Is Sad You're Leaving Already But Never Mind... Thanks For Playing 🌸")
            break

