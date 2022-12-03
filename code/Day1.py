def task1(data):
    cal = []
    for e in data.split("\n\n"):
        cal.append(sum(map(int, e.split("\n"))))
    return sorted(cal)[-1]

def task2(data):
    cal = []
    for e in data.split("\n\n"):
        cal.append(sum(map(int, e.split("\n"))))
    return sum(sorted(cal)[-3:])

if __name__ == "__main__":
    with open("Day1.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))