# Using class to parse a lot of monkeys (never thought i would ever write that, but here we are)
class monkey:
    def __init__(self, lines, task):
        self.name = lines[0][:-1]
        self.task = task
        self.inspections = 0

        # Splitting the items into an array
        self.items = list(map(int, lines[1].split(":")[1].strip().split(", ")))
        
        # Factors for increasing anxiousness
        factor = lines[2].split(" ")[-1]
        self.factorIsOld = (factor == "old")
        if not self.factorIsOld: 
            self.factor = int(lines[2].split(" ")[-1])
        
        # If the operator is + toggle the + mode (used inside monkeyRound function)
        self.operationMode = "+" in lines[2]
        
        # Values for test part of the procedure
        self.testVal = int(lines[3].split(" ")[-1])
        self.ifTestTrue = " ".join(["Monkey", lines[4].split(" ")[-1]])
        self.ifTestFalse = " ".join(["Monkey", lines[5].split(" ")[-1]])

    def monkeyRound(self, item, mod = 1):
        self.inspections += 1
        
        # Adding/multiplying the worry level
        if self.operationMode: item = item+(item if self.factorIsOld else self.factor)
        else: item = item*(item if self.factorIsOld else self.factor)
        
        # Specific action per task, task 2 action can be done in task 1 aswell
        # But i chose to keep it the way it was
        if self.task == 1: item = item//3
        else: item = (item%mod)

        # If the rest division (modulo) of item and target value == 0
        # Throw to monkey x, else throw to monkey y
        if item%self.testVal == 0: return self.ifTestTrue, item
        else: return self.ifTestFalse, item
    
def task1(data):
    monkeys = {}
    # Making the monkey classes and appending to the dictionary
    for part in data.split("\n\n"):
        lines = part.split("\n")
        monkeys[lines[0][:-1]] = monkey(lines, 1)

    # Every round the monkeyRound function is called for every item in a monkey's "inventory"
    # after this 
    for round in range(20):
        for m in monkeys:
            cm = monkeys[m] # Current monkey
            for item in cm.items:
                rm, nItem = cm.monkeyRound(item) # Receiving monkey, new item
                monkeys[rm].items.append(nItem)
            # Cleqaring the inventory, since the items have moved
            cm.items = []
    # Retrieve every inspection count and sort, multiply two last items (2 largest) together
    totalInsp = list(sorted(map(lambda m: monkeys[m].inspections, monkeys)))
    return totalInsp[-1]*totalInsp[-2]

# This is the same as task 1, but with modulo calculations
# Modulo is every test value multiplied (gets the common factor)
def task2(data):
    monkeys = {}
    mod = 1
    for part in data.split("\n\n"):
        lines = part.split("\n")
        monkeys[lines[0][:-1]] = monkey(lines, 2)
        mod *= monkeys[lines[0][:-1]].testVal

    for round in range(10000):
        for m in monkeys:
            cm = monkeys[m] # Current monkey
            for item in cm.items:
                rm, nItem = cm.monkeyRound(item, mod) # Receiving monkey, new item
                monkeys[rm].items.append(nItem)
            cm.items = []
    totalInsp = list(sorted(map(lambda m: monkeys[m].inspections, monkeys)))
    return totalInsp[-1]*totalInsp[-2]

if __name__ == "__main__":
    with open("input/Day11.txt", "r") as fi:
        data = fi.read()
        # print(task1(data))
        print(task2(data))