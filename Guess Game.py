import random
str=["Ironman","Captain America","HawkEye","Black Widow","Hulk","Thor"]
x=random.randint(0,5)
word=str[x]
length=len(str[x])
i=0
string=""
for i in range(0,length):
    if str[x][i]=="A":
        a="*"
    elif str[x][i]=="a":
        a="*"
    elif str[x][i]=="E":
        a="*"
    elif str[x][i]=="e":
        a="*"
    elif str[x][i]=="I":
        a="*"
    elif str[x][i]=="i":
        a="*"
    elif str[x][i]=="O":
        a="*"
    elif str[x][i]=="o":
        a="*"
    elif str[x][i]=="U":
        a="*"
    elif str[x][i]=="u":
        a="*"
    else:
        a=str[x][i]
    string+=a
    i+=1
    
chance=0
for chance in range(0,4):
    print(string)
    guess=input("Guess the missing character: ")
    print("Your guess: ",guess)
    i=0
    for i in range(0,length):
        if word[i]==string:
            str[x][i]=chance
        i+=1
    chance+=1
input()
