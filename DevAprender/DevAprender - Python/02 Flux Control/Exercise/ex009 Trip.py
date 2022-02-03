has_passport = True
ticket_purchased = False
underage = True

# Requirements:
# - A person can only travel if he has a passport, ticket purchased and isn't underage.
if has_passport == True and ticket_purchased == True and underage == True:
    print("Free access")

# - A person can only travel if he has a passport or has a ticket purchased and isn't underage.
if (has_passport == True) or (ticket_purchased == True and underage == True):
    print("Free access")

# - A person can only travel if he doesn't have a passport or has a ticket purchased and isn't underage.
if (not has_passport) or (ticket_purchased == True and underage != False):
    print("Free access")

# - A person can't only travel if he doesn't have a passport or doesn't have a ticket purchased and are underage.
if (not has_passport) or (not ticket_purchased and underage == True):
    print("Free access")

# - A person can only travel if he has a passport and has a ticket purchased and isn't underage.
if has_passport == True and ticket_purchased == True and underage == False:
    print("Free access.")
