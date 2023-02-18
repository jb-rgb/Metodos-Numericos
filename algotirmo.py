N = int(input("Introzuca un numero: "))
SUM = 0
SUM2 = 0
i = 1

while(i <= N):
    SUM = SUM + i
    i  = i + 1

for j in range(N + 1):
    SUM2 = SUM2 + j
    j = j + 1

print (SUM)
print (SUM2)