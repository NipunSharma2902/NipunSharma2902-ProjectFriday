a=0
i='y'
proceed='y' or 'Y'
for a in range (1,10):
       if i == proceed:
              x=int(input("first number:"))
              y=int(input("second number:"))
              print("What do you want to do?")
              print()
              print("1.Sum")
              print("2.Subtract")
              print("3.Product")
              print("4.Divide")
              ch=int(input("  enter your choice number: "))
              z=0
              if ch==1:
                     z=x+y
              elif ch==2:
                     if x>y:
                         z=x-y
                     else:
                         z=y-x
              elif ch==3:
                     z=x*y
              elif ch==4:
                     if x>y:
                         z=x/y
                     else:
                         z=y/x
                     
              print("Result is:",z)
              input()
              i=input("Do you want to continue(y/n): ")
       else:
              input("Press any key to Exit")
              exit()
