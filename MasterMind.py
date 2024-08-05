import random

def generate_hint(secret, guess):
    correct_position = sum(s == g for s, g in zip(secret, guess))
    correct_number = sum(min(secret.count(n), guess.count(n)) for n in set(guess)) - correct_position
    return correct_position, correct_number

def player_turn(player_num, secret):
    attempts = 0
    while True:
        guess = input(f"Player {player_num}, enter your guess: ")
        attempts += 1
        if guess == secret:
            print(f"Player {player_num} guessed the number in {attempts} attempts!")
            return attempts
        else:
            correct_position, correct_number = generate_hint(secret, guess)
            print(f"Hint: {correct_position} digits in the correct position and {correct_number} correct digits in the wrong position.")

def get_secret_number(player_num):
    while True:
        secret = input(f"Player {player_num}, set your secret number: ")
        if secret.isdigit():
            return secret
        else:
            print("Invalid input. Please enter a valid multi-digit number.")

def main():
    print("Welcome to the Mastermind game!")
    
    while True:
        secret1 = get_secret_number(1)
    
        print("Player 2, start guessing Player 1's number.")
        attempts_player2 = player_turn(2, secret1)
    
        secret2 = get_secret_number(2)
    
        print("Player 1, start guessing Player 2's number.")
        attempts_player1 = player_turn(1, secret2)
    
        if attempts_player1 < attempts_player2:
            print("Player 1 wins and is crowned Mastermind!")
        elif attempts_player2 < attempts_player1:
            print("Player 2 wins and is crowned Mastermind!")
        else:
            print("It's a tie!")
        
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()