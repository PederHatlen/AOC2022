# Using the ord function to get ascii values for the charracters
# Makes the math a lot easier with predone calculations
    # actions =   R  P  S
    # Left W  =  -2  1  1
    # Draw    =   0  0  0
    # Right W =  -1 -1  2
def task1(data):
    arr = list(map(lambda x: x.split(" "), data.split("\n")))
    sum = 0
    for i in arr:
        # Calculate results by normalizing and comparing too calculation (Found over)
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
        # Reversing the function to get right move
        # Done by adding score to left move, and taking modulo
        sum += ((ord(i[1])-88)*3) + res[((ord(i[0])-65) + (ord(i[1])-89))%3]
    return sum

if __name__ == "__main__":
    with open("input/Day2.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))