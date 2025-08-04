n =int(input("enter a number : "))
letter = ["A", "B" , "C" , "D" , "E"]
for i in range(n,0,-1):
    for j in range(i):
        print(letter[j],end="")
    print()
