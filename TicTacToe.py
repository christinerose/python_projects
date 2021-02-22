print("****************")


# TicTacToe Field using two simple four loops

#  |   |     0
#---------   1
#  |   |     2
#---------   3
#  |   |     4


for row in range(5):
    if row % 2 == 0:
        print("  |  |  ")
    else:
        print("---------")

print(row)

print("****************")

# in colums:
#   |   |
# 1 2 3 4 5

for row2 in range(5):  # 0,1,2,3,4
    if row2 % 2 == 0:  # 0,2
        for column in range(1, 6):  # 1,2,3,4,5
            if column % 2 == 1:
                if column != 5:
                    print(" ", end="")  # end stays on same line  -- 1,3
                else:
                    print(" ")  # 5
            else:
                print(" |", end="")  # 2
    else:
        print("--------")  # 1,3

print(row2)


print("****************")
