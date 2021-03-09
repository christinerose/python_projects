import ROT

enigma_string = "It's fun to deciper a coded message!"


# having a difficult time with this. Progress:

def rot13():

    rot_message = input(
        "Enter a word or p hrase to create your secret message: ")

    word_given = ['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz']

    word_output = ['NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijkklm']
    # list like this or dictionary? I'm not sure what to do here.

    for letter in rot_message:
        while letter <= len(rot_message):
            print(letter)

    print(" ")
    print("**********")
    print(" ")

    print(rot_message)


rot13()
