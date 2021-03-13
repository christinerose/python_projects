import ROT

enigma_string = "It's fun to deciper a coded message!"

print(" ")
print("**********")
print(" ")


# having a difficult time with this. Progress:

def rot13():

    rot_message = input(
        "Enter a word or phrase to create your secret message: ")

    word_given = ['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz']

    word_output = ['NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijkklm']
    # list like this or dictionary? I'm not sure what to do here.

    lenth = len(rot_message)
    print(lenth)

    for letter in rot_message:

        for match in (word_given):
            if match == letter:
                for position in range(int(word_given)):
                    print(position)

    print(" ")
    print("**********")
    print(" ")

    print(rot_message)

    print(" ")
    print("**********")
    print(" ")


rot13()
