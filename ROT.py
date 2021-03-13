print(" ")
print("**********")
print(" ")

print("It's fun to create a coded message!")

print(" ")

# FIND EXAMPLE
# txt = "Hello, welcome to my world."
# x = txt.find("welcome")
# print(x)


# having a difficult time with this. Progress:

result = []


def rot13():

    rot_message = input(
        "Enter a word or phrase to create your secret message: ")

    word_given = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    word_output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijkklm'
    # list like this or dictionary? I'm not sure what to do here.

    length = len(rot_message)
    #print("length is", length)

    for letter in rot_message:
        # print(letter)

        for match in (word_given):
            if match == letter:
                # print(match)  #WORKS
                position_in_given = word_given.find(match)
                # returns number position in string, ex: 36
                # print(position_in_given)  #WORKS

                # Take number position (position_in_given) and index into word_output with some number, returning letter in string
                letter_out = word_output[position_in_given]
                # print(letter_out)  # WORKS!!!

                result.append(letter_out)
                # print(result)  #WORKS

    print(" ")
    print(" ")

    encoded_word = "".join(result)
    print('"'+rot_message+'"', "encoded is", encoded_word)

    print(" ")
    print("**********")
    print(" ")


rot13()
