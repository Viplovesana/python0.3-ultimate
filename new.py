# input "abbbab"
# Output : { "a": 2, "b" : 3}

aBc = input("Enter somthinthing :-")
freq = {}
for i in aBc:
    if i in freq:
     freq[i] += 1
    print(freq)

