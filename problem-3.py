a=int(input("Enter a number: "))
res=[]
for i in range(1, a+1):
    odd=2*len(res) + 1
    if odd>a:
        break
    res.append(odd)
print("Output:", ", ".join(map(str, res)))
