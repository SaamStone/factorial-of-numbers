def factorials(num):
    result = 1
    for i in range(1,num+1):
        result*=i
    return result
x = factorials(int(input("Enter the Number : ")))
print(x)