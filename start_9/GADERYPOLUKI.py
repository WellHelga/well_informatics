def encode(message, key):
    slov = {}
    key = key.lower()
    for i in range(0, len(key), 2):
        x, y = key[i], key[i + 1]
        slov[x] = y
        slov[y] = x
        slov[x.upper()] = y.upper()
        slov[y.upper()] = x.upper()
    return "".join(slov.get(i, i) for i in message)

def decode(encrypted_message, key):
    return encode(encrypted_message, key)

print(encode("ABCD", "agedyropulik"))            # => GBCE
print(encode("Ala has a cat", "gaderypoluki"))   # => Gug hgs g cgt
print(decode("Dkucr pu yhr ykbir", "politykarenu"))  # => Dance on the table
print(decode("Hmdr nge brres", "regulaminowy"))      # => Hide our beers