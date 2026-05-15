"""Print negative and positive no."""
# l = [1,-1,2,3,-10,4,7,-12,-14]
# b = []
# c = []
# for i in l:
#     if i >= 0:
#         b.append(i)
#     else:
#         c.append(i)
# print(f"positive no: {b}, negative no: {c}")
# print(f"Total positive no: {len(b)}, Total negative no: {len(c)}")

"""Mean of a List"""
# M = [1,2,3,4,5,6,7,80,9]
# a = 0
# for i in range(0, len(M)):
#     a += M[i]
# print(f"Mean = {a/len(M)}")

"""Find the Greatest elemant in a List"""
# g = [78,2,90,455,2454,3]
# a = 0
# for i in range(len(g)):
#     if a < g[i]:
#         a = g[i]
# print("The Greatest Element in a is: ",a)
# print("The Index is: ", g.index(a) + 1)

"""Find the second greatest element in a list"""
# g = [11,111,9,119,89,121,120]
# a = 0
# b = 0
# for i in range(len(g)):
#     if a < g[i]:
#         b = a
#         a = g[i]
#     elif b < g[i] and g[i] != a:
#         b = g[i] 
# print("Greatest: ",a, "Second Greatest: ", b)

"""Find if the list is sorted or not"""
# g = [1,2,8,3,4,5,6]
# for i in range(len(g) - 1):
#     if g[i] > g[i + 1]:
#         print("The list is not sorted")
#         break
# else:
#         print("The list is Sorted")