def transform_strings(strings):
    if not strings:
        return ""
    l = len(strings)
    n = len(strings[0])
    res = []
    for i in range(n):
        schet = 0
        for j in strings:
            x = j[i]
            if x == " ":
                schet += 0
            else:
                schet += (ord(x) - ord("a") + 1)
        y = schet // l
        if y == 0:
            res.append(" ")
        else:
            res.append(chr(ord("a") + y - 1))
    return "".join(res)

s1 = "u lk zxuq hfk as fouh"
s2 = "y l  zpuv  xe at sicd"
s3 = "welvayfuqbfpeaauaqcrc"

strings = [s1, s2, s3]
result = transform_strings(strings)
print(result)