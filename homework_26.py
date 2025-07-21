# Exercise.1

# import pickle
#
# with open("data.pkl", "rb") as f:
#     odd_numbers = pickle.load(f)
#
# divisible_by_3 = [num for num in odd_numbers if num % 3 == 0]
#
# average = sum(divisible_by_3) / len(divisible_by_3)
# print("Average: ", average)

# Exercise.2

# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dict_2 = {value: len(value) for value in dict_1.values()}
#
# print(dict_2)

# Exercise.3

def filter_odd_values(input_dict):
    filtered_dict = {key: [num for num in value if num % 2 != 0]
                     for key, value in input_dict.items()}
    return filtered_dict

original_dict = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
result = filter_odd_values(original_dict)
print(result)
