'''
Python Workshop #2
Name isn't here cuz I'm putting this on my github :3
Anyways enjoy this nonsense code I guess
'''
from typing import final
def part1_function(mass = float, velocity = float):
    momentum = mass * velocity
    if momentum >= 1000:
        return ("Super kick! The target is going flying!")
    if momentum >= 500:
        return ("Decent hit! The target is knocked back.")
    else:
        return ("Hmm, needs more power!")

def part2_function(outside_temp = float):
    inside_temp = 0
    if outside_temp < 15:
        inside_temp = 22
    if outside_temp > 25:
        inside_temp = 20
    else:
        inside_temp = 21
    return inside_temp

def part3_function(sum_purchase = float):
    if sum_purchase >= 100:
        sum_purchase = sum_purchase / 1.1
    if sum_purchase >= 200:
        sum_purchase = sum_purchase / 1.2
    else:
        return sum_purchase
    return sum_purchase

def part4_function(grade = int):
    match grade:
        case p if grade >= 90:
            return "A"
        case p if grade >= 80:
            return "B"
        case p if grade >= 70:
            return "C"
        case p if grade >= 60:
            return "D"
        case p if grade < 60:
            return "F"

r = input("Enter mass then velocity: ")
r = r.split(', ')
for x in range(len(r)): r[x] = int(r[x])
print(part1_function(r[0], r[1]))

r = float(input("Enter outside temp: "))
print(part2_function(r))

r = float(input("Enter total cost of items purchased: "))
print(part3_function(r))

r = float(input("Enter grade: "))
print(part4_function(r))