
def hangman(secret_word):
    guess_word=['_ ' *len(secret_word)]
    attempt=6
    data=[]
    while guess_word!=list(secret_word) and attempt>0: 
        print(' '.join(guess_word))
        guess = input("Guess the secret word (put a single letter): ").lower()

        if len(guess)!=1:
            print("Please enter only ONE letter.")
            continue
        elif not guess.isalpha():
            print("You only can guess an APLHABET")
        
        if guess in secret_word:
            print("This letter is available in the secret word.")

            for index, letter in enumerate(secret_word):
                if letter == guess:
                    guess_word[index]=guess
                    attempt-=1
                    print("You used 1 attempts. Remaining attempt:", attempt)
                    data.append(guess)
        elif guess in data:
            print("You already guess this letter!")
            print("You still have your attempts. Remaining attempt:", attempt)
            continue
        else:
            print("This letter is not in the secret word.")
            attempt-=1
            print("You used 1 attempts. Remaining attempt:", attempt)
            data.append(guess)
        
    if guess_word!=list(secret_word) and attempt==0:
        print("Oh no! You ran out of attempts, you lose!!")

    print(' '.join(guess_word))
    print("Congratulations! You win!")

hangman('lab')