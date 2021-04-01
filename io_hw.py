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

# filename = 'ninja.txt'
# content = 'The ninjas are everywhere.'

# f = open(filename, 'w')
# f.write(content)
# f.close()


def does_file_exist(filename):
    print("testing 'does_file_exist' function")
    try:
        f = open(filename, 'r')
        return True
    except:
        return False


def write_file(filename, content):
    f = open(filename, 'w')
    f.write(content)
    f.close()


def show_file(filename):
    print('testing "show_file" function')
    f = open(filename, "r")   


def delete_file(filename):
    pass


def append_file(filename, content):
    addContent = (input("Type more content here: "))
    chooseName.append(addContent)

    fileContents.append(tempAppend)


def main():

    # filename = {ask for filename}
    chooseName = input("Please choose the file you'd like to open: ")
    
    if does_file_exist(chooseName):
        print("A file called '", chooseName, "' exists! \n")
        choiceAction = input(
            "Would you like to: \nA) Read the file\nB) Delete the file and start over\nC) Append the file. ")
        print("You chose:", choiceAction)

        print(" ")
        print("*****RESULTS:*****")
        print(" ")

        if choiceAction == "A" or "a":  # read, show contents
            show_file(chooseName)

        elif choiceAction == "B" or "b":  
            # delete file and put another empty one in its place
            delete_file(chooseName)
            print("File deleted")
            print(" ")

        elif choiceAction == "C" or "c":  # enter more text to append file
            append_file(chooseName, addContent)


            print("File appended")
            print(" ")
            print("File contents: ", fileContents)

        print(" ")
        print("*****END_RESULTS:*****")
        print(" ")

    else:
        print("That file doesn't exist. Let's create it!")
        newContent = (input("Type new contents here: "))
        write_file(chooseName, newContent)
    

# print(does_file_exist('ninja.txt'))
# print(does_file_exist('ninjaxyzxyzxyz.txt'))

# write_file('ninja.txt', 'this is a test')
# write_file("Test.txt", "This is unreasonably difficult for a beginnger class.")
# write_file('ninja.txt', 'this is a test of the emergency broadcasting system')
# write_file('ninja2.txt', 'monkeypants')

#main()

print("")
print("*Testing Section*")
print("")

show_file('Brian')

print(" ")
print("*****END_PROGRAM*****")
print(" ")
