import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "learning"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6  # You can adjust the number of allowed attempts

    print("Welcome to Hangman!")

    while attempts_left > 0:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"Word: {current_display}")
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts_left -= 1
            print("Incorrect guess!")

        if set(guessed_letters) >= set(word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if attempts_left == 0:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

# Run the Hangman game
hangman()
