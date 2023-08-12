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

    print(total_races)


min_races()
