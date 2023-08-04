import random

def create_random_list(number_of_elements, min_value, max_value):
    """
    Create a random list with random numbers.

    Parameters:
        number_of_elements (int): The number of elements in the list.
        min_value (int): The minimum value for random integers.
        max_value (int): The maximum value for random integers.

    Returns:
        list: A random list of integers.
    """
    return [random.randint(min_value, max_value) for _ in range(number_of_elements)]

if __name__ == "__main__":
    print("Welcome to the Random List Generator")
    
    while True:
        try:
            number_of_elements = int(input("How many numbers do you want in the list? "))
            min_value = int(input("Enter the minimum value for random numbers: "))
            max_value = int(input("Enter the maximum value for random numbers: "))

            if min_value > max_value:
                print("Error: Minimum value cannot be greater than the maximum value.")
            else:
                random_list = create_random_list(number_of_elements, min_value, max_value)
                print("Random List:", random_list)

        except ValueError:
            print("Error: Please enter valid integer values.")

        choice = input("Do you want to create another random list? (Y/N): ")
        if choice.upper() != 'Y':
            break
