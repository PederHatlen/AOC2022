def task1(data):
    for i in range(len(data)-4):
        if len(set(data[i:i+4])) == len(data[i:i+4]):
            return i+4
    return None

def task2(data):
    for i in range(len(data)-14):
        if len(set(data[i:i+14])) == len(data[i:i+14]):
            return i+14
    return None

if __name__ == "__main__":
    with open("input/Day6.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))