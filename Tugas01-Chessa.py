secret_word = 'lab'
guess_word = ['_', '_', '_']

while guess_word != list(secret_word): 
    print(' '.join(guess_word))
    guess = input("Guess the secret word (put a single letter): ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid. Please enter a single letter.")
        continue

    if guess in secret_word:
        print("This letter is available in the secret word.")

        for index, letter in enumerate(secret_word):
            if letter == guess:
                guess_word[index]=guess
    else:
        print("This letter is not in the secret word.")

print(' '.join(guess_word))
print("Congratulations! You win!")
