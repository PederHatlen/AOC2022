def task1(data):
    matrix = list(map(lambda x: list(map(int, list(x))), data.split("\n")))
    
    visible = 0
    for x in range(1, len(matrix)-1):
        for y in range(1, len(matrix[0])-1):
            # Checking if the maximum value in the array from subject to the edge is higher than subject
            # if any direction is open (any statement is true), the tree is visible.
            if matrix[x][y] > max(matrix[x][:y]):
                visible += 1
            elif matrix[x][y] > max(matrix[x][y+1:]):
                visible += 1
            elif matrix[x][y] > max(list(map(lambda e: e[y], matrix[:x]))):
                visible += 1
            elif matrix[x][y] > max(list(map(lambda e: e[y], matrix[x+1:]))):
                visible += 1
    visible += 2*len(matrix) + (len(matrix[0])-2)*2
    return visible

    # The error zone:
        # 7158, too high
        # 3178, too high
        # 1550, too low
        # 1688, Just right

def task2(data):
    matrix = list(map(lambda x: list(map(int, list(x))), data.split("\n")))
    
    results = []
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            left, right, top, bottom = [], [], [], []
            
            # For every element in an array with subject as startpoint
                # Add to element array (Mostly for debuging, but it's practical)
                # Check if higher than subject, if true: blockage found, stop loop
            for k in reversed(matrix[i][:j]):
                left.append(k)
                if matrix[i][j] <= k: break
            for k in matrix[i][j+1:]:
                right.append(k)
                if matrix[i][j] <= k: break
            for k in reversed(list(map(lambda x: x[j], matrix[:i]))):
                top.append(k)
                if matrix[i][j] <= k: break
            for k in list(map(lambda x: x[j], matrix[i+1:])):
                bottom.append(k)
                if matrix[i][j] <= k: break
            
            results.append(len(left)*len(right)*len(top)*len(bottom))
    return max(results)

if __name__ == "__main__":
    with open("input/Day8.txt", "r") as fi:
        data = fi.read()
        print(task1(data))
        print(task2(data))