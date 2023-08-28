#cp-praveshan-2023/unveiling-the-character-deviation
#COMPLETED
n= int(input()) #input test cases

for _ in range(t):
    s = input().strip()#.toLoweCase()

    deviation = 0
    i=0
    amfoss = "amfoss"
    for char in s:
        if(char != amfoss[i]):
            deviation+=1
        i+=1
    print(deviation)