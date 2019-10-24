a = int(input())
b = int(input())
ch = 0
nech = 0
n = a
while (n >= a)and(n <= b)and(a <= 100)and(b <= 100):
    if n % 2 == 0:
        ch = ch + n
        n = n + 1
    else:
        nech = nech + n
        n = n + 1


raz = ch - nech

print(raz)
