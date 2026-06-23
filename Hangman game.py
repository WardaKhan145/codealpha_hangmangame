import random

def play_hangman():
    # 1. Predefined list of 5 words
    words = ["python", "programming", "science", "physics", "computer"]
    secret_word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses_left = 6

    print("    Welcome to Hangman!    ")
    print("Try to guess the secret word letter by letter.")

    # 2. Main game loop (while loop)
    while incorrect_guesses_left > 0:
        print("\n" + " " * 30)
        
        # Display the current state of the word (e.g., p _ t h o n)
        displayed_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        print(f"Word: {displayed_word.strip()}")
        print(f"Incorrect guesses remaining: {incorrect_guesses_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        # Check if the player has guessed all the letters
        # (If there are no underscores left, they won!)
        if "_" not in displayed_word:
            print(f"\n🎉 CONGRATULATIONS! You guessed the word: '{secret_word}'")
            break

        # 3. Get basic console input
        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ INVALIDE INPUT. Please enter a single alphabetical letter.")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You ALREADY GUSSED '{guess}'. Try a different letter.")
            continue

        # Add the guess to our tracker
        guessed_letters.add(guess)

        # 4. Conditional logic (if-else) to check the guess
        if guess in secret_word:
            print(f"✅ GOOD JOB! '{guess}' is in the word.")
        else:
            print(f"❌ OOPS! '{guess}' is not in the word.")
            incorrect_guesses_left -= 1

    # If the loop finishes because they ran out of guesses
    else:
        print("\n" + "-" * 30)
        print("💥 GAME OVER! You've run out of guesses.")
        print(f"The secret word was: '{secret_word}'")

if __name__ == "__main__":
    play_hangman()
