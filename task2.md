Ever seen a bull race? There are 25 bulls among which you need to find out the fastest 3 bulls.
You can conduct race among at most 5 to find out their relative speed.
At no point you can find out the actual speed of the Bull in a race. 

Find out how many races are required to get the top 3 fastest Bulls. 

### Expected :

- You need to find the minimum number of races that can be done to get the fastest 3 bulls.
- Write down the pseudo code/logic how you would solve this
- Provide a working solution in the language of your choice to achieve this.


# Answer

```python
from typing import *
import math

NO_OF_BULLS: Final[int] = 25
GROUP_LENGTH: Final[int] = 5

NO_OF_WINNERS: Final[int] = 3


def min_races(n: int = NO_OF_BULLS, max_gp_legth: int = GROUP_LENGTH):
    total_races = 0
    no_of_groups = math.ceil(n/max_gp_legth)

    total_races += no_of_groups
    # after race: got 5*5 matrix row: group, column: nth member
    # sort in the order of win

    # race: with 1st column i.e winners of every group a1,a2,a3,a4,a5
    total_races += 1
    # outcome: suppose a1 first

    # race: with a2, a3, b1, b2, c1
    total_races += 1
    # second_winner and 3rd winner: foudn

    # while no_of_groups>1:
    #   no_of_groups = no_of_groups

    print(f"{n},{max_gp_legth}: {total_races}")


min_races() #7 involves matrix construction and decimation
```