# (This entire code was written at about 12 pm on the 10th, bordering on the 11th)
# It was suprisingly a lot of fun! It's (for now) my favourite task.

# Messed around with a queing system at first, but it wasn't great
# Ended up just checking twice if there was an add-instruction
def task1(data):
	xreg, cycle = 1, 1
	res = []

	# If the cycle+20 (will always be %40-able for the given values)
	# Then check first for current clock, and then increment clock by 1
	# Then do same outside for new value (Will also run for noop)
	# and the two last: add inst value to xreg and increment clock by 1
	for line in data.split("\n"):
		inst = line.split(" ")
		if inst[0] == "addx":
			if (cycle+20)%40 == 0: res.append(xreg)
			cycle += 1
		if (cycle+20)%40 == 0: res.append(xreg)
		if inst[0] == "addx": xreg += int(inst[1])
		cycle += 1

	# This is just a quick and dirty way of doing it
	# It works, so i'm not touching it
	out = 0
	for i in range(len(res)): out += res[i]*(20+(40*i))
	return out

# Instead of adding values to the result array, i now draw a pixel every cycle
# Functionalized this, so it wouldn't be repeated unnecessarily
def cycleDraw(cycle, xreg):
	sp = (cycle-1)%40
	print("#" if abs(xreg-sp) <= 1 else ".", end="")
	if cycle%40 == 0: print("\n", end="")
	return # Always remember to return your functions

def task2(data):
	xreg, cycle = 1, 1

	# Task 2 is just a slightly modified task 1
	for line in data.split("\n"):
		inst = line.split(" ")
		if inst[0] == "addx":
			cycleDraw(cycle, xreg)
			cycle += 1  
		cycleDraw(cycle, xreg)
		if inst[0] == "addx": xreg += int(inst[1])
		cycle += 1
	return

if __name__ == "__main__":
    with open("input/Day10.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))