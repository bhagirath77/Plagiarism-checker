def removeIrrelevantChars(s):
    x = ""
    for i in s:
        if ord(i) > 32 and ord(i) < 127 and ord(i):
            x += i
    x = x.lower()
    return x


def restart(s, d, j):
    x = 0
    for i in range(d):
        x += ((109 ** (d - 1 - i)) * code[s[i+j]])
        x = x % 100009
    return x


def hashValues(s, d):
    x = 0
    for i in range(d):
        x += ((109 ** (d - 1 - i)) * code[s[i]])
        x = x % 100009
    lis = []
    lis.append(x)
    i = 1
    while (i < len(s) - d + 1):
        if (s[i+d-1] == "." or s[i+d-1] == "?") and i < len(s)-2*d+1:
            x = restart(s, d, i+d)
            i += d
        else:
            x = ((x - (109 ** (d - 1)) *
                  code[s[i - 1]]) * 109 + code[s[i + d - 1]])
            x = x % 100009
        lis.append(x)
        i += 1
    return lis


def winnowing(lst, d):
    y = len(lst)
    x = 100009
    winList = []
    for i in range(y - d + 1):
        if x != min(lst[i:i + d]):
            winList.append([min(lst[i:i + d]), i])
            x = min(lst[i:i + d])
    return winList


def printPer(lis1, lis2):
    match = {}
    i = 0
    while (i < len(lis1)):
        match[lis1[i][0]] = match.get(lis1[i][0], 0) + 1
        i += 1
    i = 0
    count = 0
    while (i < len(lis2)):
        if lis2[i][0] in match:
            count += 1
            match[lis2[i][0]] -= 1
            if match[lis2[i][0]] == 0:
                del match[lis2[i][0]]
        i += 1
    print(len(lis1))
    similarity = (2 * count) / (len(lis1) + len(lis2)) * 100
    print(similarity)


def printPer500(lis1, lis2):
    match = {}
    i = 0
    while (i < len(lis1)):
        match[lis1[i]] = match.get(lis1[i], 0) + 1
        i += 1
    i = 0
    count = 0
    while (i < len(lis2)):
        if lis2[i] in match:
            count += 1
            match[lis2[i]] -= 1
            if match[lis2[i]] == 0:
                del match[lis2[i]]
        i += 1
    print(len(lis1))
    similarity = (2 * count) / (len(lis1) + len(lis2)) * 100
    print(similarity)


code = {"!": 1, "#": 2, "$": 3, "%": 4, "&": 5, "(": 6, ")": 7, "*": 8, "+": 9, ",": 10,
        "-": 11, ".": 12, "/": 13, ":": 14, ";": 15, "<": 16, "=": 17, ">": 18, "?": 19,
        "@": 20, "[": 21, "^": 22, "_": 23, "`": 24, "{": 25, "|": 26, "}": 27, "~": 28,
        "]": 29, "\"": 30, "\'": 31, "a": 32, "b": 33, "c": 34, "d": 35, "e": 36, "f": 37,
        "g": 38, "h": 39, "i": 40, "j": 41,
        "k": 42, "l": 43, "m": 44, "n": 45, "o": 46, "p": 47, "q": 48, "r": 49, "s": 50,
        "t": 51, "u": 52, "v": 53, "w": 54, "x": 55, "y": 56, "z": 57, "0": 58, "1": 59,
        "2": 60, "3": 61, "4": 62, "5": 63, "6": 64, "7": 65, "8": 66, "9": 67, "\\": 68}

f = open("ex.txt", encoding="utf8")
ff = open("./ex1.txt", encoding="utf8")


s = f.read()
ss = ff.read()

s = removeIrrelevantChars(s)
ss = removeIrrelevantChars(ss)
print(len(s))
print(len(ss))
x = len(s)
y = len(s)
if min(x, y) <= 2000:
    d = 4
else:
    d = 9
hashList = hashValues(s, d)
hashList1 = hashValues(ss, d)
z = min(x, y)
if z > 500:
    if z > 2000:
        d = 6
    else:
        d = 3
    fingerprint1 = winnowing(hashList, d)
    fingerprint2 = winnowing(hashList1, d)
    printPer(fingerprint1, fingerprint2)
else:
    printPer500(hashList, hashList1)
