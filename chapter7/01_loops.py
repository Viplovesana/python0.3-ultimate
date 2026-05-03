

# FOR-LOOP
'''for i in range(1,20+1):
    print(i)'''
#itrate the list using for loop....

'''l = ["viplove","sujal","monu","praful"]
for i in l:
    print(i)

t = ("viplove",23,"sujal",22,"praful",34,2)
for i in t:
    print(i)'''

'''s = "viplove"
for i in s:
    print(i)'''

# for loop with else condition

'''l = [22,54,78,"viplove sana"]
for item in l:
    print(item)
else:
    print("loop is over")'''

# break and continue and pass statement............

'''for item in range(0,100):
    if(item == 23):
        break# its exit the loop
    print(item)

for item in range(0,100):
    if(item == 23):
        continue# skip the iteration
    print(item)

for i in range(54):
    pass #pass is a null statement in python it instruct to do nothing

i = 0 
while(i<11):
    print(i)
    i=i+1
'''

#.....PRACTISE SET QUESTIONS............................*****

#wap to print multiplication table of a given number using for loop
'''num = int(input("Enter the number:- "))
for i in range(1,11):
    # print(num,"*",i,"=",num * i )
    print(f"{num}*{i}={num*i}")'''

 
# WAp to greet all the person names stored in a list "l" and which starts with s 
'''
l = ["sumit","rohan","sushant","viplove","sajan"]

for item in l:
    if(item.startswith("s")):
        print("aapka deen subh mangal ho",item)  '''

##wap to print multiplication table of a given number using while loop

'''n = int(input("Enter the number for table :-"))
i = 1
while(i < 11):
    print(f"{n} * {i} = {n*i}")
    i=i+1'''

#WAP to find whether a given no is prime or not.

# n = int(input("Enter the number:-"))

# for i in range(2,n):
#     if(n%i==0):
#         print("the no is not prime")
#         break
#     else:
#         print("the no is prime")

# SAME QUE WITH WHILE LOOP.........
'''n = int(input("Enter the number:-"))
if n <= 1:
    print("not a prime no")
else:
    i = 2
    while(i<n):
        if(n%i == 0):
            print("not a prime")
            break
        i=i+1
    else:
        print("prime no")'''

# WAP to find the sum of first n natural numbers using while loop

'''n=int(input("Enter the num:-"))
i = 1
sum = 0
while(i<=n):
    sum = sum + i 
    i=i+1
print(sum)    
'''
'''n=int(input("Enter the num:-"))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)'''


# WAP to calculate the factorial of a given no using for loop

# n=int(input("Enter the num:-"))
#for loop................
# fact = 1
# for i in range(1,n+1): 
#     fact = fact*i
# print(f"the factorial of {n} is {fact}")    
#while loop.............
# fact = 1
# i = 1
# while(i<=n):
#     fact = fact*i
#     i = i+1
# print(f"the fact of {i} is {fact}")

# n=int(input("Enter the num:-"))
i = 1
fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print(fact)
# while(i<=n):
#     fact=fact*i
#     print(fact)
#     i=i+1


# Example 6: Write a program to print your names ten times.       

'''a = "viplove"
for i in range(1,10+1):
    print(i,a)'''

# Write a program to display n natural numbers. 
'''n = int(input("Enter the name wher you can go : ="))
i = 0
while(i<=n):
    print(i)
    i=i+1'''

# Write a program to calculate the sum of numbers. 
''''n = int(input("Enter the name wher you can go : ="))

sum = 1
i = 1 
while(i<=n):
    sum = sum * i
    print(sum)
    i=i+1
'''

# Print numbers until user enters 0
'''n = int(input("Enter the no:-"))
i=1
while n!=0:
    print("you entered ",n)

    n = int(input("Enter the no:-"))
    print("loop ended")'''

# Example 8: Write a program to add 5 in each elements in given list.  
'''l =  [10,20,30,40,50]
for i in range(len(l)):
    l[i]=l[i]+5
print(l)'''

# l =  [10,20,30,40,50]

# i = 0 
# while(i<len(l)):
#     l[i] = l[i] + 5
#     i=i+1
# print(l)

# Example 9: Write a program to add 5 in each elements in given tuple.  
'''t = (10,20,30,40,50)
newTuple = ()
for i in t:
    newTuple = newTuple + (i + 5,)
print(newTuple)'''

# Example 10: Write a program to create a list from given string.  

'''str = "viplove","mukesh","saurabh"
l = list(str)
print(l)'''

# Example 6: Python program to display numbers from a list using a for loop. 

'''
l = [2,4,5,"viplove","rohan",34,"sakshi",89]

for i in l:
    if(type(i) ==  str):
       print(i)
    '''

# while
'''l = [2,4,5,"viplove","rohan",34,"sakshi",89]

i = 0
while(i < len(l)):
    if(type(l[i])==int):
      print(l[i])
    i=i+1'''

# Example 8: WAp whether  the word is palindrome or not 

'''word = input("Enter the word:-")
rev = "" 

for char in word:
    rev = char + rev #m
if word == rev:
    print("the word is palindrom")
else:
    print("the word is not a palindrom") '''   

# word = input("Enter the word:-")
# rev = "" 
# char = 0
# while(char< len(word)):
#     rev = word[char] + rev
#     char = char +1
# if word == rev:
#     print(f"{word} is a palindrom")
# else:
#     print(f"{word} is not a palindrom")   


# Example 10: Python program to check if a given number is an Armstrong number. (153=1**3+5**3+3**3) 

'''num = int(input("Enter the number :-"))
original = num
digits = len(str(num))
tmp = num
sum = 0
for i in range(digits):
    digit = tmp % 10  #3
    sum += digit ** digits #27
    tmp = tmp // 10 #15

if sum == original:
    print("this is a armstrong number")

else:
    print("not an armstrong number")    '''


'''num = int(input("Enter the number :-"))
original = num
digits = len(str(num))
tmp = num
sum = 0

while tmp > 0:
    last_digit = tmp % 10
    sum += last_digit ** digits
    tmp //= 10
if sum == original:
    print("this is a armstrong number")

else:
    print("not an armstrong number")    
'''


# Example 13: Python program to get the Fibonacci series. (0,1,1,2,3,5,8,13,21……………..) 

# num  = int(input("Enter the term for :- "))

# a = 0 
# b = 1
# for i in range(num):
#     print( a, end=" ")
#     c = a + b # 0 + 1 = 1   , 1 + 1 = 2  , 1 + 2 = 3 , 
#     a = b # 1     , 1 , 1
#     b = c # 1     , 2 , 3

'''num  = int(input("Enter the term for :- "))

first_no = 0
snd_no = 1
thrd_no = 0
i = 0
while i < num:
    print(first_no ,end=" ")    
    thrd_no = first_no + snd_no
    first_no = snd_no
    snd_no = thrd_no
    i += 1
'''


# Example 17: Python program to check the validity of password input by users. 
'''psswd = "Mrcool@123"
password = input("Enter the password :-")
if password == psswd:
    print("password is correct")
else:
    print("password is invalid")    
'''

psswd = "Mrcool@123"
password = input("Enter the password :-")

for i in range(len(password)):
    if password[1]  == psswd[i]:
        print("pswd is correct")
        break
    else:
        print("pswd is incorrect")  
        break  











    





