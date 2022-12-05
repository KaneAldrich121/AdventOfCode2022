from queue import LifoQueue
stackInput = open('./input.txt', 'r')
allInstructions = stackInput.readlines()
# Make all our stacks
stackInfo = []
for i in range(1, 10):
    stackInfo.append([])
# Create Starting Stack in allStacks
for lineOut in range(7, -1, -1):
    thisInputLine = allInstructions[lineOut].replace('\n', "")
    stackNum = 0
    totalCount = 0
    for letter in thisInputLine:
        if letter != " " and letter != "[" and letter != "]":
            stackInfo[stackNum].append(letter)
        totalCount += 1
        if totalCount % 4 == 0:
            stackNum += 1

def part1(allStacks, stackInstructions):
    # Begin Reading in Instructions:
    for line in stackInstructions:
        # Skip Beginning
        if line[0] != "m":
            pass
        # Read Move Instructions
        else:
            thisLine = []
            line += " "
            for index in range(0, len(line)):
                if line[index].isnumeric() and not line[index+1].isnumeric():
                    thisLine.append(int(line[index]))
                elif line[index].isnumeric() and line[index+1].isnumeric():
                    thisLine.append(int(line[index]+line[index+1]))
                else:
                    pass
            if len(thisLine) == 4:
                thisLine.remove(thisLine[1])
            while thisLine[0] > 0:
                moving = allStacks[thisLine[1]-1].pop()
                allStacks[thisLine[2]-1].append(moving)
                thisLine[0] -= 1

    solution = ""
    for stack in allStacks:
        if len(stack) != 0:
            solution += stack[len(stack)-1]
    return solution

def part2(allStacks, stackInstructions):
    for instruction in stackInstructions:
        if instruction[0] != "m":
            pass
        # Split Instruction into numbers
        else:
            thisLine = []
            instruction += " "
            for index in range(0, len(instruction)):
                if instruction[index].isnumeric() and not instruction[index+1].isnumeric():
                    thisLine.append(int(instruction[index]))
                elif instruction[index].isnumeric() and instruction[index+1].isnumeric():
                    thisLine.append(int(instruction[index]+instruction[index+1]))
                else:
                    pass
            if len(thisLine) == 4:
                thisLine.remove(thisLine[1])
            movingStack = []
            while thisLine[0] > 0:
                movingStack.append(allStacks[thisLine[1]-1].pop())
                thisLine[0] -= 1
            movingStack.reverse()
            for box in movingStack:
                allStacks[thisLine[2]-1].append(box)
    solution = ""
    for stack in allStacks:
        if len(stack) != 0:
            solution += stack[len(stack) - 1]
    return solution


# Run one at a time, pass by reference issue I don't have the energy to deal with
print("Part 1: ", part1(stackInfo, allInstructions))
print("Part 2: ", part2(stackInfo, allInstructions))
