# Training and Testing
# List 1 - Real property's Price
# List 2 - Real Property's Size
# Let's create a function that receive the lists and divides each one for training and testing

properties_price = [2.17, 1.54, 1.45, 1.94, 2.37, 2.3, 1.79, 1.8, 2.25, 1.37]
properties_size = [207, 148, 130, 203, 257, 228, 160, 194, 232, 147]

# How much will be to testing or training? 10%
factor = 0.1

# My teste list have how many items?
# 9
index = int((1 - factor) * len(properties_price)) # → 9

training_prices = properties_price[:index]
testing_prices = properties_price[index:]

print(training_prices)
print(testing_prices)


def separate_lists(list_values, list_attributes, factor=0.1):
    how_many_values = len(properties_price)
    if how_many_values == len(properties_size):
        index = int(how_many_values - how_many_values * factor)
        print(index, how_many_values)
        list_training_prices = properties_price[:index]
        list_testing_prices = properties_price[index:]
        list_training_attributes = properties_price[:index]
        list_testing_attributes = properties_price[index:]
        return list_training_prices, list_training_attributes, list_testing_prices, list_testing_attributes
    else:
        print("[ERROR] Different sizes")


y_training, x_training, y_testing, x_testing = separate_lists(properties_price, properties_size)
print()
print(x_training)