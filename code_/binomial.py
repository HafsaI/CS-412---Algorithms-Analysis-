### Modification to code taken from https://www.geeksforgeeks.org/eggs-dropping-puzzle-binomial-coefficient-and-binary-search-solution/ ###


def binomialCoeff(trials, eggs, floors):
    '''
    Calculates the sum of the binomial coefficients
    '''

    ans = 0
    term = 1
    i = 1
    while(i <= eggs and ans < floors):
        term *= trials - i + 1
        term /= i
        ans += term
        i += 1
    return ans


def eggDropBinomial(eggs, floors):
    '''
    Function to get minimum number of trials needed in worst
    case with n eggs and k floors with binomial approach
    '''

    # first floor - f
    # last floor  - l
    f = 1
    l = floors

    # binary search, for each pivot find the
    # sum of binomial coefficient and check if < floors
    while (f < l):

        mid = int((f + l) / 2)

        if (binomialCoeff(mid, eggs, floors) < floors):
            f = mid + 1
        else:
            l = mid

    return int(f)


if __name__ == "__main__":
    eggs = 1
    floors = 10
    print("Minimum number of trials with ",
          eggs, "eggs and", floors, "floors is", eggDropBinomial(eggs, floors))
#Complexity = O(nlogk), where
# k = the number of floors
# n = the number of eggs
