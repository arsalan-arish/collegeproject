def diamond(n : int, fill : bool=False):
    for i in range(2*n+1):
      for j in range(2*n+1):
        if i<=n:
          if i+j==n or j-i==n:
            print("x",end="")
          elif j<n+i and j>n-i and fill==True:
            print(":",end="")
          else:
            print(" ", end="")
        else:
          if i-j==n or i+j==3*n:
            print("x", end="")
          elif j<2*n-(i-n) and j>i-n and fill==True:
            print(":",end="")
          else:
            print(" ",end="")
      print()
    
diamond(5)