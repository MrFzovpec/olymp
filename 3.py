# a = int(input())
# b = int(input())
#
# print(a * (b - 1) + 1)

a, b = int(input()), int(input())
n = 1

while not(((n - 1) % a == 0) and ((n + 1) % b == 0)):
    n += 1

print(n)
