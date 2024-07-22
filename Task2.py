import random

def get_player_number(player_name):
    while True:
        num = input(f"{player_name}, enter a multi-digit number: ")
        if num.isdigit() and len(num) > 1:
            return num
        else:
            print("Invalid input. Please enter a multi-digit number.")

def get_guess(player_name):
    while True:
        num = input(f"{player_name}, enter your guess: ")
        if num.isdigit() and len(num) > 1:
            return num
        else:
            print("Invalid input. Please enter a multi-digit number.")

def give_hint(correct_digits, correct_positions):
    hint = ""
    for i in range(len(correct_digits)):
        if correct_positions[i]:
            hint += "X "  # correct digit in correct position
        else:
            hint += "O "  # correct digit in incorrect position
    return hint.strip()

def play_mastermind():
    player1_name = "Player 1"
    player2_name = "Player 2"

    # Player 1 sets the number
    player1_number = get_player_number(player1_name)
    print(f"{player1_name} has set the number.")

    # Player 2 tries to guess
    attempts = 0
    while True:
        attempts += 1
        player2_guess = get_guess(player2_name)
        correct_digits = [digit for digit in player2_guess if digit in player1_number]
        correct_positions = [player2_guess[i] == player1_number[i] for i in range(len(player1_number))]
        hint = give_hint(correct_digits, correct_positions)
        print(f"Hint: {hint}")
        if player2_guess == player1_number:
            print(f"{player2_name} wins! It took {attempts} attempts.")
            break

    # Player 2 sets the number
    player2_number = get_player_number(player2_name)
    print(f"{player2_name} has set the number.")

    # Player 1 tries to guess
    attempts = 0
    while True:
        attempts += 1
        player1_guess = get_guess(player1_name)
        correct_digits = [digit for digit in player1_guess if digit in player2_number]
        correct_positions = [player1_guess[i] == player2_number[i] for i in range(len(player2_number))]
        hint = give_hint(correct_digits, correct_positions)
        print(f"Hint: {hint}")
        if player1_guess == player2_number:
            if attempts < attempts:
                print(f"{player1_name} wins! It took {attempts} attempts.")
            else:
                print(f"{player2_name} wins! It took {attempts} attempts.")
            break

play_mastermind()



