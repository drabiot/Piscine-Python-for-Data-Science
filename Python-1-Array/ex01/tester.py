from array2D import slice_me


family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]

notfamily: int = 2

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
print(slice_me(notfamily, 0, 2))
print(slice_me(family, "hello", 2))
print(slice_me(family, 1, "hello"))

family2 = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88]]

print(slice_me(family2, 0, 2))
