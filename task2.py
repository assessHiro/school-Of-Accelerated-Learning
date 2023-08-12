import random
from typing import *
from itertools import combinations


NO_OF_BULLS:Final[int] = 25
GROUP_LENGTH: Final[int] = 5

class Bull:
    def __init__(self, speed, group=None):
        self.speed = speed
        self.group = group


def race(bulls: List[Bull]):
    return sorted(bulls, key=lambda x: x.speed, reverse=True)[:3]




bulls = [Bull(random.uniform(1, 100)) for _ in range(NO_OF_BULLS)]

random.shuffle(bulls)

groups = [bulls[i:i+GROUP_LENGTH] for i in range(0, len(bulls), GROUP_LENGTH)]
for i in range(len(gro)):
    groups[i] = race(groups[i])


for i in range(len(groups)):
    top_3 = race(groups[i])
    groups[i] = top_3


# Step 2: Conduct 6th race and eliminate bulls
winners = [group[0] for group in groups]  # Winners from each group
result = race(winners)
fastest_bull = result[0]

# Prepare for 7th race
candidates = [result[1], result[2], result[1].group[1],
              result[0].group[1], result[0].group[2]]

# Step 3: Conduct 7th race
result = race(candidates)
second_fastest_bull = result[0]
third_fastest_bull = result[1]

# Fastest 3 bulls
print([fastest_bull.speed, second_fastest_bull.speed, third_fastest_bull.speed])
