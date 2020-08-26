from itertools import combinations
from itertools import permutations

numbers = "011"
answer = 0

comb = []
perm = []

for i in range(len(numbers)):
    for c in combinations(numbers,i+1):
        comb.append(''.join(c))

for each in comb:
    for p in permutations(each):
        perm.append(''.join(p))

perm = list(set(perm))

# print(perm)

for num in perm:
    if int(num) > 1:
        for i in range(2,int(num)):
            if (int(num) % i) == 0:
                pass
            if i == int(num) - 1:
                print(num)
                answer += 1

print(answer)