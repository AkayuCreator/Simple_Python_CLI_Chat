a = int(input())
b = a % 4
c = a % 100
d = a % 400
if b == 0 and c != 0 or d == 0:
    print("Leap")
else:
    print("Ordinary")
