def encod(text: str):
    for shifr in range(26):
        res = ""
        for i in text:
            if 'a' <= i.lower() <= 'z':
                asci = ((ord(i.lower()) - ord("a")) + 1) % 26
                asci2 = chr(asci + ord("a"))
                res += asci2
            else:
                res += x
    return res

def decod(text: str):
    for shifr in range(26):
        res = ""
        for i in text:
            if 'a' <= i.lower() <= 'z':
                asci = ((ord(i.lower()) - ord("a")) - 1) % 26
                asci2 = chr(asci + ord("a"))
                res += asci2
            else:
                res += x
    return res

print(encod(input()))
print(decod(input()))