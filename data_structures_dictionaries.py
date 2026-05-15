"""Merge two dictionaries"""

d1 = {1:10, 2:20, 3:30}
d2 = {4:40, 5:50, 6:60}

for i in d2:
    d1[i] = d2[i]
print(d1)
    
