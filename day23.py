# part 1
import re
lines = open("day23.txt").read().split("\n")
nanobots = list()
for line in lines:
    [x,y,z,r] = list(map(int,re.findall("-?\d+",line)))
    nanobots.append([x,y,z,r])


def mDis(p1, p2):
    return abs(p1[0] - p2[0])+ abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])


maxBots = sorted(nanobots,key=lambda x : x[3])
maxBot = maxBots[len(maxBots)-1]

print(maxBot)

count = 0
for nanobot in nanobots:
    if mDis(nanobot,maxBot) <= maxBot[3]:
        count += 1

print(count)


# part 2



