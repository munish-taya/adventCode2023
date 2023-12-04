# Day 2

def stripGameID(line):
    tmp = line.split(":")
    tmp_id = tmp[0].split(" ")
    id = int(tmp_id[1])
    return(id)

def getEachGameOutcome(game):
    tmp = game.split(",")
    idx = 0
    #[red blue green]
    res = [0, 0, 0]
    while idx < len(tmp):
        a = tmp[idx]
        b = a.replace("\n", "")
        tmp2 = b.split(" ")
        if tmp2[2] == 'red':
            res[0] += int(tmp2[1])
        elif tmp2[2] == 'blue':
            res[1] += int(tmp2[1])
        elif tmp2[2] == 'green':
            res[2] += int(tmp2[1])
        else:
            print('error', tmp2)
        idx += 1
    return(res)

def stripGameOutcomes(line):
    tmp = line.split(":")
    games = tmp[1].split(";")
    tot = len(games)
    count = 0
    res = []
    while count < tot:
        res_game = getEachGameOutcome(games[count])
        count += 1
        res.append(res_game)
    return(res)

def verifyValidGame(line):
    check = [12, 14, 13]
    res = stripGameOutcomes(line)
    idx = 0
    valid = 1
    while idx < len(res):
        tmp = res[idx]
        if (tmp[0] > check[0]):
            valid = 0
        if (tmp[1] > check[1]):
            valid = 0
        if (tmp[2] > check[2]):
            valid = 0
        idx += 1
    return(valid)

def findMinSquareGame(line):
    res = stripGameOutcomes(line)
    #print(res)
    idx = 0
    mintmp = [0, 0, 0]
    while idx < len(res):
        tmp = res[idx]
        if (tmp[0] > mintmp[0]):
            mintmp[0] = tmp[0]
        if (tmp[1] > mintmp[1]):
            mintmp[1] = tmp[1]
        if (tmp[2] > mintmp[2]):
            mintmp[2] = tmp[2]
        idx += 1
    #print(mintmp)
    sq = mintmp[0]*mintmp[1]*mintmp[2]
    return(sq)

def sol_part1():
    # using readlines()
    file1 = open('input_day02.txt', 'r')
    Lines = file1.readlines()

    tot = 0
    for line in Lines:
        id = stripGameID(line)
        valid = verifyValidGame(line)
        #print(valid, line)
        if valid:
            tot = tot + id
        #else:
            #print(tot, id, line)

    return (tot)

def sol_part2():
    # using readlines()
    file1 = open('input_day02.txt', 'r')
    Lines = file1.readlines()

    tot = 0
    for line in Lines:
        sq = findMinSquareGame(line)
        tot = tot + sq

    return(tot)

ans1 = sol_part1()
print('Part 1 answer is ', ans1)
ans2 = sol_part2()
print('part2 ans is ', ans2)

#tmp = 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'
#sq = findMinSquareGame(tmp)
#print(sq)