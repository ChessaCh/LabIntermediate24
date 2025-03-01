def hangman(secret_word):
    kata=['_']*len(secret_word) 
    attempt=6
    data=[] 

    while '_' in kata and attempt>0:
        print(' '.join(kata))
        tebak=input("Guess the secret word (put a single letter): ").lower()

        if len(tebak)!=1:
            print("Please enter only ONE letter.")
            continue
        elif not tebak.isalpha():
            print("You can only guess an ALPHABET.")
            continue

        if tebak in data:
            print("You already guessed this letter!")
            print("You still have your attempts. Remaining attempt:", attempt)
            continue

        if tebak in secret_word:
            print("This letter is available in the secret word.")
            attempt -= 1
            print("You used 1 attempt. Remaining attempts:", attempt)
            for index, letter in enumerate(secret_word):
                if letter == tebak:
                    kata[index] = tebak
            data.append(tebak)
        else:
            print("This letter is not in the secret word.")
            attempt -= 1
            print("You used 1 attempt. Remaining attempts:", attempt)
            data.append(tebak)

    if '_' not in kata:
        print(' '.join(kata))
        print("Congratulations! You win!")
    else:
        print("Oh no! You ran out of attempts, you lose!!")

hangman('lab')