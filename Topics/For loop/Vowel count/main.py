string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
n = 0
for a in string:
    for b in vowels:
        if a == b:
            n += 1
print(n)