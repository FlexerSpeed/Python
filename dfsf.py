x = list(range(10, 101, 10))
print(x)

# enumarat
index_count = 0

for letter in 'abcde':
    print(f'In {index_count} the letters is {letter}')
    index_count += 1

for i, letter in enumerate('abcde', start=2):
    print(f'In {i} the letters is {letter}')

l = list(enumerate('abcde'))
print(l)
