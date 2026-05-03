# WAp check for palindrom


'''name = input("Enter the name here :-")
rev = "" 
for i in name:
    rev = i + rev
if name == rev:
    print("the sring is palindrom")
else:
    print("not a palindrom")  '''


'''name = "viplove"

print(name.capitalize())
print(name.startswith("vip"))
print(name.endswith("love"))
print(name.replace("love","mylove"))
print(name.isdigit())'''

# text = "myhero"
# freq = {}

# for i in text:
#     if i in freq:
#         freq[i] +=1
#     else:    
#         freq[i] = 1
# print(freq)        


# text = "  hello world   "
# # print(text.strip())
# print(text.replace(" ",""))


# WAP string is anagram or not.....

str1 = input("Enter the 1st name :-")
str2 = input("Enter the 2nd name :-")

if len(str1) != len(str2):
    print("not an anagram")
else:
    freq = {}
    for i in str1:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] = 1
    for i in str2:
        if i in freq:
            freq[1]-=1

        else:
            print("not Anagram")
            break
    else: 
        if all(value == 0 for value in freq.values()):
            print("Anagram")
        else:
            print("Not Anagram")                      






