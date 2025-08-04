n =int(input("enter a number : "))
letter = ["A", "B" , "C" , "D" , "E"]
for i in range(n):
    for j in range(i + 1):
        print(letter[j],end="")
    print()