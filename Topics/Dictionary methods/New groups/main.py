# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
num_groups = int(input())
attr_groups ={key:None for key in groups}
for number in range(0, num_groups):
    num_chil = int(input())
    attr_groups[groups[number]] = num_chil
print(attr_groups)