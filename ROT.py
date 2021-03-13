#import ROT

enigma_string = "It's fun to deciper a coded message!"

print(" ")
print("**********")
print(" ")


# txt = "Hello, welcome to my world."
# x = txt.find("welcome")
# print(x)


# having a difficult time with this. Progress:

def rot13():

    rot_message = input(
        "Enter a word or phrase to create your secret message: ")

    word_given = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    word_output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijkklm'
    # list like this or dictionary? I'm not sure what to do here.

    length = len(rot_message)
    print("length is", length)

    for letter in rot_message:
        # print(letter)

        result = []
        for match in (word_given):
            if match == letter:
                # print(match)  #WORKS
                position_in_given = word_given.find(match)
                # returns number position in string, ex: 36
                # print(position_in_given)  #WORKS

                # Take number position (position_in_given) and index into word_output with some number, returning letter in string
                letter_out = word_output[position_in_given]
                print(letter_out)

            for x in range(int(letter_out)):
            result.append(x)
            print(result)

#        findPos = word_given.find(letter, 0, length)
#        print(findPos)

    # for position in range(int(word_given)):
    #     print(position)

    # letterPosition = match.find(word_given)
    # print(letterPosition)

        print(" ")
        print("**********")
        print(" ")

        print(rot_message)

        print(" ")
        print("**********")
        print(" ")


rot13()
