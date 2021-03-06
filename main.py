from collections import deque

number_of_cases = int(input())
flag = True

for _ in range(number_of_cases):
    number_of_cubes = int(input())
    cubes = deque(map(int, input().split()))
    while len(cubes) >= 3:
        if cubes[0] >= cubes[-1]:
            first = cubes.popleft()
            if first < cubes[0]:
                print('No')
                flag = False
                break
        else:
            first = cubes.pop()
            if first < cubes[-1]:
                print('No')
                flag = False
                break

    if flag:
        print('Yes')

