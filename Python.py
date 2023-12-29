try:
    j = 1
    while j != 0:    
    # Swastik Code 
        n=int(input("Enter any odd number greator than or equal to 5 : "))
        while n%2 == 0 or n<=4:
            n=int(input("Enter any odd number greator than or equal to 5 : "))
        v = input("entre the character you want to the structure of ")

        for i in range(1,n+1):
            for j in range(1,n+1):
                if j==1 and i<(n+1)/2 or j==(n+1)/2 or i==(n+1)/2 or i==1 and j>(n+1)/2 or j==n and i>(n+1)/2 or i==n and j<(n+1)/2:
                    if j==n:
                        print(v)
                    else:
                        print(v,end=" ")
                else:
                    if j==n:
                        print(" ")
                    else:
                        print(" ",end=" ")

        n=int(input("Enter any odd number greator than or equal to 5 : "))
        while n%2 == 0 or n<=4:
            n=int(input("Enter any odd number greator than or equal to 5 : "))
        v = input("entre the character you want to the structure of ")
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j==(n+1)/2 or i==(n+1)/2 or i==j or i+j==n+1:
                    if j==n:
                        print(v)
                    else:
                        print(v,end=" ")
        #    ****** Asterisk Code Below ********
                else:
                    if j==n:
                        print(" ")
                    else:
                        print(" ",end=" ")
        j=int(input("To continue again (entre 1) otherwise 0 to exit : "))
        if j==0:
            print("program finished")
            break                         
except:
    print("\n","invalid syntax")
    print("\n","process terminated")
