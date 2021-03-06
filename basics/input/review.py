# A simple string example
short_string_variable = "Have a great week, Ninjas!"
print(short_string_variable)

# print the first letter of a string variable,  index 0
first_letter_variable = "New York City"[0]
print(first_letter_variable)

# Mixed upper and lower case letter variable
mixed_letter_variable = "This ia a MiXeD vArIaBlE"
print(mixed_letter_variable.lower())

# lenght of the variable
print(len(mixed_letter_variable))

# Use '+' sign inside a print command
first_name = 'Joy'
print("first name is : " +first_name)

# Replace a part of a string
first_serial_number = "ABC123"
print("Changed serial number : " +first_serial_number.replace('123' , '456'))

# Replace a part of a string -> Twice
second_serial_number = "ABC123ABC"
print("Changed serial number : " +second_serial_number.replace('ABC' , 'ZZZ' ,2))

# Take a part of a variable, according to specific index range
range_of_indexes = second_serial_number[0:3]
print(range_of_indexes)

# One last thing - adding spaces between multiple variables in print
first_word = "Thank "
second_word = "you "
third_word = "NINJAS !"

print(first_word+second_word+third_word)