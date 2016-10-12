"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil

__author__ = 'Lindsay Ward'


def main():
    # print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    # print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    #os.chdir('..')
    #for dir_name, subdir_list, file_list in os.walk('.'):

    # loop through each file in the (original) directory
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            new_name = get_fixed_filename(filename)
            print(new_name)

                # Option 1: rename file to new name - in place
                #os.rename(filename, new_name)

                # Option 2: move file to new place, with new name
                # shutil.move(filename, 'temp/' + new_name)


    # Processing subdirectories using os.walk()
    #os.chdir('..')
    #for dir_name, subdir_list, file_list in os.walk('.'):
    #    print("In", dir_name)
    #    print("\tcontains subdirectories:", subdir_list)
    #    print("\tand files:", file_list)


def get_fixed_filename(name):
    current_index = 0
    new_name = name[0].upper()
    for character in name[1:name.index(".")]:
        current_index += 1
        if name[current_index - 1] == " " or name[current_index - 1] == "(":
            new_name += character.upper()
        elif character.isupper() and name[current_index - 1] != " ":
            new_name += " " + character
        else:
            new_name += character
    new_name += name[name.index("."):]
    new_name = new_name.replace(" ", "_").replace(".TXT", ".txt")
    return new_name
main()