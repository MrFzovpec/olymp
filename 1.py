hours_t = int(input())
utc = int(input())
hours_p = int(input())

print((hours_t - utc + hours_p) % 24)
