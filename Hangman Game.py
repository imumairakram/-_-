import random

def choose_word():
    word_list = ["python", "hangman", "developer", "software", "programming"]
    
    chosen_word = random.choice(word_list)
    
    hinted_word = "".join([letter if random.choice([True, False]) else "_" for letter in chosen_word])
    
    print(f"DEBUG: Hinted word: {hinted_word}, *Rewrite all the alphabets to complete it.")
    
    return chosen_word

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts_remaining = 6
    
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while attempts_remaining > 0:
        print("\nWord: ", display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts_remaining -= 1

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nGame Over! The word was:", word)

if __name__ == "__main__":
    hangman()
