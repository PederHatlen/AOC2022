import re

### NOTICE This is a horrible, terrible, no-good solution. Please do not replicate ###

# Determining if collision by checking if edges are inside another
def task1(data):
    l = data.split("\n")
    sum = 0
    # Could have been done cleaner, but it was the fastest way i saw
    for line in l:
        n = list(map(int, re.split(',|-',line)))
        if (n[0]<=n[2] and n[1]>=n[3]) or (n[0]>=n[2] and n[1]<=n[3]):
            sum+=1
    return sum

# This is were the old method shows it's true colors
# It is done the same way as the first one, but it also needs overlappings
# The solution is too check for all possible overlappings
def task2(data):
    l = data.split("\n")
    sum = 0
    for line in l:
        n = list(map(int, re.split(',|-',line)))
        if (n[0]<=n[2] and n[1]>=n[2]) or (n[0]<=n[3] and n[1]>=n[3]) or (n[2]<=n[0] and n[3]>=n[0]) or (n[2]<=n[1] and n[3]>=n[1]):
            sum+=1
    return sum

if __name__ == "__main__":
    with open("input/Day4.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))