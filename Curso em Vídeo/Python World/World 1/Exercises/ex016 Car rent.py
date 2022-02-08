# Make a code that ask how much Km covered by a car rented and the amount of days that
# it was rented. Calculate the total, knowing that the car cost R$60 p/d and R$0,15 per Km

days = int(input("How many days the car stayed rented? "))
km = float(input("How many Km covered? "))
total = (days * 60) + (km * 0.15)

print("You need pay R${}".format(total))


# OR


def car_rent(days=0, km=0):
    total = (days * 60) + (km * 0.15)
    print(f"You need pay R${total}")


car_rent(days=int(input("How many days the car stayed rented? ")), km=float(input("Hoy many km covered? ")))