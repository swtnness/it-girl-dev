#Uso del break continue

for i in range(1, 10):
    if i == 4 and i <=8:
       continue
    print(f"{i}", end= "-")

print(" ")
for i in range(1, 11):
    if i == 5:
        break
    print(f"{i}", end=" ")