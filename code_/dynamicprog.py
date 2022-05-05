### Modification to code taken from https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/ ###

from decimal import FloatOperation


INT_MAX = 32767


def eggDropDynamic(eggs, floors):
    '''
    Function to get minimum number of trials needed in worst
    case with n eggs and k floors with dynamic approach
    '''

    eggFloor = [[0 for x in range(floors + 1)] for x in range(eggs + 1)]
    # A 2D table with eggFloor[i][j] representing minimum number of trials

    for i in range(1, eggs + 1):
        eggFloor[i][1] = 1   # 1 trial for 1 floor
        eggFloor[i][0] = 0   # 0 trials for 0 floor

    for j in range(1, floors + 1):
        eggFloor[1][j] = j  # j trials for one egg and j floors.

    for i in range(2, eggs + 1):
        for j in range(2, floors + 1):
            eggFloor[i][j] = INT_MAX
            for x in range(1, j + 1):
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res

    return eggFloor[eggs][floors]  # eggFloor[n][k] holds the result


'''Driver program'''
if __name__ == "__main__":
    eggs = 1
    floors = 100
    print("Minimum number of trials in worst case with " + str(eggs) + " eggs and "
          + str(floors) + " floors is " + str(eggDropDynamic(eggs, floors)))

# Time Complexity: O(n*k^2)
# n = number of eggs
# k = number of floors

# Auxiliary Space: O(n*k).
