def part1(cheatSheet):
    total = 0
    thisGame = 0
    pointVals = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
    losses = {'X': 'B', 'Y': 'C', 'Z': 'A'}
    for game in cheatSheet:
        thisGame += pointVals[game[2]]
        if pointVals[game[0]] == pointVals[game[2]]:
            thisGame += 3
            total += thisGame
        else:
            if game[0] == losses[game[2]]:
                total += thisGame
            else:
                thisGame += 6
                total += thisGame
        thisGame = 0
    return total


def part2(cheatSheet):
    total = 0
    thisGame = 0
    pointVals = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
    # Maps Opponent Choice to What I Should Play to Beat Them
    losses = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    # Maps Opponent Choice to What I Should Play to Lose to Them
    wins = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    for game in cheatSheet:
        # Drawing
        if game[2] == 'Y':
            thisGame += 3
            thisGame += pointVals[game[0]]
        # Winning
        elif game[2] == 'Z':
            thisGame += 6
            thisGame += pointVals[losses[game[0]]]
        # Losing
        else:
            thisGame += pointVals[wins[game[0]]]
        total += thisGame
        thisGame = 0
    return total




gameInput = open('./input.txt', 'r')
allGames = gameInput.readlines()
print(part1(allGames))
print(part2(allGames))
