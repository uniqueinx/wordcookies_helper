from itertools import permutations


def gen(s):
    out = []
    for i in xrange(2,len(s)+1):
        x = [''.join(p) for p in permutations(s, i)]
        out.extend(x)
    return out


with open('wordsEn.txt', 'r') as l:
    ll = l.readlines()
words = []
for i in ll:
    words.append(i.strip())

while(True):
    s = raw_input("enter charcters: ").strip()
    sol = []
    out = gen(s)
    for i in out:
        if i in words and not i in sol:
            sol.append(i)
    sol.sort(key=lambda x : len(x))
    print '\n'.join(sol)
    print 'Total words found %d' %len(sol)
