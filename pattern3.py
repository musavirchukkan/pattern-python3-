n=input("Enter the first input: ")
m=input("Enter the second input: ")
for i in range(0,int(n)):
    for j in range(0,int(m)):
        print(end=" "*(int(n)-i))
        print(end="* "*i)
        print(end=" "*(int(n)-i))
    print("\n")
for i in range(int(n),0,-1):
    for j in range(0,int(m)):
        print(end=" "*(int(n)-i))
        print(end="* "*i)
        print(end=" "*(int(n)-i))
    print("\n")
