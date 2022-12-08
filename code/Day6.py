def task1(data):
    # A set is a unordered list with unique items
    # So if len(set) == 4 there is 4 unique items in the set
    # Loop through array in chunks of 4 and test
    for i in range(len(data)-4):
        if len(set(data[i:i+4])) == len(data[i:i+4]):
            return i+4
    return None

def task2(data):
    # Same as previously stated, but with 14 instead of 4
    for i in range(len(data)-14):
        if len(set(data[i:i+14])) == len(data[i:i+14]):
            return i+14
    return None

if __name__ == "__main__":
    with open("input/Day6.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))