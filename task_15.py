m = int(input())
year = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
    days[-1] = 29
print(days[m-1])