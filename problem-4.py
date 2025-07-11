data=[1,2,8,9,12,46,76,82,15,20,30]
multiples={}
for i in range(1, 10):
    count=0
    for num in data:
        if num%i==0:
            count+=1
    multiples[i]=count
print("Output:", multiples)
