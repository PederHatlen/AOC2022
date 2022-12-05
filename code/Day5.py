def makeCrateMatrix(data):
    crateInput = []
    crateStack = []
    for l in data:
        comp = []
        for i in range(0, len(l), 4):
            comp.append(l[i+1:i+2])
        crateInput.append(comp)
    for i in range(len(crateInput[0])):
        temp = []
        for j in range(len(crateInput)):
            if crateInput[j][i] != " ":
                temp.append(crateInput[j][i])
        crateStack.append(list(reversed(temp)))
    return crateStack

# They are exactly the same, but without reverse in t2

def task1(data):
    part = data.split("\n\n")
    part[0] = part[0].split("\n")
    part[1] = part[1].split("\n")
    crateStack = makeCrateMatrix(part[0])

    for l in part[1]:
        split = l.split(" ")

        amount = int(split[1])
        fStack = int(split[3])-1
        tStack = int(split[5])-1

        crateStack[tStack].extend(list(reversed(crateStack[fStack][-amount:])))
        del crateStack[fStack][-amount:]
    return "".join(list(map(lambda x: x[-1], crateStack)))

def task2(data):
    part = data.split("\n\n")
    crates = part[0].split("\n")
    moves = part[1].split("\n")
    crateStack = makeCrateMatrix(crates)

    for l in moves:
        split = l.split(" ")

        amount = int(split[1])
        fStack = int(split[3])-1
        tStack = int(split[5])-1

        crateStack[tStack].extend(list(crateStack[fStack][-amount:]))
        del crateStack[fStack][-amount:]
    return "".join(list(map(lambda x: x[-1], crateStack)))

if __name__ == "__main__":
    with open("input/Day5.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))