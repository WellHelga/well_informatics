def rot13(text: str) -> str:
    res = ""
    for x in text:
        if 'a' <= x.lower() <= 'z':
            asci = ((ord(x.lower()) - ord("a")) + 13) % 26
            asci2 = chr(asci + ord("a"))
            res += asci2
        else:
            res += x
    return res

print(rot13("Hello, World!"))  # "Uryyb, Jbeyq!"
print(rot13("Uryyb, Jbeyq!"))  # "Hello, World!"
print(rot13(rot13("Test")))  # "Test"
print(rot13("123!@#"))  # "123!@#"