myUniqueList = []


def no_exist(item):
    global myUniqueList
    # Default to not found yet.
    found = False
    # Check if the item is in the list.
    for x in myUniqueList:
        if x == item:
            found = True
    # If it's not in the list, add it,
    if found == False:
        myUniqueList.append(item)
        return "Added to list"
    # Return expected value.
    return "Already in list"

    # I know the homework said to return True or False, but that's very confusing,
    # as this entire exercise as it's necessary to know Loops, which we haven't
    # learned yet. Plus, my programming partner had to show me both Loops and
    # the <<global myUniqueList>> to get this to work.

    # This course shows rather absurd, random examples in the video but doesn't
    # give us enough information to complete the homework.


print(no_exist(22))

print(no_exist(47))

print(no_exist(22))

print(myUniqueList)
