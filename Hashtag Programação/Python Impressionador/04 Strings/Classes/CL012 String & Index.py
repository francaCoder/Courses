# Starts from 0
email = "matheus@hotmail.com"
name = "Matheus França"
print(len(email))
print(len(name)) # Len = Length

print(name[0])
print(name[1])


# The last index
print(name[-1])
print(name[-2])

# Parts of a text
print(email[:1])
print(email[:-1])
print(email[:-2])
# : = until

# Show the e-mail from @
print(email.index("@"))
print(email[8:])