import random

option = ("rock", "paper", "scissor")
running = True

while running:
    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("enter your choice (rock, paper, scissor): ").lower()
    
    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("Its a Tie!")
    elif player == "rock" and computer == "scissor":
        print(f"{player} beats {computer}")
        print("player won!")
    elif player == "paper" and computer == "rock":
        print(f"{player} beats {computer}")
        print("player won!")
    elif player == "scissor" and computer == "paper":
        print(f"{player} beats {computer}")
        print("player won!")
    else:
        print(f"{computer} beats {player}")
        print("player lose!")

    if not input("play again? (y/n): ").lower() == "y":
        running = False
        
print("Thanks for playing!")