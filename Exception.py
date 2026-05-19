a = int(input("Enter the no: "))
try:
    print(10/0)
except ZeroDivisionError:
    print("Dividing by zero is not acceptable")

print("Division is complete")

try:
    print(10/a)
except Exception as err:
    print(f"Sorry their is an error as {err}")
print("Olla")

