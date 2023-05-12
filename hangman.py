# link to original https://www.youtube.com/watch?v=5x6iAKdJB6U&list=PL7yh-TELLS1EgOLIPo1sVuf_rDPEp33S8&index=1
import random


def get_word() -> str:
    """
    Function to get the self the player will be guessing from a list
    :return:Random self from list
    """
    with open('words', 'r') as f:
        words = f.readlines()
    word = random.choice(words)[:-1]
    return word


def print_word(word: str, guesses: list) -> None:
    """
    Function to print the word with blank lines or correct letters
    :param word: Word the player is guessing
    :param guesses: list of letters guessed
    """
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print('_', end=" ")
    print("")


def check_done(word: str, guesses: list) -> bool:
    """
    Function to check if the game is done
    :param word: Word the player is guessing
    :param guesses: List of letters guessed
    :return: Returns true if the game is done, and False if the game is not done
    """
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False
    return done


def main() -> None:
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    answer = input('Would you like to play hangman? y/n? ')
    while answer.lower().strip() != 'n' and answer.lower().strip() != 'y':  # checks if valid y/n input
        answer = input('Would you like to play hangman? y/n? ')

    while answer.lower().strip() != 'n':
        allowed_errors = 7
        guesses = []
        done = False
        word = get_word()
        while not done:
            print_word(word, guesses)

            guess = input(f'Allowed Errors Left {allowed_errors}, Next Guess: ')
            while guess in guesses:  # checks if letter has already been guessed
                guess = input('Letter has already been guessed. Try again. ')
            while guess not in letters:  # checks guess is a letter
                guess = input('Guess must be a letter. Try again. ')
            guesses.append(guess.lower())

            if guess.lower() not in word.lower():
                allowed_errors -= 1
                if allowed_errors == 0:
                    break

            done = check_done(word, guesses)

        if done:
            print(f'You found the word! It was {word}!\n')
        else:
            print(f'Game Over! The word was {word}.\n')

        answer = input('Would you like to play again? y/n? ')
        
    print('\nThanks for playing!')


if __name__ == "__main__":
    main()
