import os



class filemanager:
    def __init__(self, file, fextension): 
        #data = open("data.txt", "r")

        # Creating an output file in writing mode
        data = open("data.txt", "w")
  
        # Opening input file and scanning each line
        # from input file and writing in output file
        with open("shift_template_readonly.txt", "r") as scan:
            scan = scan.read()
            data.write(scan)
            data.close()
        print("* FILE CHECK *")
        os.system("pause")

        data = open("data.txt", "r")
        data = data.read()
        newfile.write(f"{newfilename}\n" + data)
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


