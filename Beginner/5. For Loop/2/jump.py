print("enter y or yes if you are tired. enter n or no if you are not tired:")

for i in range(1,11):
    print("jumping 10 jacks...")
    if i!=10:
        a=input("Are you tired:")
        if a=='y' or a=='yes':
            break
        elif a=='n' or a=='no':
            print(f"There are {(10-i)*10} jumping jacks remaining")
if i==10:
    print("Congartulations you have finished 100 jumping jacks")
else:
    print(f"you have finished {i*10} jumping jacks.")    
