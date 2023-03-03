from math import comb

total_civ = 10
no_sara_civ = total_civ - 1

c = comb(no_sara_civ, 3) / comb(total_civ, 4)
print(c)
a = comb(no_sara_civ, 7) / comb(total_civ, 8) / 2
print(a)
b = 1 - (1 - a) ** 20
print(b)
