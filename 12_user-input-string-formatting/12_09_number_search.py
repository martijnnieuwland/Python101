# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

number = int(input("Give me a number between 0 and 1,000,000,000: "))

i = 1
while True:
    if i == number:
        print(i)
        break
    i += 1
