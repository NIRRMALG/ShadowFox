import random
words=["shadowfox","python","java","tailwind","frontend","backend","fullstack","data","science"]
a='y'
while a=='y' or a=='yes':
    secret=random.choice(words)
    attempts=6
    guesses=[]
    displayword=["_ "]*len(secret)
    while attempts>0 and "".join(displayword)!=secret:
        print("\nWord:","".join(displayword))
        print("Attempts left:",attempts)
        print("Guessed letters:",guesses)
        cha=input("enter a character or word:").lower()
        if len(cha)>1:
            if cha==secret:
                displayword=list(secret)
                print("Wow you guessed it right... You won....")
                break
            else:
                print("Wrong guess...")
                attempts-=1
                continue
        
        if cha in guesses:
            print("you have already guessed that letter")
            continue
        guesses.append(cha)
        if cha in secret:
            print("Wow good guess!!!")
            for i,j in enumerate(secret):
                if j==cha:
                    displayword[i]= cha
        else:
            print("Oops! wrong guess...")
            attempts-=1
    if "".join(displayword)==secret:
        print("Hurrah! You Won. The word was,",secret)
    else:
        print("Oops! You Lost. The word was,",secret)
    a=input("\nenter y or yes if you like to continue playing:").lower()
print("Thank You...See you again...")


                
        
    
