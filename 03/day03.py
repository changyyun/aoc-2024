import re

def get_data():

    with open('in.txt', 'r') as f:
        return f.read().strip()

def solve_1():
    data = get_data()
    matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data) 
    result = 0 

    for s in matches:
        op = s[4:len(s)-1]
        a, b = tuple(map(int, op.split(',')))
        result += a * b

    print(result)

def solve_2():
    data = get_data()
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)
    flag = True
    result = 0

    for s in matches:
        if s == 'do()':
            flag = True
        elif s == "don't()":
            flag = False
        elif flag:
            op = s[4:len(s)-1]
            a, b = tuple(map(int, op.split(',')))
            result += a * b
    
    print(result)

if __name__ == '__main__':
    solve_1()
    solve_2()
