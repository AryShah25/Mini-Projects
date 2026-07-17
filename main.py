import random

computer=random.choice([0,1,2])
str = input("enter your choice:")
dict = {"stone":0,"paper":1,"scisor":2}
revdict = {0:"stone",1:"paper",2:"scisor"}

user = dict[str]

print(f"user select {revdict[user]} and computer select {revdict[computer]}")

if(computer==user):
    print("It's a Draw")

else:
    if(computer==0 and user==1):
        print("User Won")
    elif(computer==0 and user==2):
        print("Computer Won")
    elif(computer==1 and user==0):
        print("Computer Won")
    elif(computer==1 and user==2):
        print("User Won")
    elif(computer==2 and user==0):
        print("User Won")
    elif(computer==2 and user==1):
        print("Computer Won")
    else:
        print("something went wrong")
    