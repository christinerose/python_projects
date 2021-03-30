# Create a note-taking program. When a user starts it up, it should 
# prompt them for a filename.

# If they enter a file name that doesn't exist, it should prompt 
# them to enter the text they want to write to the file. After they 
# enter the text, it should save the file and exit.

# If they enter a file name that already exists, it should ask 
# the user if they want:

# A) Read the file
# B) Delete the file and start over
# C) Append the file

# If the user wants to read the file it should simply show the 
# contents of the file on the screen. If the user wants to start 
# over then the file should be deleted and another empty one made 
# in its place. If a user elects to append the file, then they 
# should be able to enter more text, and that text should be 
# added to the existing text in the file. 

print(" ")
print("***********")
print(" ")


fileName = []
fileContents = []
count = 0

print(fileName)
print(" ")

while count <= 2:
    chooseName = input("Please choose the file you'd like to open: ")

    # elem in fileName(  # if True... ask to choose another)

    if chooseName in fileName:
        print("A file called '", chooseName, "' exists! \n")
        choiceAction = input(
            "Would you like to: \nA) Read the file\nB) Delete the file and start over\nC) Append the file. ")
        print("You chose:", choiceAction)

        print(" ")
        print("***********")
        print(" ")

        if choiceAction == "A" or "a":  # read, show contents
            #chooseName = open("fileContents.txt", "r")        
            print(fileName, ":", fileContents)
            print(chooseName)

        elif choiceAction == "B" or "b":  # delete file and put another empty one in its place
            chooseName.delete  # ????
            print("File deleted")
            print(" ")

        elif choiceAction == "C" or "c":  # enter more text to append file
            chooseName.append
            print("File appended")
            print(" ")
            
    else:
        print("That file doesn't exist. What would you like to write in the file?")
        tempFile = []
        contents = (input("Type new contents here: "))
        tempFile.append(contents)

        fileName.append(chooseName) #name of file
        fileContents.append(tempFile)


        count += 1

print(" ")
print("***********")
print(" ")

print(fileName)
