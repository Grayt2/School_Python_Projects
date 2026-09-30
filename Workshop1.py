'''
Python Workshop #1
Name isn't here cuz I'm putting this on my github :3
Anyways enjoy this nonsense code I guess
'''

def rectangle(width = float, hight = float):
    return width * hight
print("P1")
r = input("Enter width then hight: ")
r = r.split(', ')
for x in range(len(r)): r[x] = int(r[x])
print(rectangle(r[0], r[1]))

calc = input("Enter the two numbers you wanna do math on: ")
calc = calc.split(", ")
print(f"Added = {int(calc[0]) + int(calc[1])}, Subtracted = {int(calc[0]) - int(calc[1])}, divided = {int(calc[0]) / int(calc[1])}, multiplied = {int(calc[0]) * int(calc[1])}")
print("P2")
def circle(radius = float):
    import math
    return math.pi * radius ** 2
rad = float(input("Enter radius: "))
print(circle(rad))
print("P3")
i = input("Enter sales: ")
i = i.split(', ')
for x in range(len(i)): i[x] = int(i[x])
print(round(sum(i)/len(i), 2))