def part1(target, depth):
    modulo = 20183
    [x, y] = target
    x += 150
    y += 150


    # erosion level =  (geologicIndex  + depth) % modulo
    # type = erosion level % 3

    # compute geologic Index
    geoIndex = list()
    for r in range(x+1):
        rowIndex = list()
        for c in range(y+1):
            if r == 0:
                geologicIndex = c * 48271
                erosionLevel = (geologicIndex + depth) % modulo
                rowIndex.append(erosionLevel)
            elif c == 0:
                geologicIndex = r*16807
                erosionLevel = (geologicIndex + depth) % modulo
                rowIndex.append(erosionLevel)
            else:
                erosionLevel = (geoIndex[r-1][c] * rowIndex[c-1] + depth) % modulo
                rowIndex.append(erosionLevel)
        # for index in rowIndex:
        #     print(rowIndex)
        geoIndex.append(rowIndex)

    geoIndex[x][y] = (0 + depth) % modulo

    # compute type: 0 rocky, 1 wet, 2 narrow
    typeIndex = [[0] * (y+1) for i in range(x+1)]
    for r in range(x+1):
        for c in range(y+1):
            typeIndex[r][c] = geoIndex[r][c]% 3
    # compute risk level of this area
    riskLevel = 0
    for r in range(x+1):
        for c in range(y+1):
            riskLevel += typeIndex[r][c]

    print("risk level is :", riskLevel)

    # part 2 使用队列的广度优先遍历法：have some problems
    import heapq
    # Equipment : Neither: 0 Torch:1 Climing: 2
    # RegionType: Rocky  ：0 Wet  :1 Narrow : 2
    queue = [(0, 0, 0, 1)] #(minutes, x,y,e)]
    best = dict() #(x,y,e) : minutes
    finalTarget = (target[0], target[1], 1)
    while queue:
        minutes, xx, yy, e = heapq.heappop(queue)
        best_key = (xx, yy, e)
        # 如果这个位置已经在best里面了，best里面对应的时间更短，那么就继续吧
        if best_key in best and best[best_key] <= minutes:
            continue
        # 否则，更新best里面对应位置的时间
        best[best_key] = minutes

        # 终止条件
        if best_key == target:
            print(minutes)
            break
        # 获取周围可选择步骤：上下左右四步
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            newx = xx + dx
            newy = yy + dy
            # 不能超出边界，负值代表是墙，通过不了
            if newx < 0 or newy < 0:
                continue
            # 更新到邻居需要付出的代价
            for ne in range(3):
                if ne != typeIndex[xx][yy] and ne != typeIndex[newx][newy]:
                    heapq.heappush(queue, (minutes+7, newx, newy, ne))
                else:
                    heapq.heappush(queue, (minutes+1, newx, newy, ne))

def main():
    depth = 3066
    target = [13, 726]
    part1(target, depth)


if __name__ == "__main__":
    main()