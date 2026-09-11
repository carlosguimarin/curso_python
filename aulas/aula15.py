name = input('What is your name? ')
print(f'Hello, {name}!')

number_1 = int(input('Enter a number: '))
number_2 = int(input('Enter another number: '))

print(f'The sum of {number_1} and {number_2} is {number_1 + number_2}')

# If we use int with input, we can broke the program if the user enters a non-integer value.

number_1 = input('Enter a number: ')
number_2 = input('Enter another number: ')

int_number_1 = int(number_1)
int_number_2 = int(number_2)

print(f'The sum of {int_number_1} and {int_number_2} is {int_number_1 + int_number_2}')