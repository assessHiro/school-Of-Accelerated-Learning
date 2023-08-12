import random

class Bull:
    def __init__(self, speed, group=None):
        self.speed = speed
        self.group = group

def race(bulls):
    return sorted(bulls, key=lambda x: x.speed, reverse=True)

# Create 25 bulls with varying speeds.
bulls = [Bull(random.uniform(1,100)) for _ in range(25)]

# Step 1: Divide bulls into groups and conduct first 5 races
groups = [bulls[i:i+5] for i in range(0, 25, 5)]
for i in range(5):
    groups[i] = race(groups[i])[:3]  # Keep only the top 3 bulls in each group

# Step 2: Conduct 6th race and eliminate bulls
winners = [group[0] for group in groups]  # Winners from each group
result = race(winners)
fastest_bull = result[0]

# Prepare for 7th race
candidates = [result[1], result[2], result[1].group[1], result[0].group[1], result[0].group[2]]

# Step 3: Conduct 7th race
result = race(candidates)
second_fastest_bull = result[0]
third_fastest_bull = result[1]

# Fastest 3 bulls
print([fastest_bull.speed, second_fastest_bull.speed, third_fastest_bull.speed])