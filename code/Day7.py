def createDirStructure(data):
    curDir = []
    dirs = {}
    for l in data.split("\n"):
        s = l.split(" ")
        if s[1] == "cd" and s[2] == "..":
            curDir.pop()
        elif s[1] == "cd":
            curDir.append(s[2])
            dirs["/".join(curDir)] = [[]]
        elif s[0] == "dir":
            dirs["/".join(curDir)].append("/".join(curDir+[s[1]]))
        elif s[0].isnumeric():
            dirs["/".join(curDir)][0].append(int(s[0]))
    return dirs
    
def getFoldersize(dirs, folder):
    for i in dirs[folder][1:]:
        dirs[folder][0] += getFoldersize(dirs, i)
        dirs[folder].remove(i)
    return dirs[folder][0]

def task1(data):
    dirs = createDirStructure(data)
    
    total = 0
    for folder in dirs:
        size = getFoldersize(dirs, folder)
        if sum(size) <= 100000:
            total += sum(size)
    
    return total

    # First try: 1010098, too low
    # Second try: 1138249, too low
    # Third try: 1555642, Correct!

def task2(data):
    dirs = createDirStructure(data)
    
    sizes = []
    for folder in dirs:
        sizes.append(sum(getFoldersize(dirs, folder)))

    sSizes = sorted(sizes, reverse=True)
    for i in range(len(sSizes)):
        if sSizes[i] <= (sizes[0]-40000000):
            return sSizes[i-1]
    
    return None

if __name__ == "__main__":
    with open("input/Day7.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))