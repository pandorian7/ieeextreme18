from itertools import combinations
from math import gcd
from functools import reduce
from functools import lru_cache

# Function to calculate LCM of multiple numbers

@lru_cache(maxsize=100000)
def lcm_(a, b):
    return a * b // gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm_, numbers)

# Read inputs
N, K = map(int, input().split())
E = list(map(int, input().split()))

hits = 0

# Apply inclusion-exclusion principle for subsets of all sizes
for r in range(1, K + 1):
    for subset in combinations(E, r):
        lcm_val = lcm_multiple(subset)
        if lcm_val > N:  # If LCM exceeds N, it does not hit any tile
            continue
        tiles_hit = N // lcm_val
        if r % 2 == 1:  # Odd subset size: add
            hits += tiles_hit
        else:           # Even subset size: subtract
            hits -= tiles_hit

print(hits)
