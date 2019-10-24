# a = int(input())
# b = int(input())
#
# ch = 0
# nch = 0
#
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         ch += i
#     else:
#         nch += i
#
# print(ch - nch)


a = int(input("Введите А = "))
b = int(input("Введите B = "))
ch = 0
nech = 0
n=a
while (n>=a)and(n<=b)and(a<=100)and(b<=100):
    if n%2 == 0:
        ch = ch + n
        n=n+1
    else:
        nech = nech + n
        n=n+1
else:
    print("Введите другие числа")

print("Сумма четных = " + str(ch))
print("Сумма нечетных = " + str(nech))
raz=ch-nech

print(raz)
