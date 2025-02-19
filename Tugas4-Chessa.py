import random
wins=0
losses=0
def hangman(secret_word):
    global wins,losses
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
            print("You still have your attempts. Remaining attempt:", attempt)
            for index, letter in enumerate(secret_word):
                if letter == tebak:
                    kata[index] = tebak
            data.append(tebak)
        else:
            print("This letter is not in the secret word.")
            attempt-=1
            print("You used 1 attempt. Remaining attempts:", attempt)
            data.append(tebak)

    if '_' not in kata:
        print(' '.join(kata))
        print("Congratulations! You win!")
        wins+=1
    else:
        print("Oh no! You ran out of attempts, you lose!!")
        losses+=1

listkata = ["labpy", "tugas", "kampus", "semangat", "python"]

while True:
    if not listkata:
        print("No games left.. Thank you for playing! >.< ")
        print("Your final score: wins(", wins,")","losses(", losses,")" )
        break

    secret_word = random.choice(listkata)  
    listkata.remove(secret_word)  
    hangman(secret_word)

    mainlagi = input("Do you want to play again? (yes/no): ").lower()
    if mainlagi != "yes":
        print("Thank you for playing! Goodbye!")
        print("Your final score: wins(", wins,")","losses(", losses,")" )
        break