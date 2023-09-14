ln = list(map(int, input().split()))
cn = 0

for i in ln:
    if (i % 2) != 0:
        cn += i

print(cn)

          
