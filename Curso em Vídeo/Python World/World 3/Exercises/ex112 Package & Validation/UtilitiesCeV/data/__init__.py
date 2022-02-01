def readMoney(msg):
    valid = False
    while not valid:
        inp = str(input(msg)).strip().replace(",", ".")
        if inp.isalpha():
            print(f"[ERROR] << {inp} >> is invalid!")
        else:
            valid = True
            return float(inp)