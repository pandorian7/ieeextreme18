N = int(input())

center = None

def update_center(p):
    global center
    if center is None:
        center = p
    else:
        center = ((center[0] + p[0])/2, (center[1] + p[1])/2)


def sqr_dist_from_c(p):
    return (center[0] - p[0])**2 + (center[1] - p[1])**2


cds = [tuple([*map(int, input().split()), i]) for i in range(N)]

for p in cds:
    update_center(p)

dists = list(map(sqr_dist_from_c, cds))

zipped = list(zip(dists, cds))

zipped.sort(key=lambda x: x[0])

grouped = zip(zipped[0::3], zipped[1::3], zipped[2::3])

for group in grouped:
    print(" ".join(str(x[1][2]) for x in group))