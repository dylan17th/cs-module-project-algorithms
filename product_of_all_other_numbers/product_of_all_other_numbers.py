'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):

    added_numbers = 0
    number_of_elements = len(arr) - added_numbers
    current_index = 0
    index_getting_added = 0
    numbers_added_together = 1

    if len(arr) == 2:
        arr = [arr[1], arr[0]]
        return arr

    while current_index < number_of_elements:
        if index_getting_added == number_of_elements:
            arr.append(numbers_added_together)
            current_index += 1
            index_getting_added = 0
            added_numbers += 1
            numbers_added_together = 1
        if index_getting_added != current_index:
            numbers_added_together *= arr[index_getting_added]
        index_getting_added += 1

    return arr[number_of_elements:]





if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1,2,3,4,5,5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")


    # def product_of_all_other_numbers(arr):
    # Your code here
    # number_of_elements = len(arr)
    # returned_array = [1] * number_of_elements
    # current_index = 0
    # if len(arr) == 2:
    #     newarray = [arr[1], arr[0]]
    #     return newarray
    # while current_index < number_of_elements:
    #     newArray = []
    #     for i in range(0, number_of_elements):
    #         if i != current_index :
    #             newArray.append(arr[i])
    #     returned_array[current_index] = 1
    #     for i in newArray:
    #         returned_array[current_index] = returned_array[current_index] * i
    #     current_index += 1
    # return returned_array