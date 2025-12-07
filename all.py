import math
from collections import Counter

###########################################################
# EXAMPLE 1: THE MYSTERY FRUIT
###########################################################
print("\n--- EXAMPLE 1: THE MYSTERY FRUIT ---")

# Our tiny dataset
fruits = [
    {"name": "Apple A", "sweetness": 10, "crunchiness": 9},
    {"name": "Apple B", "sweetness": 9,  "crunchiness": 8},
    {"name": "Pear A",  "sweetness": 3,  "crunchiness": 7},
    {"name": "Pear B",  "sweetness": 4,  "crunchiness": 6},
    {"name": "Pear C",  "sweetness": 5,  "crunchiness": 7},
]

# Mystery fruit
mystery = {"sweetness": 6, "crunchiness": 4}

# take 2 fruits and calc eclidean distance between them
def euclidean_distance(f1, f2):
    return math.sqrt(
        (f1["sweetness"] - f2["sweetness"])**2 +
        (f1["crunchiness"] - f2["crunchiness"])**2
    )

# calc distances
distances = []
for fruit in fruits:
    d = euclidean_distance(mystery, fruit)
    distances.append((fruit["name"], fruit["name"].split()[0], d))  
    # ("Apple A", "Apple", 3.2)

# sort by distance
distances.sort(key = lambda x: x[2])

# set k = 3 , aka nearest 3 neighbors
k = 3
nearest = distances[:k]

print("Nearest neighbors:")
for n in nearest:
    print(f"{n[0]} -> distance: {n[2]:.2f}")

# majority vote
labels = [n[1] for n in nearest]
vote = Counter(labels).most_common(1)[0][0]

print("\nPrediction:", vote) 


###########################################################
# EXAMPLE 2: THE HOUSE PRICE PREDICTION EXAMPLE
###########################################################
print("\n--- EXAMPLE 2: THE HOUSE PRICE PREDICTION EXAMPLE ---")

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


###########################################################
# EXAMPLE 3: T-SHIRT SIZE (WITH NORMALIZATION)
###########################################################
print("\n--- EXAMPLE 3: T-SHIRT SIZE RECOMMENDATION ---")

# for each customer -> entry: (height, weight, size)
customers = [
    (170, 65, "M"),
    (180, 75, "L"),
    (160, 55, "S"),
    (175, 70, "M"),
    (185, 85, "L"),
    (165, 60, "S"),
    (172, 68, "M"),
    (190, 95, "L"),
]

# simple min-max normalization
def normalize_dataset(data):
    heights = [h for h, _, _ in data]
    weights = [w for _, w, _ in data]
    
    min_h = min(heights)
    max_h = max(heights)
    min_w = min(weights)
    max_w = max(weights)
    
    normalized = []
    for h, w, s in data:
        nh = (h - min_h) / (max_h - min_h)
        nw = (w - min_w) / (max_w - min_w)
        normalized.append((nh, nw, s))
    
    return normalized, min_h, max_h, min_w, max_w

normalized_customers, min_h, max_h, min_w, max_w = normalize_dataset(customers)

# normalize a single new user
def normalize_user(height, weight):
    nh = (height - min_h) / (max_h - min_h)
    nw = (weight - min_w) / (max_w - min_w)
    return (nh, nw)

# New user: 175 cm, 80 kg
user = normalize_user(175, 80)

# calculating the distance between two points using euclidean
def euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# find the k nearest neighbors
k = 3
distances = []

for h, w, s in normalized_customers:
    d = euclidean(user, (h, w))
    distances.append((d, s))

# sort by distance and grab the closest K
distances.sort()
neighbors = distances[:k]

# majority vote for size
sizes = [size for _, size in neighbors]
recommended = Counter(sizes).most_common(1)[0][0]

print("Nearest neighbors:", sizes)
print("Recommended size:", recommended)
