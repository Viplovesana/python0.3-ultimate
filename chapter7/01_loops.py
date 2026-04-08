

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

n = int(input("Enter the number for table :-"))
i = 1
while(i < 11):
    print(f"{n} * {i} = {n*i}")
    i=i+1