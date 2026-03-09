# Number Statistics Calculator
# Name: Alisha
# Sample run:
# Welcome! Enter numbers one by one.
# Enter an integer: 5
# Enter another? (y/n) y
# Enter an integer: 10
# Enter another? (y/n) y
# Enter an integer: 3
# Enter another? (y/n) n
# 3 numbers were entered.
# The sum is 18
# The average is 6.0
# 3 was the smallest number entered.
# 10 was the biggest number entered.

def main():
    """Main function that controls the program flow."""
    more = 'y'
    total = 0
    count = 0
    num = 0
    smallest = None
    biggest = None

    print("Welcome! Enter numbers one by one.")

    while more == 'y':
        num = get_number()
        total, count, smallest, biggest = calc_stats(total, count, smallest, biggest, num)
        more = get_more()

    output_message(total, count, smallest, biggest)

def get_number():
    """
    Prompts the user to enter an integer.
    Returns:
        int: The integer entered by the user.
    """
    num = int(input("\nEnter an integer: "))
    return num

def get_more():
    """
    Asks the user if they want to enter another number.
    Returns:
        str: 'y' or 'n' depending on user's input.
    """
    more = input("Enter another? (y/n) ")
    return more.lower()

def calc_stats(total, count, smallest, biggest, num):
    """
    Updates the running total, count, smallest, and biggest numbers.
    Parameters:
        total (int): Current sum of numbers.
        count (int): How many numbers entered so far.
        smallest (int): The smallest number so far.
        biggest (int): The biggest number so far.
        num (int): The new number entered by user.
    Returns:
        tuple: Updated (total, count, smallest, biggest)
    """
    total = total + num
    count = count + 1

    if count == 1:  # if this is the first number
        smallest = num
        biggest = num
    else:
        if num < smallest:
            smallest = num
        if num > biggest:
            biggest = num

    return total, count, smallest, biggest

def output_message(total, count, smallest, biggest):
    """
    Displays the results (sum, average, min, max).
    Parameters:
        total (int): Sum of numbers.
        count (int): Number of entries.
        smallest (int): Minimum number.
        biggest (int): Maximum number.
    Returns:
        None
    """
    print()
    print(count, "numbers were entered.")
    print("The sum is", total)
    if count > 0:
        print("The average is", total / count)
    print(smallest, "was the smallest number entered.")
    print(biggest, "was the biggest number entered.")

main()
