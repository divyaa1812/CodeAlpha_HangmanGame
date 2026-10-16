import random

# Hangman stages
HANGMAN_STAGES = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Words grouped by difficulty
WORD_LISTS = {
    "easy": ["apple", "tiger", "chair", "bread", "plant"],
    "medium": ["python", "journey", "diamond", "library", "monitor"],
    "hard": ["algorithm", "technology", "programming", "development", "artificial"]
}


def choose_difficulty():
    """Ask the player to select a difficulty level."""
    while True:
        print("\nChoose difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        choice = input("Enter your choice (1-3): ").strip()

        levels = {"1": "easy", "2": "medium", "3": "hard"}

        if choice in levels:
            return levels[choice]

        print("Invalid choice. Please enter 1, 2, or 3.")


def display_game(secret_word, guessed_letters, wrong_guesses):
    """Display the current game state."""
    print(HANGMAN_STAGES[wrong_guesses])

    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("Word:", display_word)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("Attempts remaining:", 6 - wrong_guesses)


def play_round():
    """Play one round of Hangman and return the score."""
    difficulty = choose_difficulty()
    secret_word = random.choice(WORD_LISTS[difficulty])

    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print(f"\nYou selected {difficulty.upper()} mode!")
    print("Guess the word one letter at a time.")

    while wrong_guesses < max_attempts:
        display_game(secret_word, guessed_letters, wrong_guesses)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You won!")
            points = {"easy": 10, "medium": 20, "hard": 30}
            return points[difficulty]

        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    display_game(secret_word, guessed_letters, wrong_guesses)
    print("\nGame over! You ran out of attempts.")
    print("The correct word was:", secret_word)

    return 0


def main():
    """Run the game and manage the total score."""
    total_score = 0

    print("=" * 40)
    print("       PYTHON HANGMAN GAME")
    print("=" * 40)

    while True:
        total_score += play_round()

        print("\nYour total score:", total_score)

        play_again = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if play_again not in ("yes", "y"):
            break

    print("\nThanks for playing!")
    print("Final score:", total_score)
    print("Goodbye!")


if __name__ == "__main__":
    main()