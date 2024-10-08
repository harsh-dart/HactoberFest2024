def printTriangle(arr, n):
    
    # Initialize a 2D array to store triangle
    tri = [[0 for i in range(n)] 
              for i in range(n)]

    # Initialize last row of triangle
    for i in range(n):
        tri[n - 1][i] = arr[i]

    # Fill other rows
    i = n - 2
    while(i >= 0):
        for j in range(0, i + 1, 1):
            tri[i][j] = (tri[i + 1][j] + 
                         tri[i + 1][j + 1])
            
        i -= 1

    # Print the triangle
    for i in range(0, n, 1):
        for j in range(0, i + 1, 1):
            print(tri[i][j], end = " ")
        print("\n", end = "")

# Driver Code
if __name__ == '__main__':
    arr = [4, 7, 3, 6, 7]
    n = len(arr)
    printTriangle(arr, n)
