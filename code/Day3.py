values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def task1(data):
    r = data.split("\n")
    sum = 0
    for i in r:
        c = list(set(i[:len(i)//2])&set(i[len(i)//2:]))[0]
        sum += values.index(c)+1
    return sum

def task2(data):
    r = data.split("\n")
    sum = 0
    for i in range(2, len(r), 3):
        c = list(set(r[i-2])&set(r[i-1])&set(r[i]))[0]
        sum += values.index(c)+1
    return sum

if __name__ == "__main__":
    with open("Day3.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))