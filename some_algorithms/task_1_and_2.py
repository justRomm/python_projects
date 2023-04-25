import time


def first_task():
    n = int(input("N = "))
    start_time = time.time()
    res = int((n * (n + 1)) / 2)
    end_time = time.time()
    print(f'Execution time is equal to {end_time - start_time} seconds\n'
          f'Result is equal to {res}\n\n')


def input_sea():
    try:
        m = int(input("M = "))
    except:
        raise ValueError("Only integers")
    try:
        n = int(input("N = "))
    except:
        raise ValueError("Only integers")
    sea = []
    for i in range(m):
        row = input().split(' ')
        for j in row:
            if j not in ['0', '1']:
                raise ValueError("Only 0 or 1 separated by spaces (' ')")
        if len(row) != n:
            raise ValueError("You have entered a wrong data")
        sea.append([int(i) for i in row])
    return m, n, sea


def detect_island(m=int, n=int, x=int, y=int, sea=list):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    sea[y][x] = 0
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < n and 0 <= y1 < m and sea[y1][x1] == 1:
            detect_island(m, n, x1, y1, sea)


def second_task():
    m, n, sea = input_sea()
    count = 0
    for j in range(n):
        for i in range(m):
            if sea[i][j] == 1:
                detect_island(m, n, j, i, sea)
                count += 1
    print(f'\nNumber of islands = {count}\n\n')


def main():
    print("Task 1 and 2 from test tasks for Quantum Data Science Intern\n"
          "Made by Romaniuk Mykhailo\n")
    choice = 3
    while choice != 0:
        choice = int(input("Enter 1, if you want to see task 1;\n"
                           "Enter 2, if you want to see task 2;\n"
                           "Enter 0, if you want to close program;\n"
                           "Input: "))
        print()
        if choice == 1:
            first_task()
        elif choice == 2:
            second_task()
        else:
            print("Have a good day!")


if __name__ == '__main__':
    main()
