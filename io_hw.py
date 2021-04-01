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
print("*****START*****")
print(" ")

# f = open(filename, 'w')
# f.write(content)
# f.close()

import os


def does_file_exist(filename): #WORKS
    try:
        f = open(filename, 'r')
        return True
    except:
        return False


def write_file(filename, content):  #WORKS!
    f = open(filename, 'w')
    f.write(content)
    f.close()

    print("")
    print("File created")
    print("Contents of", filename, ":")
    show_file(filename)


def show_file(filename): #WORKS!
    f = open(filename, "r")   
    print(f.read())


def delete_file(filename): #WORKS!
    os.remove(filename)
    f = open("newFile.txt", "x")
    #f.close()

    print("File deleted")
    print(" ")
    print("New empty file called 'newFile.txt' created.")
    print(" ")


def append_file(filename, content): #WORKS
    f = open(filename, "a")
    f.write(content)
    f.close()

    print("")
    print("File appended")
    print("Contents of", filename, ":")
    show_file(filename)



def main():

    # filename = {ask for filename}
    chooseName = input("Please choose the file you'd like to open: ")
    
    if does_file_exist(chooseName): 
        print("A file called '", chooseName, "' exists! \n")
        choiceAction = input("Would you like to: \nA) Read the file\nB) Delete the file and start over\nC) Append the file. ")
        print("You chose:", choiceAction)

        print(" ")
        print("**********")
        print(" ")

        if choiceAction == "A" or choiceAction == "a":  
            # read, show contents
            show_file(chooseName)

        elif choiceAction == "B" or choiceAction == "b": 
            # delete file and put another empty one in its place
            delete_file(chooseName)

        elif choiceAction == "C" or choiceAction == "c":  
            # enter more text to append file
            addContent = input("Type additional content here: ")
            append_file(chooseName, addContent)

    else:
        print("That file doesn't exist. Let's create it!")
        newContent = input("Type new contents here: ")
        write_file(chooseName, newContent)
    

main()

print(" ")
print("*****END_PROGRAM*****")
print(" ")
