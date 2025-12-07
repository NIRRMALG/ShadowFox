import random
a,b,c=0,0,0
val2=None
for i in range(20):
    val1=random.randint(1,6)
    print(f"roll {i+1}:{val1}")
    if val1==1:
        a+=1
    if val1==6:
        b+=1
    if val1==6 and val2==6:
        c+=1
    val1,val2=val2,val1
print("Number of times I rolled 1:",a)
print("Number of times I rolled 6:",b)
print("Number of times I rolled 6 in rows:",c)

      
