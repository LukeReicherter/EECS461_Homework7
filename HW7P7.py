'''
Created: 03/10/2025
Last Change: 03/10/2025
Name: Luke Reicherter
KU ID: 3135060
EECS 461: Homework 7 Problem 7
Description: The following code ia a function that produces m samples of random varaible
Y defined in Quiz 4.2
Input: None
Output: The list of random numbers and the frequency of numbers > 1.5.
'''
import random

def quiz31rv(m):
    random_numbers = [] # Holds the values of the randomly generated numbers
    count_greater_than_1_5 = 0  # Variable to track how many numbers are greater than 1.5

    # Creates a list of numbers with length m
    for num in range(m):
        num = random.uniform(0, 1)  # Generate a random number between 0 and 1
        scaled_num = 4 * num         # Scale it by 4
        random_numbers.append(scaled_num)  # Add to the list
        
        # Checks if the scaled number is greater than 1.5
        if scaled_num > 1.5:
            count_greater_than_1_5 += 1  # Increment the count if so
    
    # Calculate the frequency as the ratio of numbers greater than 1.5 to total numbers
    frequency = count_greater_than_1_5 / m
    return random_numbers, frequency

def main():
    random_numbers, frequency = quiz31rv(int(input("Enter value for m: ")))
    print("Random Numbers:", random_numbers)
    print("Frequency of numbers greater than 1.5:", frequency)

main()
