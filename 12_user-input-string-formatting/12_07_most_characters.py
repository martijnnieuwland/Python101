# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

strings = [input("Give us a string: "), input("Give us a string: "), input("Give us a string: ")]

print(f'{max(strings)}, {len(max(strings))}')
