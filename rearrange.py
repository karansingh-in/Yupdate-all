import os
import subprocess


#running a command in cmd(NOTE: adminimstrator permission is not needed for this to run)

# subprocess.run(["C:"])
# subprocess.run(["C:\\", "Users\\", "Karan\\", "OneDrive\\" ,"Desktop"])
# files = subprocess.run(["dir"], capture_output=True)

# print(files.stdout.decode())
# command = subprocess.run(["C:\\", "Users\\", "Karan\\", "OneDrive\\" ,"Desktop", "key=clear"], capture_output=True).stdout.decode()

# C:\Users\Karan\OneDrive\Desktop


command1 = ['C:']
command2 = ["C:\\", "Users\\", "Karan\\", "OneDrive\\" ,"Desktop"]
command3 = ['dir']

subprocess.run(command1, shell=True)
subprocess.run(command2, shell = True)
files = subprocess.run(command3, shell = True, capture_output = True).stdout.decode()
#print(files)

subprocess.run(command1, shell=True)

path = 'C:\\Users\\Karan\\OneDrive\\Desktop'

print(os.listdir(path))


# file2 = subprocess.run(command3, shell = True, capture_output = True).stdout.decode()
# # print(file2)

    

  
