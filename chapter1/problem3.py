import os
# select the directory whose content you want to list
path = "/"

contents = os.listdir(path)

for item in contents:
    print(item)