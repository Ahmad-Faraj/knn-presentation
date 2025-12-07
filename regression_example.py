# THE HOUSE PRICE PREDICTION EXAMPLE


import math

# each house: (square_footage , rooms , price)
houses = [
    (2300, 4, 250000),  # house A
    (2550, 3, 260000),  # house B
    (2400, 4, 245000),  # house C
    (2650, 5, 270000),  # house D
    (3000, 4, 310000),  # some extra houses just for realism
    (1800, 3, 200000),
    (2750, 4, 290000)
]

# target house
target = (2500, 4)  # (square_footage, rooms)

# func to calculate Euclidean distance
def distance(house, target):
    size1, rooms1, price1 = house
    size2, rooms2 = target
    return math.sqrt((size1 - size2)**2 + (rooms1 - rooms2)**2)

# compute distance for each house
distances = []
for house in houses:
    d = distance(house, target)
    distances.append((d, house))

# sort houses by distance (nearest first)
distances.sort(key=lambda x: x[0])

# set k = 4 nearest neighbors
k = 4
neighbors = distances[:k]

# extract prices and compute mean
prices = [house[2] for (_, house) in neighbors]
predicted_price = sum(prices) / k

print("Nearest 4 prices:", prices)
print("Predicted price:", predicted_price)
