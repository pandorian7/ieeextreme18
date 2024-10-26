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

for Ai in A_U:
    non_crossing = filter(lambda Bi: Bi>=Ai, B_U)
    count -= len(list(non_crossing))

print(count)





