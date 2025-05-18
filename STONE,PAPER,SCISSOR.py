from random import *
def y():
    try:
        w=int(input("How many round you want to play ? "))
        a=["Stone","Paper","Scissor"];p=0;q=0
        for x in range(w):
            b=int(input("\nEnter 1 for Stone,2 for paper, 3 for scissor : "))
            if b!=1 and b!=2 and b!=3:
                raise Exception("\nThe no. entered is not equal to 1,2 or 3.\n")
            c=randint(0,2)
            if c==(b-1):
                print("\nYour choice : ",a[b-1])
                print("Computer's  choice : ",a[c])
                print("\n****\t\tDRAW\t\t****\n")
            elif (b==1 and c==1) or (b==2 and c==2) or (b==3 and c==0):
                print("\nYour choice : ",a[b-1])
                print("Computer's  choice : ",a[c])
                print("\n****\t\tYou loss\t\t****\n")
                q+=1
                print("Your score : ",p)
                print("Computer's score : ",q)
            elif (b==1 and c==2) or (b==2 and c==0) or (b==3 and c==1):
                print("\nYour choice : ",a[b-1])
                print("Computer's  choice : ",a[c])
                print("\n****\t\tYou win\t\t****\n")
                p+=1
                print("Your score : ",p)
                print("Computer's score : ",q)
        if p>q:
            print("\n\t\t\t***************YOU WIN***************\t\t\n")
        elif p==q:
            print("\n\t\t\t***************DRAW***************\t\t\n")
        elif p==0 or q==0:
            pass
        else:
            print("\n\t\t\t***************YOU LOSS***************\t\t\n")            
    except Exception as e:
        print(e)
        y()
y()