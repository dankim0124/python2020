#RPS.py
#Name: dohyun kim
#Date: 01/29
#Assignment:RPS
import random


def main():
    wins = 0
    ties = 0
    losses = 0
    #Create a loop that continues as long as the user wants to play.
    # User can play as many games as they wish.
    replay = 1
    while(replay):
        # Randomly choose the computer between 'R', 'P', or 'S'
        computerChoice = random.choice(["R","P","S"])

        # Prompt the user for their RPS selection
        playerChoice = input (" Enter choice R, S, P: ")
        # Determine winner and state what happened to the user
        if playerChoice == "R":
            print ("player chose: Rock")
        elif playerChoice =="S":
            print ("player chose: Scissors")
        elif playerChoice =="P":
            print ("player chose: Paper")

        if computerChoice == "R":
            print("computer chose: Rock")
        elif computerChoice == "S":
            print("computer chose: Scissors")
        elif computerChoice == "P":
            print("computer chose: Paper")

        if playerChoice == "R" and computerChoice =="S":
            wins+=1
            print("Win")
        elif playerChoice =="R" and computerChoice =="P":
            losses +=1
            print("Lose")
        elif playerChoice =="S" and computerChoice =="R":
            losses += 1
            print("Lose")
        elif playerChoice =="S" and computerChoice =="P":
            wins+= 1
            print("Win")
        elif playerChoice =="P" and computerChoice =="S":
            losses += 1
            print("Lose")
        elif playerChoice =="P" and computerChoice =="S":
            wins += 1
            print("Win")
        else:
            ties+=1
            print("Tie")
        # Ask the user if they would like to play again.
        replay = int(input("you like to play more? : (no:0 , yes: input any other character) :" ))


    #In the end, print the stats
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)

main()