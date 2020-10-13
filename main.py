# Replace all ______ with rjust, ljust or center.

thickness = int(input())  # This must be an odd number
c = 'H'
x = 1
f = thickness
u = 1
# Top Cone
for i in range(thickness):
    print((c * x).rjust(f, ' '))
    if x < thickness:
        u += 1
    x += 2
    f += 1

# Top Pillars
for i in range(thickness + 1):
    print(' ' *(thickness - u), end="")
    print(c * thickness, end="")
    print((' ' * (thickness * 3)), end="")
    print(c * thickness)

# Middle Belt
for i in range((thickness + 1) // 2):
    print(' ' *(thickness - u), end="")
    print(c * thickness, end="")
    print((c * (thickness * 3)), end="")
    print(c * thickness)

# Bottom Pillars
for i in range(thickness + 1):
    print(' ' *(thickness - u), end="")
    print(c * thickness, end="")
    print((' ' * (thickness * 3)), end="")
    print(c * thickness)

# Bottom Cone
z = thickness * 5 + (thickness - 1)
for i in range(thickness):
    x -= 2
    print((c * x).rjust(z, ' '))
    z -= 1
