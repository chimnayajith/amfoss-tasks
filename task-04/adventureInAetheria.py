#cp-praveshan-2023/adventure-in-aetheria
#COMPLETED
n = int(input()) #input number of cities

time = list(map(int , input().split(" ")))

if(time.count(min(time)) == 1):
    print(time.index(min(time))+1)
else : 
    print("Still Aetheria")