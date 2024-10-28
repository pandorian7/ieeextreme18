L, N, M = map(int, input().split())

UP = "U"
RIGHT = "R"
LEFT = "L"

A_U = list()
A_R = list()
B_U = list()
B_L = list()

nA = N
nB = M

for i in range(N):
    direction, distance = input().split()
    distance = int(distance)
    if direction == UP:
        A_U.append(distance)
    elif direction == RIGHT:
        A_R.append(distance)
    else:
        raise ValueError("Invalid direction")

for i in range(M):
    direction, distance = input().split()
    distance = int(distance)
    if direction == UP:
        B_U.append(distance)
    elif direction == LEFT:
        B_L.append(distance)
    else:
        raise ValueError("Invalid direction")
    
count = (N+1) * (M+1)

def find_max_index_leq(nums, target: int) -> int:
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            result = mid  # update the result with the current index
            left = mid + 1  # search in the right half to find a larger value within the limit
        else:
            right = mid - 1  # search in the left half

    return result

B_U.sort()

for Ai in A_U:
    non_crossing = filter(lambda Bi: Bi>=Ai, B_U)
    # print(len(list(non_crossing)), find_max_index_leq(B_U, Ai) + 1)
    count -= find_max_index_leq(B_U, Ai) + 1
    # count -= len(list(non_crossing))

print(count)





