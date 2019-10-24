a = int(input())
b = int(input())

chet = 0
nechet = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        chet += i
    else:
        nechet += i
        
print(chet - nechet)
