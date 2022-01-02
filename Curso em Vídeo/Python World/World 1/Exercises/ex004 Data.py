# Create a code that read something and show on screen your type and all informations
# about this value

value = input("Type something: ")
print('Primitive type?', type(value))
print('Alphanumeric?', value.isalnum())
print('Alpha?', value.isalpha())
print('Numeric?', value.isnumeric())
