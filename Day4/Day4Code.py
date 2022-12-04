def part1():
    # Read in Input
    campInput = open('./input.txt', 'r')
    allGroups = campInput.readlines()

    # Needed Variables
    fullyEnclosedCount = 0
    allInfo = []

    # Splitting Info Loop
    for group in allGroups:
        eachSide = group.split(",")
        eachSide[1] = eachSide[1].replace('\n', "")
        groupInfo = []
        for side in eachSide:
            groupInfo.append(side.split("-"))
        allInfo.append(groupInfo)

    # Checking Bounds Loop
    for group in allInfo:
        # First Start Lower than Second Start and First End Higher than Second End
        if int(group[0][0]) <= int(group[1][0]) and int(group[0][1]) >= int(group[1][1]):
            fullyEnclosedCount += 1
        # Second Start Lower than First Start and Second End Higher than First End
        elif int(group[1][0]) <= int(group[0][0]) and int(group[1][1]) >= int(group[0][1]):
            fullyEnclosedCount += 1
    return fullyEnclosedCount

def part2():
    # Read in Input
    campInput = open('./input.txt', 'r')
    allGroups = campInput.readlines()

    # Needed Variables
    allInfo = []
    partiallyEnclosed = 0

    # Splitting Info Loop
    for group in allGroups:
        eachSide = group.split(",")
        eachSide[1] = eachSide[1].replace('\n', "")
        groupInfo = []
        for side in eachSide:
            groupInfo.append(side.split("-"))
        allInfo.append(groupInfo)

    for group in allInfo:
        # If Start of Group 1 is Later than Start of Group 2 and Earlier than End of Group 2
        if int(group[1][0]) <= int(group[0][0]) <= int(group[1][1]):
            partiallyEnclosed += 1
        # If Start of Group 2 is Later than Start of Group 1 and Earlier than End of Group 1
        elif int(group[0][0]) <= int(group[1][0]) <= int(group[0][1]):
            partiallyEnclosed += 1
    return partiallyEnclosed


print("Part 1: ", part1())
print("Part 2: ", part2())
