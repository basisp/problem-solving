from collections import deque

for _ in range(10):
    order = int(input())

    arr = deque(list(map(int, input().split())))
    offset = 0

    while True:
        num = arr.popleft()
        offset +=1
        if offset == 6:
            offset = 1

        if num - offset <= 0:
            num = 0
            arr.append(num)
            break

        else:
            arr.append(num-offset)



    print(f"#{order} " + ' '.join(map(str,arr)))