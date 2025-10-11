def dirReduc(x):
    cardinal_directions = {
        "SOUTH": "NORTH", "NORTH": "SOUTH", "WEST": "EAST", "EAST": "WEST"
    }
    s = []
    for i in x:
        if s and s[-1] == cardinal_directions.get(i):
            s.pop()
        else:
            s.append(i)
    return s
y = input().split()
res = dirReduc(y)
print(res)
