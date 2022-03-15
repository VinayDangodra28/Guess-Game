import random

def Chance(player, mn, mx, n, pOne):
    pTwo = 0
    if player == 1:
        while True:
            print(f"Player{player}:\nGuess the number between {mn} and {mx}")
            guess = input()
            pOne = pOne+1
            if int(guess) == n:
                print(f"Player 1 guesssed the number in {pOne} chances")
                n = random.randint(mn, mx)
                Chance(2, mn, mx, n, pOne)
                break
            elif int(guess)>n:
                print("Your guess is greater than the actual number")
                continue
            elif int(guess)<n:
                print("Your guess is smaller than the actual number")
                continue
    else:
        while True:
            print(f"Player{player}:\nGuess the number between {mn} and {mx}")
            guess = input()
            pTwo = pTwo+1
            if int(guess) == n:
                print(f"Player 2 guesssed the number in {pTwo} chances")
                decision(pOne, pTwo)
                break
            elif int(guess)>n:
                print("Your guess is greater than the actual number")
                continue
            elif int(guess)<n:
                print("Your guess is smaller than the actual number")
                continue
      
      
def decision(pOne, pTwo):
    print(f"Player 1 took {pOne} chances to complete the game and Player 2 took {pTwo} chances to complete the game")
    if pOne>pTwo:
        print("Player two won the game")
    elif pOne<pTwo:
        print("Plpayer 1 won the game")
    else:
        print("It's a tie")
        
              
      
    

def Run():
    mn = input("Enter the lower limit of the range of guessing\n")
    mx = input("Enter the upper limit of the range of guessing\n")
    mn = int(mn)
    mx = int(mx)
    n = random.randint(mn,mx)
    Chance(1, mn, mx, int(n), 0)
    

if __name__ == '__main__':
    Run()
    while True:
        again = input("Do you want to play again?(y/n)(Press enter to exit)")
        if again == "y":
            Run()
        elif again == "n" or again == "":
            break
        else:
            continue

    