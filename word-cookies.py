from itertools import permutations


def generate_permutations(s):
    for i in range(2, len(s) + 1):
        for p in permutations(s, i):
            yield ''.join(p)


words = set()
with open('wordsEn.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        words.add(i.strip())

while True:
    s = input("Enter characters: ").strip()
    sol = set()
    for i in generate_permutations(s):
        if i in words:
            sol.add(i)
    sol = sorted(list(sol), key=lambda x: len(x))
    print('\n'.join(sol))
    print(f'Total words found {len(sol)}')
