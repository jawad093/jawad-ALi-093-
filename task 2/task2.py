movies = [
    ("The Midnight Chronicles", 15000000),
    ("Shadow Memories", 12000000),
    ("Whispers of the Ocean", 8000000),
    ("Galaxy Rangers: Beyond the Stars", 400000000),
    ("Legends of Eternity", 380000000),
    ("Chronicles of Valor", 360000000),
    ("The Phoenix Saga", 220000000)
]

total_budget = 0 
for title, budget in movies:
    total_budget += budget 

average_budget = total_budget / len(movies)
print(f'Average budget: {average_budget}')

for title, budget in movies:
    if budget > average_budget:
        print(f"{title} has a higher budget, {int(budget - average_budget)} more than the average.")








