x = int(input('ENTER THE SIZE OF THE PYRAMID : '))

def pattern(n):
    k = 2*n - 2
    for i in range(n,-1,-1): #for rows
        for j in range(k,0,-1): #for columns
            print(end=" ")
        k = k + 1
        for j in range(0,i+1):
            print("* ",end=" ")
        print(("\r"))

pattern(x)
