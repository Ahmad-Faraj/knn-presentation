import math
from collections import Counter

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
