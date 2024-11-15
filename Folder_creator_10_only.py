# Folder creator version 2.0. this tool is same as the Folder_creator_0_to_100 1.0,
# But difference is this tool creates 10 folders only. but you can edit if you know how to edit. Good luck editing the "TOOL".  :) :)  :) :) :) :) 


import os

# Here you need to put your own path where you want the folders to be

path= 'C:\\Users\\LUCIfer\\Desktop\\test folder'
os.chdir(path)
for i in range (10,21):
        NewFolder='0' + str(i)
        os.makedirs(NewFolder)

print("Thank Me Later :)")

# made by BORIX

