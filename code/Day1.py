# Splitting the calories into the groups, and summing
# Return the largest by sorting and taking the last element
def task1(data):
    cal = []
    for e in data.split("\n\n"):
        cal.append(sum(map(int, e.split("\n"))))
    return sorted(cal)[-1]

# Same as task 1, but suming the last 3 at the end
def task2(data):
    cal = []
    for e in data.split("\n\n"):
        cal.append(sum(map(int, e.split("\n"))))
    return sum(sorted(cal)[-3:])

if __name__ == "__main__":
    with open("input/Day1.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))