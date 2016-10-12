import os, shutil

print("Current directory is", os.getcwd())

os.chdir('FilesToSort')
print(os.listdir('.'))