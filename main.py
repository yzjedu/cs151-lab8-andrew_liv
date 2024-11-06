# Programmers: Andrew Leimbach & Liv Oakes
# Course:  CS151, Dr. Zee
# Due Date: 11/6/2024
# Lab Assignment: 8
# Problem Statement: Create a program to roll pairs of dice and display the sum of the dice roll in a chart
# Data In: Amount of times dice are rolled
# Data Out: Chart and list displaying the sums
# Credits: Class Assignment

import random

# Purpose: Make sure user enters a valid input
# Parameters: None
# Return: total_rolls
def valid_input():
    total_rolls = input("Enter the number of rolls: ")

    # Check if the input is a valid integer and positive
    if total_rolls.isdigit() and int(total_rolls) > 0:
        return int(total_rolls)
    else:
        # Print error message for invalid input
        print("Error: Please enter a valid positive integer.")
        return -1  # Return an invalid value to indicate failure


# Purpose: Simulates the sum of dice roll
# Parameters: None
# Return: Sum
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2


# Purpose: Create a list of the sums
# Parameters: total_rolls
# Return: sum_counts
def track_sum(total_rolls):
    sum_counts = [0] * 11  # List to count occurrences of sums (2 to 12)
    for _ in range(total_rolls):
        roll = roll_dice()
        sum_counts[roll - 2] += 1  # Adjust index to match sum (2-12)
    return sum_counts


# Purpose: Displays the sums in a chart using "*"
# Parameters: sum_counts
# Return: None
def display_chart(sum_counts):
    print("\nSum Distribution:")
    print(sum_counts)  # Output the raw counts list (this is optional for debugging)
    for i in range(11):
        sum_value = i + 2
        stars = '*' * sum_counts[i]
        print(f"Sum of {sum_value:02} {stars}")


# Purpose: Welcome, thank user, call functions, and run program
# Parameters: None
# Return: None
def main():
    print("Welcome to the dice rolling simulation!")

    # Get a valid number of rolls from the user
    total_rolls = valid_input()

    # If the input was invalid, ask again
    while total_rolls == -1:
        total_rolls = valid_input()

    # Track the sums of the dice rolls
    sum_counts = track_sum(total_rolls)

    # Display the distribution chart
    display_chart(sum_counts)

    print("\nThank you for using the dice rolling simulator!")


# Run the program
main()
