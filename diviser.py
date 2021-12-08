n=int(input("pls enter the number of apple Harry has gotten: "))
mn=int(input("pls enter minimum number of student: "))
mx=int(input("pls enter minimum number of student: "))
if mn!=mx:
    for i in range(mn, (mx+1)):
        if n%i==0:
            print(f"{n} is divisible of {i}")
        else:
            print(f"{n} is not divisible of {i}")
else:
    print("You don't enter a valid range")