# THE MYSTERY FRUIT


import math
from collections import Counter

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
