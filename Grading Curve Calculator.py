n = input("Please enter exam scores")
z = n.split(",")

for i in range(0,len(z)):
    z[i] = int(z[i])

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

y = 0

for i in z:
    y += ((i - mean(z)) ** 2)

import math

stddev = math.sqrt(y / len(z))

grade = []

for i in z:
    if (i >= mean(z) - (.5 * stddev)) and (i <= mean(z) + (.5 * stddev)):
        grade.append("C")
    elif i < mean(z) - (1.5 * stddev):
        grade.append("F")
    elif i < mean(z) - (.5 * stddev):
        grade.append("D")
    elif i > mean(z) + (1.5 * stddev):
        grade.append("A")
    elif i > mean(z) + (.5 * stddev):
        grade.append("B")

print("Mean:" , "{0:.2f}".format(mean(z)) , "Standard Deviation:" , "{0:.2f}".format(stddev))
print("Grades:" , ",".join(grade))
