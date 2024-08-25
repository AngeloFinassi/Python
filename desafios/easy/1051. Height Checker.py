heights = [1,1,4,2,1,3]
expected = sorted(heights)

d = 0
for c in range(0, len(heights)):
    if heights[c] != expected[c]:
        d += 1

print(d)