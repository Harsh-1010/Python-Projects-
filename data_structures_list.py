l = [1,-1,2,3,-10,4,7,-12,-14]
b = []
c = []
for i in range(0, len(l)):
    if l[i] >= 0:
        b.append(l[i])
    else:
        c.append(l[i])
print(f"positive no: {b}, negative no: {c}")
print(f"Total positive no: {len(b)}, Total negative no: {len(c)}")