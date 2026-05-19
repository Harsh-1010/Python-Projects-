"""Merge two dictionaries"""
# d1 = {1:10, 2:20, 3:30}
# d2 = {4:40, 5:50, 6:60}

#d1.update(d2)
# for i in d2:
#     d1[i] = d2[i]
#print(d1)

"""Sum all the Values in the Dictionaries"""
# d = {1:10,2:20,3:30,4:30,5:10,6:30}
# for i in d :
#     sum += d[i]
# print(sum)

"""Frequency of each element in a list"""
# a = (1,2,3,1,1,4,8,7,2,4,6,6)
# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#         # print(d)
#     else:
#         d[i] = 1
# print(d)

"""Add the same key values"""
d1 = {1:10,2:20,3:30}
d2 = {3:40,4:50,5:60}

for i in d2:
    if i in d1:
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1)

