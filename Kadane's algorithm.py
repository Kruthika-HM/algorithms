#KADEN's algorithm to find maximum subarray
"""according to this algorithm it gives the contigious list of array elements which gives the maximum sum"""

def kd_algorithm(list_of_numbers):
    if not list_of_numbers:
        return 0

    max = list_of_numbers[0]
    best_start = 0
    best_end = 0

    current = list_of_numbers[0]
    current_start = 0

    for value in range(1, len(list_of_numbers)):
        value = list_of_numbers[i]
        
        if value > current + value:
            current = value
            current_start = value
        else:
            current = current + value

        if current_max > max:
            max = current
            best_start = current_start
            best_end = value
            
    subarray = list_of_numbers[best_start : best_end + 1]
    
    return max, subarray

inputed_list = input("enter the comma seperated numbers only: ")
modified_list = inputed_list.split(",")

try:
    list_of_numbers = [int(num_str.strip()) for num_str in modified_list]
    result = kd_algorithm(list_of_numbers)
    print(f"\nThe maximum sum and subarray of the given list is: {result}")
except ValueError:
    print("\nInvalid input: Please ensure all entries are valid numbers.")







