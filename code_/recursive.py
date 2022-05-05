
### Modification to code taken from https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/ ###

import sys


def eggDropRecursive(eggs, floors):
    ''' Function to get minimum number of trials
        needed in worst case with some eggs and floors '''

    # no floors / one floor
    if (floors == 1 or floors == 0):
        return floors

    # k trials for one egg
    if (eggs == 1):
        return floors

    minValue = sys.maxsize

    # from 1st floor to kth floor
    for x in range(1, floors + 1):

        res = max(eggDropRecursive(eggs - 1, x - 1),
                  eggDropRecursive(eggs, floors - x))
        if (res < minValue):
            minValue = res

    return minValue + 1


if __name__ == "__main__":
    eggs = 2
    floors = 10
    print("Minimum number of trials with ",
          eggs, "eggs and", floors, "floors is", eggDropRecursive(eggs, floors))


# Time Complexity: Exponential: 2 ^k (k = floors)
# Space Complexity: O(1).
