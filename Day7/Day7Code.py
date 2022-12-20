# Read in Input
dirInput = open('./input.txt', 'r')
lines = []
while True:
    line = dirInput.readline()
    if not line:
        break
    else:
        cleanUp = line.replace("\n", "")
        cleanUp = cleanUp.replace("$ ", "")
        if cleanUp != "ls":
            lines.append(cleanUp)

directoryStack = []
directoryValues = {}
for instruction in lines:
    if instruction == "cd ..":
        directoryStack.pop()
    elif instruction[0:2] == "cd":
        newDirectory = instruction.split(" ")[1]
        directoryStack.append(newDirectory)
        if newDirectory not in directoryValues:
            directoryValues[newDirectory] = 0
    elif instruction[0].isnumeric():
        directoryValues[currentDirectory] += int(instruction.split(" ")[0])
    currentDirectory = directoryStack[len(directoryStack)-1]

# We now have what the value of every directory is not including the totals of the directories inside them
secondCurrentStack = []
for instruction in lines:
    if instruction == "cd ..":
        secondCurrentStack.pop()
    elif instruction[0:2] == "cd":
        secondCurrentStack.append(instruction.split(" ")[1])
    elif instruction[0:3] == "dir":
        directoryValues[currentDirectory] += directoryValues[instruction.split(" ")[1]]
    currentDirectory = secondCurrentStack[len(secondCurrentStack)-1]

total = 0
for key in directoryValues.keys():
    if directoryValues[key] <= 100000:
        total += directoryValues[key]
print(total)











