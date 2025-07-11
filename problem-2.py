a = int(input("enter number:"))
count=0
num=1
while count < a:
    print(num, end=", " if count < a - 1 else "")
    num+=2
    count+=1
