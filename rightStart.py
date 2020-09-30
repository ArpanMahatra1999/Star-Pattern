#FOR ABSOLUTE BEGINNERS 
rows = int(input("ENTER THE NUMBERS OF ROWS YOU WANT : "))
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')

    print("\r")

    
    
#FOR MODERATE LEARNERS
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end=" ")
        print("\r")
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ", end=" ")
        print("\r")

pattern(5)
