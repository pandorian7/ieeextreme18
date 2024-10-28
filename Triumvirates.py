from collections import defaultdict

N = int(input())

cds = [tuple([*map(int, input().split()), i]) for i in range(N)]

# distmap = defaultdict(dict)
distmap = defaultdict(list)

def sqr_dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

for i in range(N):
    for j in range(i+1, N):
        dist = sqr_dist(cds[i], cds[j])
        distmap[i].append((j, dist))
        distmap[j].append((i, dist))

for key in distmap.values():
    key.sort(key=lambda k:k[1])

selected = dict()

for i in range(N):
    if selected.get(i):
        continue
    selected[i] = 1




print(distmap)

