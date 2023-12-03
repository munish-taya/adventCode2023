# Code of advent 2023
# Day 1, problem 1

def processOneString(line):
    firstNum = -1
    lastNum = 0
    for char in line:
        if char.isnumeric():
            num = int(char)
            if firstNum < 0:
                firstNum = num
            lastNum = num
    numFull = 10*firstNum + lastNum
    return(numFull)

def findNumerics(line):
    firstNum = -1
    lastNum = 0
    idx = 0
    for char in line:
        if char.isnumeric():
            num = int(char)
            if firstNum < 0:
                firstNum = num
                firstIdx = idx
            lastNum = num
            lastIdx = idx
        idx += 1
    return(firstNum, firstIdx, lastNum, lastIdx)

def findFirstStringNumber(new_str):
    idx1 = new_str.find('one')
    idx2 = new_str.find('two')
    idx3 = new_str.find('three')
    idx4 = new_str.find('four')
    idx5 = new_str.find('five')
    idx6 = new_str.find('six')
    idx7 = new_str.find('seven')
    idx8 = new_str.find('eight')
    idx9 = new_str.find('nine')
    tmp = [idx1, idx2, idx3, idx4, idx5, idx6, idx7, idx8, idx9]

    out = -1
    i = 0
    valid = 0
    firstIdx = 99999
    while i < len(tmp):
        if (-1 < tmp[i] < firstIdx):
            valid = 1
            firstIdx = tmp[i]
            out = i
        i += 1
    if valid:
        out = out + 1
    return(out, firstIdx)

def findLastStringNumber(new_str):
    idx1 = new_str.rfind('one')
    idx2 = new_str.rfind('two')
    idx3 = new_str.rfind('three')
    idx4 = new_str.rfind('four')
    idx5 = new_str.rfind('five')
    idx6 = new_str.rfind('six')
    idx7 = new_str.rfind('seven')
    idx8 = new_str.rfind('eight')
    idx9 = new_str.rfind('nine')
    idx9 = new_str.rfind('nine')
    tmp = [idx1, idx2, idx3, idx4, idx5, idx6, idx7, idx8, idx9]

    out = -1
    i = 0
    valid = 0
    lastIdx = -1
    while i < len(tmp):
        if (tmp[i] > lastIdx):
            valid = 1
            lastIdx = tmp[i]
            out = i
        i += 1
    if valid:
        out = out + 1
    return(out, lastIdx)

def  findNum_part2(tmp):
    firstStr, firstIdxStr = findFirstStringNumber(tmp)
    lastStr, lastIdxStr = findLastStringNumber(tmp)
    #print(firstStr, firstIdxStr)
    #print(lastStr, lastIdxStr)

    firstNum, firstIdx, lastNum, lastIdx = findNumerics(tmp)
    #print(firstNum, firstIdx)
    #print(lastNum, lastIdx)

    if firstIdxStr < firstIdx:
        first = firstStr
    else:
        first = firstNum

    if lastIdxStr > lastIdx:
        last = lastStr
    else:
        last = lastNum

    num = 10*first + last
    return(num)

def sol_part1():
    # using readlines()
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    tot = 0
    for line in Lines:
        count += 1
        num = processOneString(line)
        tot = tot + num
    return(tot)

def sol_part2():
    # using readlines()
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()

    tot = 0
    for line in Lines:
        num = findNum_part2(line)
        #print(line, num)
        tot = tot + num
    return (tot)



ans1 = sol_part1()
print('Part 1 answer is ', ans1)
ans2 = sol_part2()
print('Part 2 answer is ', ans2)

#tmp = 'ftjjqbgphtmhthreesix1six'
#num = findNum_part2(tmp)
#print(num)

