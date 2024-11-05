# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

## tasks
- make sure input is valid
- roll the dice and calculate sum
- track sum
- create a chart to display the distribution
- run entire program

## Algorithms:
- Purpose:  input a valid integer 
- Name: valid_input
- Parameters: none 
- Return: number of rolls
- Algorithm:
1. define function 'valid_input'
   1. prompt user to enter the amount of times they want to roll the dice as a positive integer.
   2. while input is invalid:
      1. prompt user to enter a positive integer
   3. return number of rolls


-  Purpose: roll dice 
- Name: roll_dice
-  Parameters: roll dice 
-  Return: sum of the two dice
-  Algorithm:
1. define function roll dice
2. generate first number between 1 and 6
3. generate second random number between 1 and 6
4. return sum of the two numbers


-  Purpose:  store the sums of the dice in a list 
- Name: track_sum
-  Parameters: total_rolls(integer)
-  Return: list of sums
-  Algorithm:
1. define function track_sum
2. create an empty list to store the sums
3. create a list of 11 zeros to count occurrences of each sum
4. while i is in range of total_rolls
   1. call roll_dice function
   2. increment count for the corresponding sum in the count list
5. return count list

- Purpose: create a chart to display the distribution
- Name: display_chart
- Parameters: sum_counts (list of integers)
- Return: none
- Algorithm:
1. define function display_chart
2. print the sum_count list
3. while i is in range of 11
   1. output to user the sum of "Sum of" followed by the current sum (i+2) formatted as a two-digit number.
   2. output a number of asterisks equal to the count of that sum stored in sum_counts[i].

- Purpose: welcome, thank user, call functions, and run program
- Name: main
- Parameters: none
- Return: none
- Algorithm:
1. define main function
2. print welcome message
3. call valid_input function and store result in total_rolls
4. call track_sum function with total_rolls as argument and store result in sum_counts
5. call display_chart function with sum_counts as argument
6. print thank you message



































# Purpose:  [what problem does the function solve?]
# Name: [The proposed name of the function]
# Parameters: [list with purpose in the same order they appear in the function header]
# Return: [return value, it's type, and what it represents]
# Algorithm:
1. define main function
   1. 
2. define function 'calculate_sum'
   1. 
# Purpose:  [what problem does the function solve?]
# Name: [The proposed name of the function]
# Parameters: [list with purpose in the same order they appear in the function header]
# Return: [return value, it's type, and what it represents]
# Algorithm:
2. define function 'random_roll'
   1. 
   1. return random int
# Purpose:  [what problem does the function solve?]
# Name: [The proposed name of the function]
# Parameters: [list with purpose in the same order they appear in the function header]
# Return: [return value, it's type, and what it represents]
# Algorithm:
3. define function 'get_valid_rolls'
   4. 