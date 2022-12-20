from collections import Counter

def findStartMarker(input, lengthOfMarker):
    for index in range(0, len(input)):
        thisWindow = input[index:index+lengthOfMarker]
        if len(Counter(thisWindow)) == lengthOfMarker:
            return index + lengthOfMarker
    raise "Could not find solution"


signalInput = open('./input.txt', 'r')
signalLines = signalInput.readlines()[0]
print("Part 1: ", findStartMarker(signalLines, 4))
print("Part 2: ", findStartMarker(signalLines, 14))


