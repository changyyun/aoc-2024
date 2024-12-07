
def read_input():

    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
        left = []
        right = []
        for (x, y) in map(lambda x : x.split(), lines):
            left.append(int(x))
            right.append(int(y))

        return left, right

def solve_1():
    left, right = read_input()
    left.sort()
    right.sort()
    diff_sum = 0
    for l, r in zip(left, right):
        diff_sum += abs(l - r)

    print(diff_sum)

def solve_2():
    from collections import Counter

    left, right = read_input()
    counts = Counter(right)
    total = 0
    for l in left:
        total += l * counts[l]

    print(total)

    

def main():
    solve_1()
    solve_2()

if __name__ == '__main__':
    main()
