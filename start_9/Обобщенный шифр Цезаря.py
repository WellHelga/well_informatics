def caesar_cipher(text: str, shift: int, mode: str) -> str:
    res = ""
    for x in text:
        if 'a' <= x.lower() <= 'z':
            if mode == 'encrypt':
                asci = ((ord(x.lower()) - ord("a")) + shift) % 26
            else:
                asci = ((ord(x.lower()) - ord("a")) - shift) % 26
            asci2 = chr(asci + ord("a"))
            res += asci2
        else:
            res += x
    return res

print(caesar_cipher("Hello", 3, 'encrypt'))  # Должно вернуть: "Khoor"
print(caesar_cipher("Khoor", 3, 'decrypt'))  # Должно вернуть: "Hello"
print(caesar_cipher("XYZ", 5, 'encrypt'))  # Должно вернуть: "CDE" (циклический сдвиг)
print(caesar_cipher("Hello, World!", 13, 'encrypt'))  # Должно вернуть: "Uryyb, Jbeyq!"