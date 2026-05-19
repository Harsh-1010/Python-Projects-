from pathlib import Path

def readfileandfolder():
 path = Path('')
 items = list(path.rglob('*'))
 for i, items in enumerate(items):
  print(f"{i +1} : {items}")

def createfile():
 readfileandfolder()
 name = input("Enter the name of the file: ")
 p = Path(name)
 with open(p,'w') as fs:
  data = input("What you want to write in the file: ")
  fs.write(data)

print("Enter 1 to create the file")
print("Enter 2 to read the file")
print("Enter 3 to update the file")
print("Enter 4 to delete the file")

check = int(input("Enter your response: "))
if check == 1:
 createfile()