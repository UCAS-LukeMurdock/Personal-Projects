
#Chess2

import random  as r
#startMap = 
"""
1_|_2_|_3
4_|_5_|_6
7 | 8 | 9
"""

map1 = "123\n456\n789"
uToken = "X"
cToken = "O"

print(map1)
for num in range(10):
    uPlace = int(input("Where do you want to place your token?: ")) - 1
    if uPlace >=3:
        uPlace += 1
    if uPlace >=7:
        uPlace += 1
    map1 = map1.replace((map1[uPlace]),uToken)
    print(map1)
    cPlace = r.randrange(1,10)-1
    print(f"Robot's place: {cPlace+1}")
    if cPlace >= 3:
        cPlace += 1
    if cPlace >=7:
        cPlace += 1
    map1 = map1.replace((map1[cPlace]),cToken)
    print(map1)
print("END")