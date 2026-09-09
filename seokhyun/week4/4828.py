# SEWA 4828 min max

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_arr = list(map(int, input().split()))
    min_val = 1000001
    max_val = 0

    for num in num_arr:
        if min_val > num:
            min_val = num

        if max_val < num:
            max_val = num

    print(f"#{test_case} {max_val - min_val}")
