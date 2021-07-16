print("    /\\")
print("   /  \\")
print("  /    \\")
print(" /      \\")
print("/________\\")
print("Triangle")
print()
print("|\\")
for i in range(1,10):
    print("|", end="")
    for j in range(0,i):
        print(" ", end="")
    print("\\")
print("|", end="")
for i in range(0,10):
    print("_", end="")
print("\\")


i=input("What do you wanna print: ")
j=input("How many times should we print it? ")
i=i+" "
x=int(j)
print()
print(i*x)

y="Hi!, "
print(y+i)