friends = ["apple","orange",5,345.06,False,"akash","Rohan"]

print(friends[0])
print(friends[2])
print(friends[4])

friends[0]="grapes" # unlike strings list are mutable
print(friends[0])


# Methods of list.................

# friends.append("viplove")
# print(friends)

# l1 = [1,34,62,2,6,11]
# l1.sort()
# print(l1)

# l1.reverse()
# print(l1)

# print(reverse(l1))


l1 = [8,9,3,6,1,5,78,34,15]

l1.sort()
print(l1)

l1.append(90)
print(l1)

l1.pop(3)
print(l1)

l1.remove(15)
print(l1)

l1.reverse()
print(l1)

l1.insert(3,8)
print(l1)


