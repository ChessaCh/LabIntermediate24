
def hangman(secret_word):
    kata=['_ ' *len(secret_word)]
    attempt=6
    data=[]
    while kata!=list(secret_word) and attempt>0: 
        print(' '.join(kata))
        tebak= input("Guess the secret word (put a single letter): ").lower()

        if len(tebak)!=1:
            print("Please enter only ONE letter.")
            continue
        elif not tebak.isalpha():
            print("You only can guess an APLHABET")
        
        if tebak in secret_word:
            print("This letter is available in the secret word.")

            for index, letter in enumerate(secret_word):
                if letter == tebak:
                    kata[index]=tebak
                    attempt-=1
                    print("You used 1 attempts. Remaining attempt:", attempt)
                    data.append(tebak)
        elif tebak in data:
            print("You already guess this letter!")
            print("You still have your attempts. Remaining attempt:", attempt)
            continue
        else:
            print("This letter is not in the secret word.")
            attempt-=1
            print("You used 1 attempts. Remaining attempt:", attempt)
            data.append(tebak)
        
    if kata!=list(secret_word) and attempt==0:
        print("Oh no! You ran out of attempts, you lose!!")

    print(' '.join(kata))
    print("Congratulations! You win!")

hangman('lab')