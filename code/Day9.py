import numpy

def task1(data):
    # Initialize the head and tail x, y arrays
    # And their backstorage arrays
    h, t = [0, 0], [0, 0]
    headMoves = [[0,0]]
    tailMoves = [[0,0]]
    for l in data.split("\n"):
        move = l.split(" ")
        for i in range(1, int(move[1])+1):
            # Moving the head to the new possition
            # Last possition + point delta
            pd = [0, 0] # point delta
            if move[0] == "L": pd[0] -= 1
            elif move[0] == "R": pd[0] += 1
            elif move[0] == "U": pd[1] += 1
            elif move[0] == "D": pd[1] -= 1
            h = [h[0] + pd[0], h[1] + pd[1]]

            headMoves.append(h)

            # If head is close to tails, put tails = last heads value
            # This works if you only have one joint
            if abs(h[0]-t[0]) > 1 or abs(h[1]-t[1]) > 1:
                t = headMoves[-2]
                tailMoves.append(t)
    # Utilizing set to make the array exclusive, and getting the length
    return len(set(map(lambda x: f"{x[0]}, {x[1]}", tailMoves)))


# Recursive function for moving the tail joints
# Receives the item list and current index
def tailCalc(items, i):  
    hp = items[i-1][-1]
    tp = items[i][-1]

    # If tail is not close, calculate new positon
    if abs(hp[0]-tp[0]) > 1 or abs(hp[1]-tp[1]) > 1:
        pd = [1, 1] # point delta, initialized to 1 for efficiency if diagonal
        # Tail and head on same axis: calc, else: use diagonal calculations
        if hp[0] == tp[0] or hp[1] == tp[1]:
            pd = [(hp[0]-tp[0])//2, (hp[1]-tp[1])//2]
        else:
            if hp[0] < tp[0]: pd[0] = -1
            if hp[1] < tp[1]: pd[1] = -1
        items[i].append([tp[0] + pd[0], tp[1] + pd[1]])

        if len(items) > i+1: return tailCalc(items, i+1)
    # return if the tail is close or last element
    return items

def task2(data):

    items = numpy.zeros(((10,1,2)), dtype=numpy.int8).tolist()
    for l in data.split("\n"):
        move = l.split(" ")

        pd = [0, 0] # Point delta
        if move[0] == "L": pd = [-1,0]
        elif move[0] == "R": pd = [1,0]
        elif move[0] == "U": pd = [0,1]
        elif move[0] == "D": pd = [0,-1]

        for i in range(1, int(move[1])+1):
            # Calc actual head first
            items[0].append([items[0][-1][0] + pd[0], items[0][-1][1] + pd[1]])
            items = tailCalc(items, 1)
        
    # Utilizing set to make the array exclusive, and getting the length
    return len(set(map(lambda x: f"{x[0]}, {x[1]}", items[-1])))

if __name__ == "__main__":
    with open("input/Day9.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))