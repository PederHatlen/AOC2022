def task1(data):
    arr = list(map(lambda x: x.split(" "), data.split("\n")))
    sum = 0
    for i in arr:
        choice = ord(i[0])+23 - ord(i[1])
        if choice == 0: sum += 3
        elif choice == -1 or choice == 2: sum += 6
        sum += ord(i[1])-87
    return sum

def task2(data):
    arr = list(map(lambda x: x.split(" "), data.split("\n")))
    sum = 0
    res = [1, 2, 3]
    for i in arr:
        sum += ((ord(i[1])-88)*3) + res[((ord(i[0])-65)+(ord(i[1])-89))%3] # Charcodes
    return sum

    # X = Loose
    # Y = Draw
    # Z = Win

    # 1 - 3 = -2, venstre vinner
    # 1 - 2 = -1, høyre vinner
    # 1 - 1 = 0, draw
    # 2 - 3 = -1, høyre vinner
    # 2 - 2 = 0, draw
    # 2 - 1 = 1, venstre vinner
    # 3 - 3 = 0, draw
    # 3 - 2 = 1, venstre vinner
    # 3 - 1 = 2, høyre vinner

    # 1 + 2 = 3
    # 2 -1 = 1

    # Høyre = -1, -1, 2
    # Venstre = -2, 1, 1
    # Draw = 0, 0, 0

if __name__ == "__main__":
    with open("Day2.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))