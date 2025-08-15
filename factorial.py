def factorials(num):
    result = 1
    for i in range(1,num+1):
        result*=i
    if result % 2 == 0:
            print("its a even number")
    else:
            print("its a odd number")
    return result
x = factorials(int(input("Enter the Number : ")))
print(x)