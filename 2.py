a = int(input())
b = int(input())

ch = 0
nch = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        ch += i
    else:
        nch += i

print(ch - nch)
