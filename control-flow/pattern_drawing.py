size = int(input("Enter the size of the pattern: "))

row = 0


    while row < size:
        for _ in range(n):
            print("*", end="")
            print() # print a newline after each row
            row+= 1
