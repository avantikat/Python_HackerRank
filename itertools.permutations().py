from itertools import permutations

word, num = input().split(" ")
permutations = list(permutations(word, int(num)))
permutations.sort()

[print("".join(i)) for i in permutations]
