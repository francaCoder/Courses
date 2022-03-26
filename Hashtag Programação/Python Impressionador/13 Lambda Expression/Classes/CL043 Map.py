word = "MatHEUs"


def standardize_text(text):
    final_text = text.strip().lower()
    return final_text


result = standardize_text(word)
print(result)

#
print()

products = ["ABC12", "abc34", "abC37", "beb12", "bsa151", "BEB23"]

for i, product in enumerate(products):
    products[i] = standardize_text(product)
print(products)

# Map
print()

products = list(map(standardize_text, products))
print(products)