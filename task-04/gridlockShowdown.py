#cp-praveshan-2023/gridlock-showdown
# COMPLETED
t = int(input()) #input test cases

sum_x , sum_y , sum_z = 0,0,0

for tc in range(t):
    x, y, z = map(int, input().split())

    sum_x += x
    sum_y += y
    sum_z += z
if (sum_x == 0 and sum_y == 0 and sum_z == 0):
    print("YES")
else:
    print("NO")