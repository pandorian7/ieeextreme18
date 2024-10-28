n = int(input())

ranges = [range(*map(int, input().split())) for _ in range(n)]


filtered = list()

def ranges_overlap(range1, range2):
    # Get the start and end of each range, adjusting stop to be inclusive
    start1, end1 = range1.start, range1.stop - 1
    start2, end2 = range2.start, range2.stop - 1

    # Check if ranges overlap or are adjacent
    return start1 <= end2 and start2 <= end1

def intersect_ranges(range1, range2):
    # Get the start and end of each range, adjusting stop to be inclusive
    start1, end1 = range1.start, range1.stop - 1
    start2, end2 = range2.start, range2.stop - 1

    # Find the intersection boundaries
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)

    # Check if there's an actual intersection
    if intersection_start <= intersection_end:
        return range(intersection_start, intersection_end + 1)  # +1 to make it inclusive
    
    # If there's no overlap, return None
    return None

for r in ranges:
    does_overlap = False
    for i, f in enumerate(filtered):
        overlap = intersect_ranges(r, f)
        if overlap:
            filtered[i] = overlap
            does_overlap = True
    if not does_overlap:
        filtered.append(r)
    

if len(filtered) > 2:
    print(-1)
else:
    temps = [f.start for f in filtered]
    temps.sort()
    print(" ".join(map(str, temps)))
 
