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

    # Left W = -2, 1, 1
    # Draw = 0, 0, 0
    # Right W = -1, -1, 2

if __name__ == "__main__":
    with open("input/Day2.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))