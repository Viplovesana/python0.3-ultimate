# a = int(input("Enter your age :-"))
'''
if(a>=18):
    print("you are above the age of concent")
    print("good for you")
elif(a<0):
    print("you are entering an invalid age")   
elif(a==0):
    print("you are entering 0 which is not a valid age")     
else:
    print("you are below the age of concent")   '''

'''if(a>=18):
    print("Yes yes yes ahh")
else:
    print("no")'''
# if(a%2 == 0):
#     print("no is even")
# else:
#     print("No is odd")

a1 = int(input("Enter your number :-"))
a2= int(input("Enter your number :-"))
a3 = int(input("Enter your number :-"))
a4 = int(input("Enter your number :-"))

if(a1>a2 and a1>a3 and a1>a4):
    print(f"a1 is {a1} is greater")
elif(a2>a1 and a2>a3 and a2>a4):  
    print(f"a2 is {a2} is greater")
elif(a3>a1 and a3>a2 and a3>a4):
    print(f"a3 is {a3} is greater")
elif(a4>a1 and a4>a2 and a4>a3):
    print(f"a4 is {a4} is greater")
else:
    print("Enter a number :-")    

