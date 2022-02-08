# You can't add or remove values inside a tuple

site1 = "Youtube"
site2 = "Facebook"
site3 = "Instagram"
#
value1 = 23
value2 = 43
value3 = 65

sites = ("Youtube", "Facebook", "Instagram")
values = (23, 43, 65)

print(sites[2])

# I can join tuples

data = sites + values
print(data)