# COMPLETED
s = input().strip()
hello= "hello"
i = 0
for char in s:
    if (i < 5 and char == hello[i]):
        i+= 1 #move to the next character

    # all 5 characters are found
    if (i == 5): 
        print("YES")
        break
else:
    print("NO")


# hlelo