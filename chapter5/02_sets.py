
'''s = {876, 45,1, 5, 32, 54, 5, 5, 5, "viplove"}
print(s)

s.add(566)
print(s,type(s))

print(len(s))

s.remove(54) #it removes the 54 from the set
print(s)

s.pop()
print(s)

s.clear()
print(s)'''

# ...........SET_UNION_AND_INTERTSECTION.....
'''
s1 = {1, 4, 54 ,67}
s2 = {7, 5, 1, 67}

print(s1.union(s2))

print(s1.intersection(s2)) #intersection makes a new set where it pics commom values from set1 and set2'''

# NEW SETS ......................

'''s1 = {}
print(s1)'''

s1 = {2,5,7,64,75,86}

s2 = {7,86,54,43,543,42}

'''print(s1.union(s2))
print(s1.intersection(s2))
print(len(s1))
s1.remove(64)
print(s1)'''
print(s2.pop())

# create Empty set.......
# EmSet = set()
# print(type(EmSet))

# pratice set............................

# write a program to creaye a dictionary of hindi words with values as the in english translation

words = {
    "madad":"help",
    "kutta":"dog",
    "billi":"cat",
    "kitaab":"book"
}
# print(words["madad"])
'''change = input("Enter the name which you translate :-")
print(words[change])'''

# WAP to input eigt numbers from the user and display all the unique numbers(once)
# sets = set()
# print(type(sets))
'''num1 = int(input("Enter the first number :-"))
sets.add(num1)
num2 = int(input("Enter the second number :-"))
sets.add(num2)
num3 = int(input("Enter the third number :-"))
sets.add(num3)
num4 = int(input("Enter the four number :-"))
sets.add(num4)
num5 = int(input("Enter the fivth number :-"))
sets.add(num5)
num6 = int(input("Enter the sixth number :-"))
sets.add(num6)
num7 = int(input("Enter the seven number :-"))
sets.add(num7)
num8 = int(input("Enter the eight number :-"))
sets.add(num8)'''

# print(sets)


# can we have set with 18(int) and '18' (str) as avlaue in it?
 
'''sets = set()
sets.add(18)
sets.add("18")
print(sets)
'''
#create an emoty dictionary.allow 4 frnfs to enter their favorite langauge as values and use key as thier names 

d = {}

name = input("Enter friends name :-")
lang = input("Enter the lang name")
d.update({name:lang})

name = input("Enter friends name :-")
lang = input("Enter the lang name")
d.update({name:lang})

name = input("Enter friends name :-")
lang = input("Enter the lang name")
d.update({name:lang})

name = input("Enter friends name :-")
lang = input("Enter the lang name")
d.update({name:lang})


print(d)
