calInput = open('./input.txt', 'r')
allLines = calInput.readlines()
thisElfTotal = 0
bestElfTotal = 0
allTotals = []
for line in allLines:
    if line == '\n':
        if thisElfTotal > bestElfTotal:
            allTotals.append(int(thisElfTotal))
        thisElfTotal = 0
    else:
        thisElfTotal += int(line)
allTotals.sort(reverse=True)
top3 = allTotals[0] + allTotals[1] + allTotals[2]
print('Best Elf: ', allTotals[0], 'Top 3: ', top3)

