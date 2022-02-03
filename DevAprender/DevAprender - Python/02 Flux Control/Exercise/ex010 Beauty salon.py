"""
You are building a system for a beauty salon to calculate the price of a haircut:

- If the hair is between 21cm - 30cm you pay RS50,00
- If the hair is between 31cm - 50cm you pay R$70,00
- Over 50cm consult at reception
"""

cm_hair = 50

# if cm_hair <= 20:
#     print("You need pay R$50,00")
# elif cm_hair <= 21 and cm_hair <= 30:
#     print("You need pay R$70,00")
# elif cm_hair <= 31 and cm_hair <= 50:
#     print("You need pay R$100,00")
# else:
#     print("Please, consult at reception.")


if cm_hair <= 20:
    print("You need pay R$50,00")
elif 21 <= cm_hair <= 30:
    print("You need pay R$70,00")
elif 31 <= cm_hair <= 50:
    print("You need pay R$100,00")
else:
    print("Please, consult at reception.")