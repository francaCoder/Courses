goal = 10000
sales = {
    "João": 8000,
    "Marcos": 9000,
    "Matheus": 10000,
    "Eduardo": 11000,
    "Guilherme": 12000,
    "Renan": 13000,
    "Igor": 7000,
    "Douglas": 6000,
    "Carlos": 14000,
    "Bruno": 5000,
}

def calculate_goal(goal, sellers):
    reached_goal = []
    for seller in sellers:
        if sales[seller] >= goal:
            reached_goal.append(seller)
    percentage = len(reached_goal) / len(sales)
    return reached_goal, percentage


final_sellers, perc_sellers = calculate_goal(goal, sales)
print(final_sellers)
print(perc_sellers)