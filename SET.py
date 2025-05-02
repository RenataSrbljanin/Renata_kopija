a={1,2,3}
b={2,3,4}
print(a)
print(b)

print(a|b)
print(a&b)
print(a-b)
print(b-a)
print(a^b)


print()
c={2, 4, 6, 54, 56, 2, 4}
print(c)
d=a|b
print(d)
print(f"presek je: {c&d}")

print()
c.add(8)

print(c)

if 8 in c:
    print("true")
