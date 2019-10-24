s = input()

index = None


def pal_check(s):
    l = len(s)
    for i in range(l // 2):
        if s[i] != s[-1 - i]:
            return False
    return True


if pal_check(s):
    print(0)
    quit()
else:
    for i in range(len(s)):
        n = s.replace(s[i], '')
        if pal_check(n):
            index = i
            break

    if index != None:
        print(index + 1)
    else:
        print(0)
