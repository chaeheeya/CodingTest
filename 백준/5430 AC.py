from collections import deque

T = int(input())

for __ in range(T):
    p = input().strip()
    n = int(input().strip())
    arr_str = input().strip()

    if n ==0:
        arr = []
    else:
        arr = arr_str[1:-1].split(',')
        arr = deque(map(int, arr))

    reverse = False
    error = False

    for f in p:
        if f == 'R':
            if not reverse:
                reverse = True
            else:
                reverse = False
        elif f == 'D':
            if not arr:
                error = True
                print('error')
                break
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    # print(reverse, arr)
    if not error:
        if reverse:
            arr.reverse()

        print('['+','.join(map(str, arr))+']')