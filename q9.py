def calc_sum(n):
    if n == 1:
        return 1
    return n + calc_sum(n-1)

print(calc_sum(5))