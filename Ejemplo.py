def countdown(n):
    print ("Counting down from", n)
    while n > 0:
        yield n 
        n -= 1
    print ("Done couting")
    
num = int(input("Enter an number\n"))

for i in countdown(num):
    print(i)