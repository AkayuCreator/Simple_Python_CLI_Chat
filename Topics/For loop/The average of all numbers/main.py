# put your python code here
a = int(input())
b = int(input())
numbers_3 = []
counter = 0
for number in range(a, b+1):
    if number % 3 == 0:
        numbers_3.append(number)
        counter += 1
result = sum(numbers_3)
print(result/counter)

