input_numbers = input()
list_numbers = []
for i in range(1, int(input_numbers)+1):
    enter_number = input()
    list_numbers.append(int(enter_number))

result = sum(list_numbers) / int(input_numbers)
print(result)