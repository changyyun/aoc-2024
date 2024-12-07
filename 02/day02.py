

def read_input():
    with open('in.txt', 'r') as f:
        return map(lambda x : list(map(int, x.strip().split())), f.readlines())

def is_safe(line):
    is_increasing = line[0] - line[1] < 0 
    
    for i in range(1, len(line)):
        diff = line[i-1] - line[i]
        if abs(diff) > 3 or diff == 0 or (diff < 0 and not is_increasing) or (diff > 0 and is_increasing):
            return False

    return True

def solve_1():
    data = read_input()
    total = 0
    for row in data:
        total += is_safe(row)

    print(total)

def solve_2():
    data =  read_input()
    total = 0
    for row in data:
        if is_safe(row):
            total += 1
        else:
            size = len(row)
            for i in range(size):
                if is_safe(row[0:i] + row[i+1:size]):
                    total += 1
                    continue 
    print(total)


if __name__ == '__main__':
    solve_1()
    solve_2()

