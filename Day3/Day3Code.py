import string
# Read in Input
packInput = open('./input.txt', 'r')
allPacks = packInput.readlines()

# Variable Setup
total = 0
letterDict = dict(zip(string.ascii_lowercase, range(1,27)))
letterDict.update(dict(zip(string.ascii_uppercase, range(27, 53))))

# Part 1
for pack in allPacks:
    length = len(pack)
    middle = length//2
    firstHalf = pack[:middle]
    secondHalf = pack[middle:]
    firstSet = set(firstHalf)
    secondSet = set(secondHalf)
    commonCharacter = firstSet.intersection(secondSet)
    total += letterDict[list(commonCharacter)[0]]

print("Part 1: ", total)
# Part 2
thisGroup = []
total = 0
for pack in allPacks:
    thisGroup.append(pack)
    if len(thisGroup) == 3:
        firstPack = set(thisGroup[0])
        secondPack = set(thisGroup[1])
        thirdPack = set(thisGroup[2])
        commonCharacter = firstPack.intersection(secondPack, thirdPack)
        commonList = list(commonCharacter)
        if len(commonList) == 2:
            commonList.remove('\n')
        total += letterDict[commonList[0]]
        thisGroup.clear()

print('Second Part: ', total)

