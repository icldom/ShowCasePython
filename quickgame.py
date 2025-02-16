print("Rock...\nPaper...\nScissors...")

Dominik = input ("Dominik, make your move: ").lower()
print("***NO CHEATING !!!***\n" * 40)
Viliam = input ("Viliam, make your move: ").lower()

if Dominik == Sebi:
    print("It´s a tie!")
elif Dominik == "rock":
    if Sebi == "paper":
        print("Sebi WINS!")
    elif Sebi == "scissors":
        print("Dominik WINS!")
elif Dominik == "paper":
    if Sebi == "rock":
        print("Dominik WINS!")
    elif Sebi == "scissors":
        print("Sebi WINS!")
elif Dominik == "scissors":
    if Sebi == "rock":
        print("Sebi WINS!")
    elif Sebi == "paper":
        print("Dominik WINS!")
else:
    print("Smth went wrong!")