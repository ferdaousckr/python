
x = 12
y = 16

while x != y:
    print("Loop ended. x:", x)
    print("Loop ended. y:", y)
    if x < y:
        x += 1
    else:
        y += 1

print("Loop ended. x:", x)
print("Loop ended. y:", y)

for i in range(1,11):
    for j in range (1,10):
        print ("*"*j)
print("*"*i)

