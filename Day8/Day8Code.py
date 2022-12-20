def part1(allTreeLines):
    visibleTrees = 198 + (97 * 2)
    for lineNumber in range(1, 98):
        for treeNumber in range(1, 98):
            thisTreeHeight = allTreeLines[lineNumber][treeNumber]
            visible = True

            # Check Left:
            variableCheck = treeNumber - 1
            while variableCheck >= 0 and visible:
                if allTreeLines[lineNumber][variableCheck] >= thisTreeHeight:
                    visible = False
                variableCheck -= 1
            if visible:
                visibleTrees += 1
                continue

            visible = True
            # Check Right
            variableCheck = treeNumber + 1
            while variableCheck <= len(allTreeLines[lineNumber]) - 1 and visible:
                if allTreeLines[lineNumber][variableCheck] >= thisTreeHeight:
                    visible = False
                variableCheck += 1
            if visible:
                visibleTrees += 1
                continue

            visible = True
            # Check Down
            variableCheck = lineNumber + 1
            while variableCheck <= len(allTreeLines) - 1 and visible:
                if allTreeLines[variableCheck][treeNumber] >= thisTreeHeight:
                    visible = False
                variableCheck += 1
            if visible:
                visibleTrees += 1
                continue

            visible = True
            # Check Up:
            variableCheck = lineNumber - 1
            while variableCheck >= 0 and visible:
                if allTreeLines[variableCheck][treeNumber] >= thisTreeHeight:
                    visible = False
                variableCheck -= 1
            if visible:
                visibleTrees += 1
                continue
    return visibleTrees

def part2(allTreeLines):
    allVisibilityScores = []
    for lineNumber in range(1, 98):
        for treeNumber in range(1, 98):
            leftDistance = 0
            rightDistance = 0
            downDistance = 0
            upDistance = 0
            thisTreeHeight = allTreeLines[lineNumber][treeNumber]
            visible = True

            # Check Left:
            variableCheck = treeNumber - 1
            while variableCheck >= 0 and visible:
                if allTreeLines[lineNumber][variableCheck] >= thisTreeHeight:
                    visible = False
                leftDistance += 1
                variableCheck -= 1

            visible = True
            # Check Right
            variableCheck = treeNumber + 1
            while variableCheck <= len(allTreeLines[lineNumber]) - 1 and visible:
                if allTreeLines[lineNumber][variableCheck] >= thisTreeHeight:
                    visible = False
                rightDistance += 1
                variableCheck += 1

            visible = True
            # Check Down
            variableCheck = lineNumber + 1
            while variableCheck <= len(allTreeLines) - 1 and visible:
                if allTreeLines[variableCheck][treeNumber] >= thisTreeHeight:
                    visible = False
                downDistance += 1
                variableCheck += 1

            visible = True
            # Check Up:
            variableCheck = lineNumber - 1
            while variableCheck >= 0 and visible:
                if allTreeLines[variableCheck][treeNumber] >= thisTreeHeight:
                    visible = False
                upDistance += 1
                variableCheck -= 1
            thisVisibilityScore = leftDistance * rightDistance * downDistance * upDistance
            allVisibilityScores.append(thisVisibilityScore)
    return max(allVisibilityScores)


treeInput = open('./input.txt', 'r')
allTreeLinesInput = treeInput.readlines()
print(part1(allTreeLinesInput))
print(part2(allTreeLinesInput))

