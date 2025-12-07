hei=float(input("Enter height in metres:"))
wei=float(input("Enter weight in kilo gram:"))
bmi=wei/(hei*hei)
if bmi>30:
    print("Obesity")
elif bmi>25 and bmi<=29:
    print("Over weight")
elif bmi>18.5 and bmi<=25:
    print("Normal")
else:
    print("Under weight")

    
