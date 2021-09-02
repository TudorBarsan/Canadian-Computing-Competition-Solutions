n = int(input())
points = [(0,0)]
for i in range(n):
    x,y = [int(a) for a in input().split()]
    points.append((x,y))

dist = []
for a in range(0, n+1):
    for b in range(a+1, n+1):
        dx = points[a][0] - points[b][0]
        dy = points[a][1] - points[b][1]
        dist.append((dx*dx+dy*dy, a, b))

dist.sort()

best = [0] * (n+1)
pdist = [0] * (n+1)


for pair in dist:
    d = pair[0]
    a = pair[1]
    b = pair[2]

    if a == 0 and d > pdist[b]:
        best[a] = max(best[a], best[b] + 1)
    else:
        pbesta = best[a]
        pbestb = best[b]
        pdista = pdist[a]
        pdistb = pdist[b]
        if d > pdistb and pbesta < pbestb + 1:
            best[a] = pbestb + 1
            pdist[a] = d
        if d > pdista and pbestb < pbesta + 1:
            best[b] = pbesta + 1
            pdist[b] = d

print(best[0])



# n = int(input())
# points = [(0, 0)]
#
# for i in range(n):
#     x, y = [int(a) for a in input().split()]
#     points.append((x, y))
#
# dist = []
#
# for a in range(0, n + 1):
#     for b in range(a + 1, n + 1):
#         xa = points[a][0]
#         xb = points[b][0]
#         ya = points[a][1]
#         yb = points[b][1]
#         distance = (xa-xb) ^ 2 + (ya-yb) ^ 2
#         dist.append((distance, a, b))
#
# dist.sort()
#
# best = [0] * (n + 1)
# last_hop = [0] * (n + 1)
#
# for tup in dist:
#     a = tup[1]
#     b = tup[2]
#     d = tup[0]
#     if a == 0 and d > last_hop[b]:
#         best[a] = max(best[a], best[b] + 1)
#     else:
#         pbest_a = best[a]
#         pbest_b = best[b]
#         plast_hop_a = last_hop[a]
#         plast_hop_b = last_hop[b]
#         if d > plast_hop_b and pbest_a < pbest_b + 1:
#             best[a] = pbest_b + 1
#             last_hop[a] = d
#         if d > plast_hop_a and pbest_b < pbest_a + 1:
#             best[b] = pbest_a + 1
#             last_hop[b] = d
#
# print(best[0])
