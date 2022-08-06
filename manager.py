from datetime import datetime

import calendar
import os


today = datetime.now()

month = today.strftime('%B')
daycount = today.strftime('%d') 
year = today.strftime('%Y')



daycount = int(daycount)

daycount = daycount + 1

day = str(daycount)

newfilename = month + " " + day + ", " + year 
txtfilename = month + " " + day + ", " + year + ".txt"

newfile = open(txtfilename, 'x')
newfile.write(f"{newfilename}\n* DTLA *\n\n\n\n\n"
              "XX:XX - Onsite\n"
              "\n"
              "Tasks\n"
              "\tMonday.com\n"
              "\t- added time for remote hands requests\n\n"
              "Rounds\n"
              "\t1202\n"
              "\tPressure Dial: 20 psi\n"
              "\tCRAC-1: 73/29\n"
              "\tCRAC-2: 73/29\n"
              "\tCRAC-3: \n"
              "\tCRAC-4: \n"
              "\tNOTES: \n"
              "\t1220\n"
              "\tCRAC-1: 73/29\n"
              "\tCRAC-2: 73/29\n"
              "\tCRAC-3: \n"
              "\tCRAC-4: \n"
              "\tMain Supply Pipe Leak: no leak \n"
              "\tNOTES: \n"
              "\t1208\n"
              "\tCRAC-1: 73/29\n"
              "\tCRAC-2: \n"
              "\tCRAC-3: \n"
              "\tCRAC-4: \n"
              "\tNOTES: \n"
              "\t1611\n"
              "\tCRAC-1: 73/29\n"
              "\tCRAC-2: 66/48\n"
              "\tCRAC-3: 78/36\n"
              "\tCRAC-4: \n"
              "\tCRAC-5: \n"
              "\tNOTES: \n"
              "\t1600\n"
              "\tHoneywell: 82\n"
              "\tCRAC-1: 76/35\n"
              "\tCRAC-2: 66/48\n"
              "\tCRAC-3: 78/36\n"
              "\tNOTES: \n"
              "\t300\n"
              "\tCRAC-1: 74/42\n"
              "\tCRAC-2: 79/37\n"
              "\tCRAC-3: 70/48\n"
              "\tCRAC-4: 77/41\n"
              "\tCRAC-5: 67/53\n"
              "\tCRAC-6: 75/42\n"
              "\tCRAC-7: 73/44\n"
              "\tCRAC-8: 77/37\n"
              "\tCRAC-9: 75/33\n"
              "\tNOTES: \n"
              "\t305\n"
              "\tCRAC-1: 73/29\n"
              "\tCRAC-2: 66/48\n"
              "\tCRAC-3: 78/36\n"
              "\tCRAC-4: \n"
              "\tCRAC-5: \n"
              "\tNOTES: \n"
              "\t2805\n"
              "\tCRAC-1: 69/35\n"
              "\tCRAC-2: \n"
              "\tCRAC-3: 64.4\n"
              "\tCRAC-4: 62.6\n"
              "\tNOTES: \n"
              "\t400\n"
              "\tCRAC-1: 71/49\n"
              "\tCRAC-2: 72/47\n"
              "\tCRAC-3: \n"
              "\tCRAC-4: \n"
              "\tCRAC-5: \n"
              "\tCRAC-6: \n"
              "\tCRAC-7: \n"
              "\tDC-PLANT-1: \n"
              "\tNOTES: \n"
              "\t611\n"
              "\tUPS-1: Clear!\n"
              "\tUPS-2: Clear!\n"
              "\tUPS-3: Clear!\n"
              "\tUPS-4: Clear!\n"
              "\tNOTES: \n"
              "\t609\n"
              "\tAll good!\n"
              "\tBuilding Lobby: Clear!\n"
              "\tPre-action PNL: All clear!\n"
              "\tNOTES: \n\n"

              "XX:XX - Offsite\n\n\n\n\n"
              "NOTES: \n")

newfile.close()

print("* FILE CHECK *")
os.system("pause")

#newfile.write("XX:XX - Onsite\n")
#newfile.write("XX:XX - Offsite\n")


# Get the list of all files and directories
# in the root directory
cwd = os.getcwd()
dir_list = os.listdir(cwd)

print(cwd)

print("Files and directories in ", cwd,":") 
  
# print the list
print(dir_list)

path = os.path.join(cwd, txtfilename)

os.remove(path)
print("Deleting created file: ", newfile)

##os.close(dir_fd)  # don't leak a file descriptor

#file = open(r"C:\Users\wmartinez\OneDrive - Crown Castle USA Inc\Documents\Shift Reports\Shift Report TEMPLATE.txt")

#file = 

#print(file.read())

#print(today.strftime('%B'), today.strftime('%d,'),d today.strftime('%Y.txt'))
#print(today.strftime('%d'))
#print(",")
#print(today.strftime('%Y'))


##.strftime('%A') prints Day only ex: Monday  wz*T.+d?L3UY2K_SG!RHT9x?
