#  You can experiment here, it won’t be checked
numbers = {"first": 1, "second": 2, "third": 3, "fourth": 4}
print(numbers.get(4))
print(numbers.get("fourth"))
print(numbers.get(4, "4"))

pop_value = numbers.pop('fourth')
print(pop_value)