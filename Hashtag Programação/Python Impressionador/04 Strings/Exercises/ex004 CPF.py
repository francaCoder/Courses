"""
Create a program that will receive a user's CPF and will verify if the CPF is just numbers and has 11 characters. For each condition that is 'False' return a message according to context
"""

# print("(just numbers)")
# cpf = input("CPF: ")
# print(len(cpf))
# if len(cpf) == 11 and cpf.isnumeric():
#     print("Access allowed")
# else:
#     print("Type a valid CPF")


# Error Handling
cpf = input("CPF: ").strip()
cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")
if len(cpf) == 11 and cpf.isnumeric():
    print("Access allowed")
else:
    print("Type a valid CPF")
