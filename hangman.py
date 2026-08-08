import random


def play_hangman():
    # Small list of 5 predefined words
    words = ["python", "hangman", "coding", "program", "developer"]

    # Select a random word from the list
    secret_word = random.choice(words)

    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("=== Welcome to Hangman! ===")
    print(
        f"Guess the word one letter at a time. You have {max_incorrect} incorrect guesses allowed.\n"
    )

    # Game loop using a while loop
    while incorrect_guesses < max_incorrect:
        # Build current display state of the secret word
        display_word = []
        all_guessed = True

        for letter in secret_word:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")
                all_guessed = False

        print("Word: " + " ".join(display_word))
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        print(
            f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}"
        )

        # Check win condition
        if all_guessed:
            print(f"\nCongratulations! You won! The word was: {secret_word}")
            break

        # Get console input from player
        guess = input("Enter a letter: ").lower().strip()

        # Validate and process guess using if / else statements
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
        else:
            guessed_letters.append(guess)
            if guess in secret_word:
                print(f"Good guess! '{guess}' is in the word.\n")
            else:
                incorrect_guesses += 1
                print(f"Sorry, '{guess}' is not in the word.\n")

    # Lose condition check
    if incorrect_guesses == max_incorrect:
        print("Game Over! You reached the maximum number of incorrect guesses.")
        print(f"The word was: {secret_word}")


if __name__ == "__main__":
    play_hangman()
