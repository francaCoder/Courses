# Create a code that read how much money the people have in your wallet and converter
# R$ in $

money = float(input("How much money you have in your wallet? R$"))
converter = money / 5.57

print("Considering that 1 Dollar today is equal R$5,57  you have: ")
print("{:.2f} Dollars.".format(converter))
