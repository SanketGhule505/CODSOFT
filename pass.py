# import the string and random modules
import string
import random

# define the characters that can be used in the password
all_characters = string.ascii_letters + string.digits + string.punctuation

# ask the user for the desired length of the password
length = int(input("Enter the length of the password: "))

# generate a password using randomly chosen characters
# using the 'choices' function from the random module
# and joining the resulting characters into a string
password = ''.join(random.choices(all_characters, k=length))

# display the generated password to the user
print("Your password is:", password)


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
