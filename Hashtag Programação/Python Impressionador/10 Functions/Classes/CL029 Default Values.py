products = ["Cell", "Iphone", "Ipad", "Tv", "Airpods"]

def my_function(arg=False): # False = default value
    pass

def standardize_codes(codes, pattern="m"):
    for i, code in enumerate(codes):
        code.replace("  ", "")
        code.strip()
        if pattern == "m":
            code = code.lower()
        elif pattern == "M":
            code = code.upper()
        codes[i] = code
    return codes


code_products = ["ABC12", "abc34", "abc37"]
print(standardize_codes(code_products, "M"))